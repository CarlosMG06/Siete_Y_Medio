import decks
import utils
import printing
import titles
import texts
import players as p
import random
import sizes
from db_access_config import execute_transaction_in_db, insert_query

selected_players = {}
played_cards = [] #Lista con las cartas jugadas hasta el momento para que no se repitan
active_deck = None #Cambia dinámicamente durante la ejecución del juego
active_deck_id = None 
max_rounds = 5
players_in_session = {} #Donde se guardan los jugadores y los valores dinámicos que ocurren durante la partida

def initialize_players(players):
    
    initialized_players = players.copy()

    for player in initialized_players.keys():
        initialized_players[player].update( 
            {
                "bank": False,
                "initialCard": "",
                "bet": 0,
                "points": 20,
                "cards": [],
                "cards_value": 0,
                "priority": 0
            }
        )

    return initialized_players

def start_game(padding):
    global active_deck, players_in_session
    if active_deck != None:
        
        #Se inicializan los jugadores soptionados
        players_in_session = initialize_players(selected_players)
        #Se barajan las cartas
        active_deck = utils.shuffle_cards(active_deck)

        #Se muestra la pantalla principal para mostrar los jugadores que hay, etc.
        printing.print_title(titles.TITLES["game_title"], padding=padding)
        printing.print_main_game_scene(players_in_session, padding)
        
        input()
    
    else:
        printing.print_line(texts.TEXTS["invalid_deck"], padding, "=")
        input()
    


def deal_card(player):
    card_list = list(active_deck.keys())
    card = card_list[random.randint(0, len(card_list) - 1)]
    while card in played_cards:
        card = card_list[random.randint(0, len(card_list) - 1)]

    played_cards.append(card)
    players_in_session[player]["cards"].append(card)
    players_in_session[player]["cards_value"] += active_deck[card]["real_value"]
    return active_deck[card]['literal'], players_in_session[player]["cards_value"]

def assign_priority(players_in_session):
    """Se añade la prioridad repartiendo una carta a todo el mundo
    :param players_in_session: (dict) -> diccionario de diccionarios de los jugadores
    :return: (list) -> Devuelve una lista con los diccionarios de los jugadores ordenados"""
    global played_cards
    

    for player in players_in_session.keys():
        #Se reparte una carta a cada jugador
        deal_card(player)
        #Se asigna esa carta como la carta inicial del jugador
        players_in_session[player]["initialCard"] = players_in_session[player]["cards"][0]

    #Para asignar prioridades se compararán uno por uno en un diccionario los valores de los jugadores
    dicValores = {}

    for jugador in players_in_session:
        dicValores[jugador] = {}
        dicValores[jugador]["numValue"] = active_deck[players_in_session[jugador]["cards"][0]]["value"]
        dicValores[jugador]["priority"] = active_deck[players_in_session[jugador]["cards"][0]]["priority"]
    
    ordered = sort_priorities(dicValores)

    #Se muestra por pantalla lo que ha recibido cada uno y quién será la banca
    utils.clear_screen()
    printing.print_title(titles.TITLES["game_title"], padding=sizes.TOTAL_WIDTH)
    printing.print_line_centered(" Priority assignment ", "=")
    print()
    for jugador in players_in_session:
        printing.print_line_centered(f"{players_in_session[jugador]['name']} has received the card: {active_deck[players_in_session[jugador]['cards'][0]]['literal']}", " ")

    #Según el orden hay que asignar una banca y el orden de jugada.
    orderTxt = "Order will now be: "
    for jugador in ordered: #ordenado está de menor prioridad a mayor, la banca es el último index
        
        players_in_session[jugador]["priority"] = ordered.index(jugador) + 1

        if ordered.index(jugador) + 1 == len(ordered):
            orderTxt += players_in_session[jugador]["name"]
            players_in_session[jugador]["bank"] = True
            print()
            printing.print_line_centered(f" {players_in_session[jugador]['name']} is now the bank ", "=")
            print()
            printing.print_line_centered(orderTxt, " ")
        else:
            orderTxt += players_in_session[jugador]["name"] + " -> "
            players_in_session[jugador]["bank"] = False
    
    #Por último se limpia la lista de cartas jugadas y se eliminan las cartas  y los puntos de los jugadores
    for jugador in players_in_session:
        players_in_session[jugador]["cards"] = []
        players_in_session[jugador]["cards_value"] = 0
        
    played_cards = []

    input()

    return ordered

