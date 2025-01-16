#Primero recoger cartas
#Imprimir titulo (print title)
#Repartir una carta a jugadores para prioridad

import mazos
import utils
import printing
import titles
import texts
import players as p
import random
import sizes


selectedPlayers = {}
playedCards = [] #Lista con las cartas jugadas hasta el momento para que no se repitan

activeDeck = None #Cambia dinamicamente durante la ejecución del juego
playersInSession = {} #Donde se guardan los jugadores y los valores dinámicos que ocurren durante la partida

def initializePlayers(players):
    
    initializedPlayers = players.copy()

    for player in initializedPlayers.keys():
        initializedPlayers[player]["initialCard"] = ""
        initializedPlayers[player]["bet"] = 0
        initializedPlayers[player]["points"] = 20
        initializedPlayers[player]["cards"] = []
        initializedPlayers[player]["roundPoints"] = 0
        initializedPlayers[player]["priority"] = 0

    return initializedPlayers

def start_game(padding):
    global activeDeck, playersInSession
    if activeDeck != None:
        
        #Se inicializan los jugadores seleccionados
        playersInSession = initializePlayers(selectedPlayers)
        #Se barajan las cartas
        activeDeck = utils.shuffle_cards(activeDeck)

        #Se muestra la pantalla principal para mostrar los jugadores que hay, etc.
        printing.print_title(titles.TITLES["game_title"], padding=padding)
        printing.print_main_game_scene(playersInSession, padding)
        
        input()
    
    else:
        printing.print_line(texts.TEXTS["invalidDeck"], padding, "=")
        input()
    


def deal_card(player):
    cardList = list(activeDeck.keys())
    card = cardList[random.randint(0, len(cardList) - 1)]
    while card in playedCards:
        card = cardList[random.randint(0, len(cardList) - 1)]

    playedCards.append(card)
    playersInSession[player]["cards"].append(card)
    playersInSession[player]["roundPoints"] += activeDeck[card]["realValue"]

def assign_priority(playersInSession):
    """Se añade la prioridad repartiendo una carta a todo el mundo
    -> Devuelve una lista de diccionarios con el orden de los jugadores"""
    global playedCards
    

    for player in playersInSession.keys():
        #Se reparte una carta a cada jugador
        deal_card(player)
        #Se asigna esa carta como la carta inicial del jugador
        playersInSession[player]["initialCard"] = playersInSession[player]["cards"][0]

    #Para asignar prioridades se compararán uno por uno en un diccionario los valores de los jugadores
    dicValores = {}

    for jugador in playersInSession:
        dicValores[jugador] = {}
        dicValores[jugador]["numValue"] = activeDeck[playersInSession[jugador]["cards"][0]]["value"]
        dicValores[jugador]["priority"] = activeDeck[playersInSession[jugador]["cards"][0]]["priority"]
    
    #hacer una función que ordene el diccionario en una lista o como sea
    ordenado = sort_priorities(dicValores)

    #Se muestra por pantalla lo que ha recibido cada uno y quién será la banca
    utils.clear_screen()
    printing.print_title(titles.TITLES["game_title"], padding=sizes.TOTAL_WIDTH)
    printing.print_line_centered(" Priority assignement ", "=")
    print()
    for jugador in playersInSession:
        printing.print_line_centered(f"{playersInSession[jugador]['name']} has received the card: {activeDeck[playersInSession[jugador]['cards'][0]]['literal']}", " ")

    #Según el orden hay que asignar una banca y el orden de jugada.
    orderTxt = "Order will now be: "
    for jugador in ordenado: #ordenado está de menor prioridad a mayor, la banca es el último index
        
        playersInSession[jugador]["priority"] = ordenado.index(jugador) + 1

        if ordenado.index(jugador) + 1 == len(ordenado):
            orderTxt += playersInSession[jugador]["name"]
            playersInSession[jugador]["bank"] = True
            print()
            printing.print_line_centered(f" {playersInSession[jugador]['name']} is now the bank ", "=")
            print()
            printing.print_line_centered(orderTxt, " ")
        else:
            orderTxt += playersInSession[jugador]["name"] + " -> "
            playersInSession[jugador]["bank"] = False
    
    #Por último se limpia la lista de cartas jugadas y se eliminan las cartas  y los puntos de los jugadores
    for jugador in playersInSession:
        playersInSession[jugador]["cards"] = []
        playersInSession[jugador]["roundPoints"] = 0
        
    playedCards = []

    input()

    return ordenado


    
