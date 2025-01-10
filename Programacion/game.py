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
#Estos diccionarios de jugadores son únicamente como ejemplo para programar, después se reemplaza por el diccionario real.

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
    print(playersInSession[player]["cards"])
    input()

def assign_priority(playersInSession):
    """Se añade la prioridad repartiendo una carta a todo el mundo"""

    for player in playersInSession.keys():
        #Se reparte una carta a cada jugador
        deal_card(player)
    
    values = {} #Aquí guardo los valores de las cartas junto con el id y la prioridad del palo
    for player in playersInSession.keys():
        values[player] = {}
        values[player]["value"] = activeDeck[playersInSession[player]["cards"][0]]["value"]
        values[player]["priority"] = activeDeck[playersInSession[player]["cards"][0]]["priority"]

    #Hay que ordenar los valores según los valores de las cartas y las prioridades si es necesario.
    print("diccionario de valores:")
    print(values)
    print()

    valueList = []
    for player in values.keys():
        valueList.append(values[player]["value"])

    print("Lista de los valores sin más:")
    print(valueList)

    valueList = utils.doBurbuja(valueList)
    print("Lista de valores ordenados")
    print(valueList)

        #Con los valores de las cartas se ordena la prioridad
    orden = [] #Lista que se crea con los ordenes de prioridad, tiene los ids de los jugadores, la banca será el del index mayor, y el orden de menor a mayor.
    for value in valueList:
        for player in values.keys():
            if value == values[player]["value"]:
                orden.append(player)

    print("Orden unicamente segun valor númerico:")
    print(orden)

        #Aquí hay que hacer que en caso de haber repetidos, se juzgue según el palo
    
    for value in valueList:
        if valueList.index(value) != len(valueList) - 1:
            if value == valueList[valueList.index(value) + 1]: #En caso de que sea igual al número que tiene a la derecha (es repetido)
                jugadoresConValoresRepetidos = []
                for player in orden:
                    if activeDeck[playersInSession[player]["cards"][0]]["value"] == value:
                        jugadoresConValoresRepetidos.append(player)
                
                #Una vez tenemos los jugadores con valores repetidos, se comprueban los palos de las cartas
                prioridadPalos = []
                for jugador in jugadoresConValoresRepetidos:
                    playersInSession[jugador]["priority"] #mirar la prioridad de la carta

    input()

    #Según el orden hay que asignar una banca y el orden de jugada.

    #Por último se limpia la lista de cartas jugadas y se eliminan las cartas del inventario de los jugadores
    playedCards = []
    


def game_logic(playersInSession):
    assign_priority(playersInSession)

def game_main(padding):
    start_game(padding)
    game_logic(playersInSession)
    #deal_card(playersInSession["33337777C"])
