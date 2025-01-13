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

def assign_priority(playersInSession):
    """Se añade la prioridad repartiendo una carta a todo el mundo"""
    global playedCards
    

    for player in playersInSession.keys():
        #Se reparte una carta a cada jugador
        deal_card(player)

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
    
    #Por último se limpia la lista de cartas jugadas y se eliminan las cartas del inventario de los jugadores
    for jugador in playersInSession:
        playersInSession[jugador]["cards"] = []
        
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


def game_logic(playersInSession):
    assign_priority(playersInSession)

def game_main(padding):
    start_game(padding)
    game_logic(playersInSession)