def sort_priorities(dic):
    """Dic con los valores númericos y las prioridades de la carta de los jugadores"""
    result = []

    dic_list = list(dic)

    result.append(dic_list[0])
    for jugador in dic_list:
        #Ordenar las prioridades de menor a mayor, es decir si sacan 2, 8 y 5, la prioridad es 1, 3, 2   
        if dic_list.index(jugador) != 0:
            if active_deck[players_in_session[result[-1]]["cards"][0]]["value"] == active_deck[players_in_session[jugador]["cards"][0]]["value"]: #Si el valor es igual se comprueba la prioridad
                if active_deck[players_in_session[result[-1]]["cards"][0]]["priority"] < active_deck[players_in_session[jugador]["cards"][0]]["priority"]:
                    result.append(jugador)
                else:
                    result.insert(-1, jugador) 
                
            else:

                if active_deck[players_in_session[result[-1]]["cards"][0]]["value"] < active_deck[players_in_session[jugador]["cards"][0]]["value"]:
                    result.append(jugador)
                else:
                    offset = -1

                    while active_deck[players_in_session[result[offset]]["cards"][0]]["value"] > active_deck[players_in_session[jugador]["cards"][0]]["value"]:
                        if len(result) != abs(offset):
                            if (active_deck[players_in_session[result[offset - 1]]["cards"][0]]["value"] > active_deck[players_in_session[jugador]["cards"][0]]["value"]
                                or (active_deck[players_in_session[result[offset - 1]]["cards"][0]]["value"] == active_deck[players_in_session[jugador]["cards"][0]]["value"]
                                    and active_deck[players_in_session[result[offset - 1]]["cards"][0]]["priority"] > active_deck[players_in_session[jugador]["cards"][0]]["priority"])):
                                offset -= 1
                                continue
                            break
                        else:
                            break
                    
                    if len(result) == 1 or abs(offset) == len(result):
                        result.insert(0, jugador)
                    else:
                        result.insert(offset, jugador)

    return result

def order_card(current_player):
    def draw_card(current_player):
        new_card, new_value = deal_card(current_player)
        printing.print_line_centered("New card ordered!", " ")
        printing.print_line_centered(f"The new card is: {new_card}", " ")
        printing.print_line_centered(f"Now you have {new_value}", " ")
        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
    
    def draw_confirmation(risk):
        if risk > 0:
            printing.print_line_centered(f"The risk to exceed 7.5 is {risk}%, are you sure? (y/n)", " ")
            sure = str(input())
            if sure.lower() != "y":
                return False
        return True
    
    def exceeded_7·5(current_value):
        if current_value <= 7.5:
            return False
        else:
            printing.print_line_centered("You have exceeded 7.5 points!", " ")
            utils.press_to_continue()
            return True

    bank = players_in_session[current_player]["bank"]
    current_value = players_in_session[current_player]["cards_value"]

    if not bank:
        if current_value == 7.5:
            printing.print_line_centered("You already have 7.5 points!", " ")
            utils.press_to_continue()
        elif not exceeded_7·5(current_value):
            risk = calculate_risk(current_value)
            if draw_confirmation(risk):
                draw_card(current_player)
    else:
        value_to_match = max(
            (data["cards_value"] for player, data in players_in_session.items() 
            if player != current_player and data["cards_value"] <= 7.5),
            default = 0
        )
        if current_value < value_to_match:
            risk = calculate_risk(current_value)
            if draw_confirmation(risk):
                draw_card(current_player)                 
        elif not exceeded_7·5(current_value):
            printing.print_line_centered("You've already beaten all other players!", " ")
            utils.press_to_continue()

def calculate_risk(current_value):
    sum_valid = 0
    total_cards = 0
    for card in active_deck.values():
        if card not in played_cards:
            if current_value + card["real_value"] <= 7.5:
                sum_valid += 1
            total_cards += 1
    risk = 100 - (sum_valid / total_cards) * 100
    return risk 
                    