def sort_priorities(dic):
    """Dic con los valores númericos y las prioridades de la carta de los jugadores"""
    result = []

    dicList = list(dic)

    result.append(dicList[0])
    for jugador in dicList:
        #Ordenar las prioridades de menor a mayor, es decir si sacan 2, 8 y 5, la prioridad es 1, 3, 2   
        if dicList.index(jugador) != 0:
            if activeDeck[playersInSession[result[-1]]["cards"][0]]["value"] == activeDeck[playersInSession[jugador]["cards"][0]]["value"]: #Si el valor es igual se comprueba la prioridad
                if activeDeck[playersInSession[result[-1]]["cards"][0]]["priority"] < activeDeck[playersInSession[jugador]["cards"][0]]["priority"]:
                    result.append(jugador)
                else:
                    result.insert(-1, jugador) 
                
            else:

                if activeDeck[playersInSession[result[-1]]["cards"][0]]["value"] < activeDeck[playersInSession[jugador]["cards"][0]]["value"]:
                    result.append(jugador)
                else:
                    offset = -1

                    while activeDeck[playersInSession[result[offset]]["cards"][0]]["value"] > activeDeck[playersInSession[jugador]["cards"][0]]["value"]:
                        if len(result) != abs(offset):
                            if (activeDeck[playersInSession[result[offset - 1]]["cards"][0]]["value"] > activeDeck[playersInSession[jugador]["cards"][0]]["value"]
                                or (activeDeck[playersInSession[result[offset - 1]]["cards"][0]]["value"] == activeDeck[playersInSession[jugador]["cards"][0]]["value"]
                                    and activeDeck[playersInSession[result[offset - 1]]["cards"][0]]["priority"] > activeDeck[playersInSession[jugador]["cards"][0]]["priority"])):
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

def set_bet(player):
    if playersInSession[player]["human"]: #Si el jugador es humano se hace de esta forma
        if len(playersInSession[player]["cards"]) == 0: #Si ha pedido cartas no puede realizar la apuesta
            printing.print_line_centered("How much do you want to bet? (Exit to cancel)", " ")
            while True:
                apuesta = input()
                if apuesta.isdigit():
                    if int(apuesta) > 0:
                        if int(apuesta) <= playersInSession[player]["points"]:
                            playersInSession[player]["bet"] = int(apuesta)
                            printing.print_line_centered("Bet has been made succesfully", " ")
                            input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                            break
                        else:
                            printing.print_line_centered(f"You can only bet up to {playersInSession[player]['points']}!", " ")
                    else:
                        printing.print_line_centered("Invalid amount", " ")
                else:
                    if apuesta.lower() == "exit":
                        break
                    printing.print_line_centered("Please insert a number", " ")
        else:
            printing.print_line_centered("You have already ordered a card, you cannot make a bet anymore.", fill_char=" ")
            input()

    else: #Si el jugador no es humano se hace de esta forma
        printing.print_line_centered("Not a human.")
        input()


def order_card(player):
    if playersInSession[player]["bet"] > 0:
        if playersInSession[player]["roundPoints"] < 7.5:
            sum_valid = 0
            total_cards = 0
            for card in activeDeck.values():
                if card not in playedCards:
                    if playersInSession[player]["roundPoints"] + card["realValue"] <= 7.5:
                        sum_valid += 1
                    total_cards += 1
            risk = (sum_valid / total_cards) * 100 #Esto más que riesgo es la probabilidad de no pasarse
            printing.print_line_centered(f"The risk to exceed 7.5 is {100 - risk}%, are you sure? (y/n)", " ")
            if playersInSession[player]["human"]:
                sure = str(input())
            else:
                sure = "y"
            if sure.lower() == "y":
                deal_card(player)
                if playersInSession[player]["human"]:
                    printing.print_line_centered("New card ordered!", " ")
                    printing.print_line_centered(f"The new card is: {activeDeck[playersInSession[player]['cards'][-1]]['literal']}", " ")
                    printing.print_line_centered(f"Now you have {playersInSession[player]['roundPoints']}", " ")
                    input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))                            
        else:
            if playersInSession[player]["roundPoints"] == 7.5:
                printing.print_line_centered("You already have 7.5 points!", " ")
                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
            else:
                printing.print_line_centered("You have exceeded 7.5 points!", " ")
                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
    else:
        printing.print_line_centered("Make a bet before ordering a card", " ")
        input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                    
