#Primero recoger cartas
#Imprimir titulo (print title)
#Repartir una carta a jugadores para prioridad

import mazos
import utils
import printing
import titles
import texts
import players as p


selectedPlayers = {}

#Estos diccionarios de jugadores son únicamente como ejemplo para programar, después se reemplaza por el diccionario real.

activeDeck = None #Cambia dinamicamente durante la ejecución del juego

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
    global activeDeck
    if activeDeck != None:
        
        #Se inicializan los jugadores seleccionados
        playersInSession = initializePlayers(selectedPlayers)
        #Se barajan las cartas
        activeDeck = utils.shuffle_cards(activeDeck)
        
        aa = True
        while aa:
            #Printeando la pantalla con los jugadores y puntos.
            utils.clear_screen()
            printing.print_title(titles.TITLES["game_title"], padding=padding)
            printing.print_players(playersInSession, padding)
            print("")
            printing.print_line("Enter to continue", padding, " ")

            #Para salir por ahora es poniendo "quit" ya que aún no tiene funcionalidad.
            if input() == "quit":
                aa = False
    else:
        printing.print_line(texts.TEXTS["invalidDeck"], padding, "=")
        input()