def order_card_human_automatic(player):
    while True:
        if players_in_session[player]["cards_value"] < 7.5:
            risk = calculate_risk(players_in_session[player]["cards_value"])
            acceptable_risk = 0

            if players_in_session[player]["type"] == "Moderated":
                acceptable_risk = 50
            if players_in_session[player]["type"] == "Cautious":
                acceptable_risk = 30
            if players_in_session[player]["type"] == "Bold":
                acceptable_risk = 80

            if risk < acceptable_risk:
                deal_card(player)
            else:
                break             
        else:
            break

def check_losers_winners(order):
    """Devuelve 

    losers (list) -> Es una lista de str con los ids de los jugadores
    
    En la lista winners nunca estará la banca, la forma de saber si la banca es el único ganador es comprobando que no esté en la lista losers
    """

    losers = []

    if players_in_session[order[-1]]["cards_value"] == 7.5: #Gana la banca contra todos
        losers = order[:-1]
        return losers
    
    for player in order[:-1]: #Comprobar contra quién gana y quién pierde
        if (players_in_session[player]["cards_value"] <= players_in_session[order[-1]]["cards_value"]
            and players_in_session[player]["cards_value"] <= 7.5
            and players_in_session[order[-1]]["cards_value"] <= 7.5):
            # Si tiene menos o los mismos puntos que la banca y ambos no se han pasado de 7.5
            losers.append(player)

        elif players_in_session[player]["cards_value"] > 7.5: #Si se pasa de 7.5 puntos
            losers.append(player)
        
        else: # Pierde la banca
            losers.append(order[-1])


    #Las listas ya están ordenadas de menor a mayor prioridad
    return losers