def order_card_human_automatic(player):
    while True:
        if playersInSession[player]["roundPoints"] < 7.5:
            sum_valid = 0
            total_cards = 0
            for card in activeDeck.values():
                if card not in playedCards:
                    if playersInSession[player]["roundPoints"] + card["realValue"] <= 7.5:
                        sum_valid += 1
                    total_cards += 1
            risk = (sum_valid / total_cards) * 100 #Esto más que riesgo es la probabilidad de no pasarse
            acceptable_risk = 0

            if playersInSession[player]["type"] == "Moderated":
                acceptable_risk = 50
            if playersInSession[player]["type"] == "Cautious":
                acceptable_risk = 30
            if playersInSession[player]["type"] == "Bold":
                acceptable_risk = 80

            if (100 - risk) < acceptable_risk:
                deal_card(player)
            else:
                break             
        else:
            break

def check_losers_winners(orden):
    """Devuelve 

    losers (list) -> Es una lista de str con los ids de los jugadores

    winners (list) -> Es una lista de dic con los ids de los jugadores como clave y los beneficios al ganar como entrada
    
    En la lista winners nunca estará la banca, la forma de saber si la banca es el único ganador es comprobando que no esté en la lista losers
    """

    losers = []
    winners = []
    if playersInSession[orden[-1]]["roundPoints"] == 7.5: #Gana la banca contra todos
        losers = orden[:-1]
        return losers
    if playersInSession[orden[-1]]["roundPoints"] > 7.5: #Pierde la banca contra todos
        losers.append(orden[-1])
        return losers

    for player in orden[:-1]: #Comprobar contra quién gana y quién pierde
        if playersInSession[player]["roundPoints"] <= playersInSession[orden[-1]]["roundPoints"] and playersInSession[player]["roundPoints"] < 7.5: #Si tiene menos puntos o los mismos que la banca
            losers.append(player)

        elif playersInSession[player]["roundPoints"] > 7.5: #Si se pasa de 7.5 puntos
            losers.append(player)

        else:
            dic = {}
            dic[player] = {}
            if playersInSession[player]["bet"] == 7.5:
                dic[player]["profit"] = playersInSession[player]["bet"] * 2
            else:
                dic[player]["profit"] = playersInSession[player]["bet"]

            winners.append(dic)
    
    #Las listas ya están ordenadas de menor a mayor prioridad
    return losers


