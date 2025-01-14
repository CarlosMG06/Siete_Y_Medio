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

        aa = True
        while aa:
            #Printeando la pantalla con los jugadores y puntos.
            printing.print_main_game_scene(playersInSession, padding)
            
            input()
            break
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
    """Se añade la prioridad repartiendo una carta a todo el mundo"""
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
                            playersInSession[player]["bet"] = float(apuesta)
                            printing.print_line_centered("Bet has been made succesfully", " ")
                            input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
                            break
                        else:
                            printing.print_line_centered(f"You can only bet up to {playersInSession[player]["points"]}!", " ")
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
            sure = str(input())
            if sure.lower() == "y":
                deal_card(player)
                printing.print_line_centered("New card ordered!", " ")
                printing.print_line_centered(f"The new card is: {activeDeck[playersInSession[player]["cards"][-1]]["literal"]}", " ")
                printing.print_line_centered(f"Now you have {playersInSession[player]["roundPoints"]}", " ")
                input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))                            
        else:
            if playersInSession[player]["roundPoints"] == 7.5:
                printing.print_line_centered("You already have 7.5 points!", " ")
                input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
            else:
                printing.print_line_centered("You have exceeded 7.5 points!", " ")
                input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
    else:
        printing.print_line_centered("Make a bet before ordering a card", " ")
        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
                    
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

def rounds_logic(playersInSession, maxRounds):
    global playedCards
    for round in range(0, maxRounds):
        for player in playersInSession:
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
                            set_bet(player)

                        if int(eleccion) == 4: #Order Card
                            order_card(player)
                            
                        if int(eleccion) == 5: #Automatic play
                            playersInSession[player]["bet"] = p.cpu_make_bet(player=playersInSession[player])
                            order_card_human_automatic(player)
                            utils.clear_screen()
                            printing.print_round_screen(round, playersInSession[player]["name"], showMenu=False)
                            printing.print_line_centered(" AUTOMATIC PLAY ", "=")
                            printing.print_line_centered(f"{playersInSession[player]["name"]} has made a bet of {playersInSession[player]["bet"]} points", " ")
                            txtCards = ""
                            for card in playersInSession[player]["cards"]:
                                txtCards += card
                                if playersInSession[player]["cards"].index(card) != len(playersInSession[player]["cards"]) - 1:
                                    txtCards += ";"

                            printing.print_line_centered(f"Has ordered the cards: {txtCards}", " ")
                            printing.print_line_centered(f"Has ended with {playersInSession[player]["roundPoints"]} round points.", " ")

                            input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
                            break



                    else:
                        printing.print_line(texts.TEXTS["invalid_option"], padding=sizes.TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(sizes.TOTAL_WIDTH))
            

            else: #Si el jugador es un bot se hará de esta forma
                pass

        #A partir de aquí es cuando termina cada ronda.
        for player in playersInSession:
            playersInSession[player]["cards"] = []
            playersInSession[player]["roundPoints"] = 0
        playedCards = []






def game_logic(playersInSession, maxRounds):
    assign_priority(playersInSession)
    rounds_logic(playersInSession, maxRounds)

def game_main(padding, maxRounds):
    start_game(padding)
    game_logic(playersInSession, maxRounds)