def distribute_points(order):
    """Se reparten los puntos apostados según quién ha ganado y quién no.
    :param order: (list) -> el orden de los jugadores, en el cual el último es la banca
    :return: None"""
    losers = check_losers_winners(order)

    utils.clear_screen()
    printing.print_title(title=titles.TITLES["game_title"], padding=sizes.TOTAL_WIDTH)

    printing.print_line_centered(f" ROUND RESULTS ", "=")

    if len(losers) == 1:
        if players_in_session[losers[0]]["bank"]: #Si el único perdedor es la banca se tendrá que repartir por prioridades
            can_bank_pay = True

            #El orden en "orden" es de menor a mayor prioridad, pero la repartición de puntos es de mayor a menor prioridad
            for player in order[::-1][1:]: #Se invierte el orden de "orden" y se skipea el index 1, que es la banca
                if can_bank_pay:
                    if players_in_session[player]["points"] > 0:
                        if players_in_session[player]["cards_value"] != 7.5:
                            #Si la apuesta es mayor que el dinero que tiene la banca (no tiene dinero suficiente para pagar)
                            if players_in_session[player]["bet"] > players_in_session[order[-1]]["points"] or players_in_session[player]["bet"] - players_in_session[order[-1]]["points"] == 0:                    
                                players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                                printing.print_line_centered(f"Bank has paid {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                                players_in_session[order[-1]]["points"] = 0
                                can_bank_pay = False
                                

                            else:
                                players_in_session[player]["points"] += players_in_session[player]["bet"]
                                players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"]
                                printing.print_line_centered(f"Bank has paid {players_in_session[player]['bet']} to {players_in_session[player]['name']}", " ")
                        else:
                            #Si la apuesta es mayor que el dinero que tiene la banca (no tiene dinero suficiente para pagar)
                            if players_in_session[player]["bet"] * 2 > players_in_session[order[-1]]["points"] or (players_in_session[player]["bet"] * 2) - players_in_session[order[-1]]["points"] == 0:                    
                                players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                                printing.print_line_centered(f"Bank has paid {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                                players_in_session[order[-1]]["points"] = 0
                                can_bank_pay = False
                                

                            else:
                                players_in_session[player]["points"] += players_in_session[player]["bet"] * 2
                                players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"] * 2
                                printing.print_line_centered(f"Bank has paid {players_in_session[player]['bet'] * 2} to {players_in_session[player]['name']}", " ")
                else:
                    printing.print_line_centered(f"Bank is out of money and can't pay anymore.", " ")



        else: #Si el único perdedor no es la banca
            can_bank_pay = True
            for player in order: #Aquí el único perdedor (que no es la banca) le paga a la banca
                if player in losers and players_in_session[player]["points"] > 0: #Este perdedor no es la banca
                    players_in_session[order[-1]]["points"] += players_in_session[player]["bet"]
                    players_in_session[player]["points"] -= players_in_session[player]["bet"]
                    printing.print_line_centered(f"{players_in_session[player]['name']} pays {players_in_session[player]['bet']} to the bank", fill_char=" ")
                
            #Aquí es donde se reparten los puntos a los ganadores, aunque la banca en este punto aunque haya ganado contra 1 ya tiene los puntos gracias al bucle anterior
            for player in order[::-1][1:]: #Se invierte el orden de "orden" y se skipea a la banca
                 #Aquí se tratan los ganadores (en el caso de que solo haya un perdedor)
                if player not in losers and players_in_session[player]["points"] > 0:
                    if players_in_session[player]["bank"] == False: #En caso de que no sea la banca, ya que no hace falta hacer nada con la banca si es ganadora en este momento
                        #La banca tiene que pagar a los ganadores
                        if can_bank_pay:
                            if players_in_session[player]["cards_value"] != 7.5:
                                #En caso de que no tenga para pagar    
                                if players_in_session[order[-1]]["points"] < players_in_session[player]["bet"] or players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] == 0:
                                    players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                                    printing.print_line_centered(f"Bank has paid {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                                    players_in_session[order[-1]]["points"] = 0
                                    can_bank_pay = False
                                    
                                else:
                                    players_in_session[player]["points"] += players_in_session[player]["bet"]
                                    players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"]
                                    printing.print_line_centered(f"Bank has paid {players_in_session[player]['bet']} to {players_in_session[player]['name']}", " ")

                            else:
                                if players_in_session[order[-1]]["points"] < players_in_session[player]["bet"] * 2 or players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] * 2 == 0:
                                    players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                                    printing.print_line_centered(f"Bank has paid {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                                    players_in_session[order[-1]]["points"] = 0
                                    can_bank_pay = False
                                    
                                else:
                                    players_in_session[player]["points"] += players_in_session[player]["bet"] * 2
                                    players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"] * 2
                                    printing.print_line_centered(f"Bank has paid {players_in_session[player]['bet'] * 2} to {players_in_session[player]['name']}", " ")

    else:
        #Comprobar si en los más de un jugadores que hay perdedores está la banca, si no, eso quiere decir que la banca ha ganado a todos

        #Primero se suma todo lo de los perdedores que no sean la banca a la banca
        for player in losers:
            if players_in_session[player]["bank"] == False and players_in_session[player]["points"] > 0:
                printing.print_line_centered(f"{players_in_session[player]['name']} pays {players_in_session[player]['bet']} to the bank", " ")
                players_in_session[order[-1]]["points"] += players_in_session[player]["bet"] #Se suma a la banca los puntos
                players_in_session[player]["points"] -= players_in_session[player]["bet"] #Se le resta al perdedor los puntos


        #En este punto los jugadores perdedores ya han pagado a la banca, por lo que se omite a la banca
        can_bank_pay = True
        for player in order[::-1][1:]: #Se invierte y skipea la banca
            if player not in losers and players_in_session[player]["points"] > 0: #Si el jugador es ganador (y no la banca)
                if can_bank_pay:
                    if players_in_session[player]["cards_value"] == 7.5: #Si el jugador tiene 7.5 cards_value (gana el doble de la bet)
                        #En caso de que cuando pague tenga más o igual a 0 paga
                        if players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] * 2 == 0 or players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] * 2 > 0:
                            players_in_session[player]["points"] += players_in_session[player]["bet"] * 2
                            players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"] * 2
                            printing.print_line_centered(f"The Bank pays {players_in_session[player]['bet'] * 2} to {players_in_session[player]['name']}", " ")
                        else:
                            #En caso de que no tenga para pagar paga con lo que le queda.
                            players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                            printing.print_line_centered(f"The Bank pays {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                            players_in_session[order[-1]]["points"] = 0
                            can_bank_pay = False
                            
                        
                    else:
                        #En caso de que cuando pague tenga más o igual 0 paga
                        if players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] == 0 or players_in_session[order[-1]]["points"] - players_in_session[player]["bet"] > 0:
                            players_in_session[player]["points"] += players_in_session[player]["bet"]
                            players_in_session[order[-1]]["points"] -= players_in_session[player]["bet"]
                            printing.print_line_centered(f"The Bank pays {players_in_session[player]['bet']} to {players_in_session[player]['name']}", " ")
                        else:
                            #En caso de que no tenga para pagar paga con lo que le queda.
                            players_in_session[player]["points"] += players_in_session[order[-1]]["points"]
                            printing.print_line_centered(f"The Bank pays {players_in_session[order[-1]]['points']} to {players_in_session[player]['name']}", " ")
                            players_in_session[order[-1]]["points"] = 0
                            can_bank_pay = False
                else:
                    printing.print_line_centered(f"Bank is out of money and can't pay anymore", " ")