def distribute_points(orden):
    losers = check_losers_winners(orden)
    for loser in losers:
        print(playersInSession[loser]["name"])
    input("losers")

    #utils.clear_screen()
    printing.print_title(title=titles.TITLES["game_title"], padding=sizes.TOTAL_WIDTH)

    printing.print_line_centered(f" ROUND RESULTS ", "=")

    if len(losers) == 1:
        if playersInSession[losers[0]]["bank"]: #Si el único perdedor es la banca se tendrá que repartir por prioridades
            canBankPay = True
            for player in orden[:-1]:
                if canBankPay:
                    if playersInSession[player]["roundPoints"] != 7.5:
                        #Si la apuesta es mayor que el dinero que tiene la banca (no tiene dinero suficiente para pagar)
                        if playersInSession[player]["bet"] > playersInSession[orden[-1]]["points"] or playersInSession[player]["bet"] - playersInSession[orden[-1]]["points"] == 0:                    
                            playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                            printing.print_line_centered(f"Bank has payed {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                            playersInSession[orden[-1]]["points"] = 0
                            canBankPay = False
                            

                        else:
                            playersInSession[player]["points"] += playersInSession[player]["bet"]
                            playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"]
                            printing.print_line_centered(f"Bank has payed {playersInSession[player]['bet']} to {playersInSession[player]['name']}", " ")
                    else:
                        #Si la apuesta es mayor que el dinero que tiene la banca (no tiene dinero suficiente para pagar)
                        if playersInSession[player]["bet"] * 2 > playersInSession[orden[-1]]["points"] or (playersInSession[player]["bet"] * 2) - playersInSession[orden[-1]]["points"] == 0:                    
                            playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                            printing.print_line_centered(f"Bank has payed {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                            playersInSession[orden[-1]]["points"] = 0
                            canBankPay = False
                            

                        else:
                            playersInSession[player]["points"] += playersInSession[player]["bet"] * 2
                            playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"] * 2
                            printing.print_line_centered(f"Bank has payed {playersInSession[player]['bet'] * 2} to {playersInSession[player]['name']}", " ")
                else:
                    printing.print_line_centered(f"Bank is out of money and can't pay anymore.", " ")



        else: #Si el único perdedor no es la banca
            canBankPay = True
            for player in orden:
                if playersInSession[player] in losers: #Este perdedor no es la banca
                    playersInSession[orden[-1]]["points"] += playersInSession[player]["bet"]
                    playersInSession[player]["points"] -= playersInSession[player]["bet"]
                    printing.print_line_centered(f"{playersInSession[player]['name']} pays {playersInSession[player]['bet']} to the bank")
                
                else: #Aquí se tratan los ganadores (en el caso de que solo haya un perdedor)
                    if playersInSession[player]["bank"] == False: #En caso de que no sea la banca, ya que no hace falta hacer nada con la banca si es ganadora en este momento
                        #La banca tiene que pagar a los ganadores
                        if canBankPay:
                            if playersInSession[player]["roundPoints"] != 7.5:
                                #En caso de que no tenga para pagar    
                                if playersInSession[orden[-1]]["points"] < playersInSession[player]["bet"] or playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] == 0:
                                    playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                                    printing.print_line_centered(f"Bank has payed {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                                    playersInSession[orden[-1]]["points"] = 0
                                    canBankPay = False
                                    
                                else:
                                    playersInSession[player]["points"] += playersInSession[player]["bet"]
                                    playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"]
                                    printing.print_line_centered(f"Bank has payed {playersInSession[player]['bet']} to {playersInSession[player]['name']}", " ")

                            else:
                                if playersInSession[orden[-1]]["points"] < playersInSession[player]["bet"] * 2 or playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] * 2 == 0:
                                    playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                                    printing.print_line_centered(f"Bank has payed {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                                    playersInSession[orden[-1]]["points"] = 0
                                    canBankPay = False
                                    
                                else:
                                    playersInSession[player]["points"] += playersInSession[player]["bet"] * 2
                                    playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"] * 2
                                    printing.print_line_centered(f"Bank has payed {playersInSession[player]['bet'] * 2} to {playersInSession[player]['name']}", " ")

    else:
        #Comprobar si en los más de un jugadores que hay perdedores está la banca, si no, eso quiere decir que la banca ha ganado a todos

        #Primero se suma todo lo de los perdedores que no sean la banca a la banca
        for player in losers:
            if playersInSession[player]["bank"] == False:
                printing.print_line_centered(f"{playersInSession[player]['name']} pays {playersInSession[player]['bet']} to the bank", " ")
                playersInSession[orden[-1]]["points"] += playersInSession[player]["bet"] #Se suma a la banca los puntos
                playersInSession[player]["points"] -= playersInSession[player]["bet"] #Se le resta al perdedor los puntos


        #En este punto los jugadores perdedores ya han pagado a la banca, por lo que se les omite
        canBankPay = True
        for player in orden[:-1]:
            if player not in losers: #Si el jugador es ganador (y no la banca)
                if canBankPay:
                    if playersInSession[player]["roundPoints"] == 7.5: #Si el jugador tiene 7.5 roundPoints (gana el doble de la bet)
                        #En caso de que cuando pague tenga más o igual a 0 paga
                        if playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] * 2 == 0 or playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] * 2 > 0:
                            playersInSession[player]["points"] += playersInSession[player]["bet"] * 2
                            playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"] * 2
                            printing.print_line_centered(f"The Bank pays {playersInSession[player]['bet'] * 2} to {playersInSession[player]['name']}", " ")
                        else:
                            #En caso de que no tenga para pagar paga con lo que le queda.
                            playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                            printing.print_line_centered(f"The Bank pays {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                            playersInSession[orden[-1]]["points"] = 0
                            canBankPay = False
                            
                        
                    else:
                        #En caso de que cuando pague tenga más o igual 0 paga
                        if playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] == 0 or playersInSession[orden[-1]]["points"] - playersInSession[player]["bet"] > 0:
                            playersInSession[player]["points"] += playersInSession[player]["bet"]
                            playersInSession[orden[-1]]["points"] -= playersInSession[player]["bet"]
                            printing.print_line_centered(f"The Bank pays {playersInSession[player]['bet']} to {playersInSession[player]['name']}", " ")
                        else:
                            #En caso de que no tenga para pagar paga con lo que le queda.
                            playersInSession[player]["points"] += playersInSession[orden[-1]]["points"]
                            printing.print_line_centered(f"The Bank pays {playersInSession[orden[-1]]['points']} to {playersInSession[player]['name']}", " ")
                            playersInSession[orden[-1]]["points"] = 0
                            canBankPay = False
                else:
                    printing.print_line_centered(f"Bank is out of money and can't pay anymore", " ")

        #PROBLEMA: A VECES LA BANCA NO REPARTE LOS PUNTOS A ALGUIEN CONTRA QUIEN PIERDE (QUIZAS SOLO OCURRE SI OTROS PIERDEN CONTRA ELLA, O SI EL GANADOR SACA 7.5)




        