def check_bank_status(order):
    #Hacer que cambie la banca a quien tiene que ser la banca y que reordene la lista order
    #No tienen que intercambiar prioridad
    new_order = []

    
    #Aquí se comprueba en caso de que la banca no haya perdido si alguien ha sacado 7.5 y la banca no.

    #Para asegurarme de que sea según el orden de prioridad debería invertir el orden de "order"
    for player in order[::-1]:
        if players_in_session[player]["cards_value"] == 7.5 and players_in_session[order[-1]]["cards_value"] != 7.5:
            players_in_session[order[-1]]["bank"] = False
            players_in_session[player]["bank"] = True

            printing.print_line_centered(f"{players_in_session[player]['name']} is the new bank", " ")
            ganador = player
            #Necesito hacer que el jugador que saca 7.5 se quede al final de la lista y que al resto se les ordene en "order" según la prioridad que tienen.
            #Se recorre la lista con las prioridades y se comprueba que no sea el ganador, se añade en new_order en orden ya que order ya está ordenado
            for player in order:
                if player != ganador:
                    new_order.append(player)
            
            #Por último se añade al ganador como último index de la lista representando la banca
            new_order.append(ganador)

            txt = "New order is: "
            for player in new_order:
                if players_in_session[player]["points"] > 0:
                    if new_order.index(player) != len(new_order) - 1:
                        txt += f"{players_in_session[player]['name']} -> "
                    else:
                        txt += f"{players_in_session[player]['name']}"

            printing.print_line_centered(f" {txt} ", "=")

            return new_order
    
    bank_points = players_in_session[order[-1]]["points"]
    #En caso de que la banca se haya quedado sin puntos pero alguien no haya sacado 7.5 se pasa al anterior en la lista de prioridad
    if bank_points == 0:
        players_in_session[order[-1]]["bank"] = False
        players_in_session[order[-2]]["bank"] = True

        new_order = order[:-1] #Se hace que la lista de new_order tenga todos menos a la banca que acaba de perder y desupués se le añade al principio

        new_order.insert(0, order[-1])
        printing.print_line_centered(f"The bank has been eliminated, {players_in_session[order[-2]]['name']} is the new bank", " ")
        return new_order


    if len(new_order) == 0: #Si ha habido algún cambio en new_order quiere decir que algo ha cambiado en el orden de prioridades
        new_order = order

    return new_order


def check_game_winner(order): #Esta función se usa cuando una partida termina por limite de rondas
    #El ganador es la persona con más puntos de la partida

    #Se asigna como ganador al primero de la lista, después se recorre un bucle y va asignando como ganador a la persona con mayor puntaje del juego
    winner = order[0]

    for player in order[1:]:
        if players_in_session[player]["points"] > players_in_session[winner]["points"]:
            winner = player

    return winner




def rounds_logic(players_in_session, order, start_time):
    global played_cards

    query = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'cardgame';"
    game_id = execute_transaction_in_db(query, one=True)
    
    pgr_list = []
    total_rounds = 0

    for round_number in range(1, max_rounds + 1):
        # Almacenar puntos iniciales de la ronda para guardar en la BBDD luego
        starting_points_dict = {}
        for player_id, data in players_in_session.items():
            starting_points_dict.update({player_id: data["points"]})

        round_results = []
        player_bets = []

        #Que cada jugador haga la apuesta
        for player in order[:-1]: #Se omite la última posición ya que es la banca y ésta no apuesta
            if players_in_session[player]["points"] > 0:
                if players_in_session[player]["human"]:
                    while True:
                        utils.clear_screen()
                        printing.print_round_screen(round_number, players_in_session[player]["name"], showMenu=False)
                        printing.print_line_centered("How much would you like to wager this round? (-1 to see game stats)", " ")

                        option = input()
                        if option != "-1":
                            if option.isdigit():
                                if int(option) < 1:
                                    printing.print_line_centered(f"Invalid amount", " ")
                                    utils.press_to_continue()
                                elif int(option) > players_in_session[player]["points"]:
                                    printing.print_line_centered(f"You can only wager up to {players_in_session[player]['points']}!", " ")
                                    utils.press_to_continue()
                                else:
                                    players_in_session[player]["bet"] = int(option)
                                    printing.print_line_centered(f" Bet successfully made ", "=")
                                    utils.press_to_continue()
                                    break

                            else:
                                printing.print_line_centered(" Please insert a valid amount ", "*")
                                utils.press_to_continue()
                        else:
                            printing.print_main_game_scene(players_in_session, sizes.TOTAL_WIDTH)
                            input()
                else:
                    players_in_session[player]["bet"] = p.cpu_make_bet(players_in_session[player])

        
        #Se muestra la pantalla principal de las rondas antes de que empiece la ronda, para poder ver apuestas, puntos y demás
        utils.clear_screen()
        printing.print_main_game_scene(players_in_session, padding=sizes.TOTAL_WIDTH)
        utils.press_to_continue()

        #Demás lógica de la ronda
        for player in order:
            #Se reparte una carta al jugador antes de nada
            if players_in_session[player]["points"] > 0:
                deal_card(player)
                

            if players_in_session[player]["human"] and players_in_session[player]["points"] > 0: #Si el jugador es humano se hará de esta forma
                turn = True
                is_first = True
                while turn:
                    utils.clear_screen()
                    printing.print_round_screen(round_number, players_in_session[player]["name"])
                    if is_first:
                        print()
                        printing.print_line_centered(f"{players_in_session[player]['name']} has received {players_in_session[player]['cards'][0]} as first card.", " ")
                        is_first = False
                    option = input()
                    try:
                        if int(option) > 0 and int(option) < 6 and option.isdigit():
                            if int(option) == 5:

                                printing.print_line(f" {players_in_session[player]['name']}'s turn is over ", padding=sizes.TOTAL_WIDTH, fill_char='=')
                                input()
                                break

                            if int(option) == 1: #Show Stats
                                utils.clear_screen()
                                printing.show_player_stats(player, players_in_session=players_in_session)
                                input()

                            if int(option) == 2: #View Game Stats
                                printing.print_main_game_scene(players_in_session, sizes.TOTAL_WIDTH)
                                input()
                            
                            if int(option) == 3: #Order Card
                                order_card(player)
                                
                            if int(option) == 4: #Automatic play
                                len_cards = len(players_in_session[player]["cards"])

                                if len_cards == 1:
                                    order_card_human_automatic(player)
                                    utils.clear_screen()
                                    printing.print_round_screen(round_number, players_in_session[player]["name"], showMenu=False)
                                    printing.print_line_centered(" AUTOMATIC PLAY ", "=")
                                    if not players_in_session[player]["bank"]:
                                        printing.print_line_centered(f"{players_in_session[player]['name']} has made a bet of {players_in_session[player]['bet']} points", " ")
                                    txt_cards = ""
                                    for card in players_in_session[player]["cards"]:
                                        txt_cards += card
                                        if players_in_session[player]["cards"].index(card) != len(players_in_session[player]["cards"]) - 1:
                                            txt_cards += ";"

                                    printing.print_line_centered(f"Has ordered the cards: {txt_cards}", " ")
                                    printing.print_line_centered(f"Has ended with {players_in_session[player]['cards_value']} round points.", " ")

                                    utils.press_to_continue()
                                    break

                                else:
                                    printing.print_line_centered(f"You have already ordered a card!", " ")
                                    printing.print_line_centered(f"Automatic play is not available anymore", " ")
                                    utils.press_to_continue()

                        else:
                            printing.print_line(texts.TEXTS["invalid_option"], padding=sizes.TOTAL_WIDTH, fill_char='=')
                            utils.press_to_continue()
                    
                    except ValueError:
                        printing.print_line(texts.TEXTS["value_error"], padding=sizes.TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
                
                #A partir de aquí es cuando termine el turno del jugador (pero aún sigue activa la ronda)
                round_results.append(players_in_session[player]["cards_value"])
                player_bets.append(players_in_session[player]["bet"])
                
            else: #Si el jugador es un bot se hará de esta forma
                if players_in_session[player]["points"] > 0:
                    while p.cpu_demand_card(players_in_session[player], active_deck, round_results, player_bets):
                        deal_card(player)

        #Se muestra como queda la ronda después de cada turno (sin distribuir puntos todavía)
        utils.clear_screen()
        printing.print_main_game_scene(players_in_session=players_in_session, padding=sizes.TOTAL_WIDTH)
        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
        
        #Ver quien gana y repartir puntos
        distribute_points(order=order)

        order = check_bank_status(order=order)

        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))

        #A partir de aquí es cuando termina cada ronda.
        total_rounds += 1

        # Almacenamos los datos de la ronda para guardarlos en la BBDD luego.
        for player_id, data in players_in_session.items():
            pgr_dict = {
                "game_id": game_id,
                "round_number": round_number,
                "player_id": player_id,
                "is_bank": data["bank"],
                "bet_amount": data["bet"],
                "starting_points": starting_points_dict[player_id],
                "cards_value": data["cards_value"],
                "ending_points": data["points"]
            }
            pgr_list.append(pgr_dict)
        
        # Restablecer datos 
        for player in players_in_session:
            players_in_session[player]["cards"] = []
            players_in_session[player]["cards_value"] = 0
            players_in_session[player]["bet"] = 0
        played_cards = []

        #Comprobar si hay más de una persona con puntos, en caso de que no, la persona que queda es la ganadora.
        numPlayersWithPoints = 0
        for player in players_in_session:
            if players_in_session[player]["points"] > 0:
                numPlayersWithPoints += 1

        if numPlayersWithPoints == 1:
            for player in players_in_session:
                if players_in_session[player]["points"] != 0:
                    winner = player
                    break
            break
    
    #A partir de aquí es cuando termina la partida
    end_time = execute_transaction_in_db("SELECT now();", one=True)

    insert_game_into_db(game_id, players_in_session, start_time, total_rounds, end_time, pgr_list)

    winner = check_game_winner(order=order)

    utils.clear_screen()
    printing.print_title(titles.TITLES["game_title"], padding=sizes.TOTAL_WIDTH)
    printing.print_line_centered(" WINNER ", "=")
    printing.print_line_centered(f" {players_in_session[winner]['name']} has won the game with {players_in_session[winner]['points']} points! ")

    input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))