def rounds_logic(playersInSession, maxRounds, orden):
    global playedCards
    
    for round in range(0, maxRounds):
        resultadosRonda = []
        apuestasJugadores = []

        #Que cada jugador haga la apuesta
        for player in orden:
            if playersInSession[player]["human"]:
                while True:
                    utils.clear_screen()
                    printing.print_round_screen(round, playersInSession[player]["name"], showMenu=False)
                    printing.print_line_centered("How much would you like to wager this round? (-1 to see game stats)", " ")

                    eleccion = input()
                    if eleccion != "-1":
                        if eleccion.isdigit():
                            if int(eleccion) < 1:
                                printing.print_line_centered(f"Invalid amount", " ")
                                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                            elif int(eleccion) > playersInSession[player]["points"]:
                                printing.print_line_centered(f"You can only wager up to {playersInSession[player]['points']}!", " ")
                                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                            else:
                                playersInSession[player]["bet"] = int(eleccion)
                                printing.print_line_centered(f" Bet succesfully made ", "=")
                                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                                break

                        else:
                            printing.print_line_centered(" Please insert a valid amount ", "*")
                            input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                    else:
                        printing.print_main_game_scene(playersInSession, sizes.TOTAL_WIDTH)
                        input()
            else:
                playersInSession[player]["bet"] = p.cpu_make_bet(playersInSession[player])

        #Se muestra la pantalla principal de las rondas antes de que empiece la ronda, para poder ver apuestas, puntos y demás
        utils.clear_screen()
        printing.print_main_game_scene(playersInSession, padding=sizes.TOTAL_WIDTH)
        input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))

        #Demás lógica de la ronda
        for player in orden:
            if playersInSession[player]["human"]: #Si el jugador es humano se hará de esta forma
                turno = True
                while turno:
                    utils.clear_screen()
                    printing.print_round_screen(round, playersInSession[player]["name"])
                    eleccion = input()
                    if int(eleccion) > 0 and int(eleccion) < 7 and eleccion.isdigit():
                        if int(eleccion) == 6:

                            printing.print_line(f" {playersInSession[player]['name']}'s turn is over ", padding=sizes.TOTAL_WIDTH, fill_char='=')
                            input()
                            break

                        if int(eleccion) == 1: #Show Stats
                            utils.clear_screen()
                            printing.show_player_stats(player, playersInSession=playersInSession)
                            input()

                        if int(eleccion) == 2: #View Game Stats
                            printing.print_main_game_scene(playersInSession, sizes.TOTAL_WIDTH)
                            input()
                        
                        if int(eleccion) == 3: #Set Bet
                            set_bet(player) #Esto está mal, no se debería poder cambiar la apuesta, quitarlo después

                        if int(eleccion) == 4: #Order Card
                            order_card(player)
                            
                        if int(eleccion) == 5: #Automatic play
                            lenCards = len(playersInSession[player]["cards"])

                            if lenCards == 0:
                                #playersInSession[player]["bet"] = p.cpu_make_bet(player=playersInSession[player])
                                order_card_human_automatic(player)
                                utils.clear_screen()
                                printing.print_round_screen(round, playersInSession[player]["name"], showMenu=False)
                                printing.print_line_centered(" AUTOMATIC PLAY ", "=")
                                printing.print_line_centered(f"{playersInSession[player]['name']} has made a bet of {playersInSession[player]['bet']} points", " ")
                                txtCards = ""
                                for card in playersInSession[player]["cards"]:
                                    txtCards += card
                                    if playersInSession[player]["cards"].index(card) != len(playersInSession[player]["cards"]) - 1:
                                        txtCards += ";"

                                printing.print_line_centered(f"Has ordered the cards: {txtCards}", " ")
                                printing.print_line_centered(f"Has ended with {playersInSession[player]['roundPoints']} round points.", " ")

                                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                                break

                            else:
                                printing.print_line_centered(f"You have already ordered a card!", " ")
                                printing.print_line_centered(f"Automatic play is not available anymore", " ")
                                input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))

                    else:
                        printing.print_line(texts.TEXTS["invalid_option"], padding=sizes.TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))
                
                #A partir de aquí es cuando termine el turno del jugador (pero aún sigue activa la ronda)
                resultadosRonda.append(playersInSession[player]["roundPoints"])
                apuestasJugadores.append(playersInSession[player]["bet"])
                
            else: #Si el jugador es un bot se hará de esta forma
                if p.cpu_demand_card(playersInSession[player], activeDeck, resultadosRonda, apuestasJugadores):

                    while p.cpu_demand_card(playersInSession[player], activeDeck, resultadosRonda, apuestasJugadores):
                        deal_card(player)

                else: #Si no puede demandar una carta, la apuesta será de uno
                    playersInSession[player]["bet"] = 1

        #Se muestra como queda la ronda después de cada turno (sin distribuir puntos todavía)
        utils.clear_screen()
        printing.print_main_game_scene(playersInSession=playersInSession, padding=sizes.TOTAL_WIDTH)
        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
        
        #Ver quien gana y repartir puntos
        distribute_points(orden=orden)
        input("bbbbbb")
        

        #A partir de aquí es cuando termina cada ronda.
        for player in playersInSession:
            playersInSession[player]["cards"] = []
            playersInSession[player]["roundPoints"] = 0
            playersInSession[player]["bet"] = 0
        playedCards = []

        #Mostrar los resultados de la ronda






def game_logic(playersInSession, maxRounds):
    orden = assign_priority(playersInSession)
    rounds_logic(playersInSession, maxRounds, orden)

def game_main(padding, maxRounds):
    start_game(padding)
    game_logic(playersInSession, maxRounds)


#PROBLEMAS

#AHORA MISMO NO HAY FORMA DE DESCALIFICAR A ALGUIEN DEL JUEGO CUANDO SE QUEDA SIN PUNTOS.
#FALTA HACER QUE LA BANCA NO APUESTE
#QUITAR LO DE SET BET EN EL MENÚ
#HACER QUE EL ORDEN DE PRIORIDADES SE HAGA DE FORMA CORRECTA (EN CASO DE QUE NO LO SEA YA, NO SÉ SI UNA PRIORIDAD MÁS ALTA ES MEJOR QUE UNA MÁS BAJA A LA HORA DE REPARTIR PUNTOS)