def insert_game_into_db(game_id, players, start_time, total_rounds, end_time, pgr_list):
    """Recoge todos los datos necesarios para las tres tablas relacionadas con partidas
    y ejecuta las tres sentencias INSERT INTO en una sola transacción."""    
    # Tabla cardgame
    cardgame = {
        "players": len(players),
        "start_time": start_time,
        "rounds": total_rounds,
        "end_time": end_time,
        "deck_id": active_deck_id
    }
    cg_query = insert_query(cardgame, "cardgame")

    # Tabla player_game
    pg_list = []
    for player_id, data in players.items():
        pg_dict = {
            "game_id": game_id,
            "player_id": player_id,
            "initial_card_id": data["initialCard"],
            "starting_points": 20,
            "ending_points": data["points"]
        }
        pg_list.append(pg_dict)
    pg_query = insert_query(pg_list, "player_game")
    
    # Tabla player_game_round
    pgr_query = insert_query(pgr_list, "player_game_round")

    # Insertar en las tres tablas en una sola transacción
    execute_transaction_in_db([cg_query, pg_query, pgr_query], DML=True)

def game_logic(playersInSession, start_time):
    order = assign_priority(playersInSession)
    rounds_logic(playersInSession, order, start_time)

def game_main(padding):
    start_time = execute_transaction_in_db("SELECT now();", one=True)
    start_game(padding)
    game_logic(players_in_session, start_time)

