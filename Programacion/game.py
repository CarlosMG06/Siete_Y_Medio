#Primero recoger cartas
#Imprimir titulo (print title)
#Repartir una carta a jugadores para prioridad

import mazos
import utils
import printing
import titles
import texts
import players as p



players6 = {
            "11111111A": 
                {"name": "Michael", "human": True, "bank": False, "initialCard": "", "priority": 1, "type": 40, "bet": 1, "points": 30, "cards": ["O01", "C04"], "roundPoints": 3},
           "222222222A": 
                {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 2, "type": 20, "bet": 5, "points": 7, "cards": [], "roundPoints": 2},
           "333333333A": 
                {"name": "Bot3", "human": False, "bank": True, "initialCard": "", "priority": 4, "type": 60, "bet": 8, "points": 10, "cards": ["P06"], "roundPoints": 5},
            "444444444A": 
                {"name": "John", "human": True, "bank": False, "initialCard": "", "priority": 3, "type": 40, "bet": 2, "points": 12, "cards": ["O02"], "roundPoints": 7},
            "555555555A": 
                {"name": "Ann", "human": True, "bank": False, "initialCard": "", "priority": 5, "type": 40, "bet": 4, "points": 10, "cards": [], "roundPoints": 2},
            "666666666A": 
                {"name": "Jhonny", "human": True, "bank": False, "initialCard": "", "priority": 6, "type": 40, "bet": 8, "points": 22, "cards": ["E03"], "roundPoints": 4},
           }

players2 = {
            "11111111A": 
                {"name": "Michael", "human": True, "bank": False, "initialCard": "", "priority": 1, "type": 40, "bet": 1, "points": 30, "cards": ["O01", "C04"], "roundPoints": 3},
           "222222222A": 
                {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 2, "type": 20, "bet": 5, "points": 7, "cards": [], "roundPoints": 2},
           
           }

players4 = {
            "11111111A": 
                {"name": "Michael", "human": True, "bank": False, "initialCard": "", "priority": 1, "type": 40, "bet": 1, "points": 30, "cards": ["O01", "C04"], "roundPoints": 3},
           "222222222A": 
                {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 2, "type": 20, "bet": 5, "points": 7, "cards": [], "roundPoints": 2},
           "333333333A": 
                {"name": "Bot3", "human": False, "bank": True, "initialCard": "", "priority": 4, "type": 60, "bet": 8, "points": 10, "cards": ["P06"], "roundPoints": 5},
            "444444444A": 
                {"name": "John", "human": True, "bank": False, "initialCard": "", "priority": 3, "type": 40, "bet": 2, "points": 12, "cards": [], "roundPoints": 7},
            }

selectedPlayers = {}

#Estos diccionarios de jugadores son únicamente como ejemplo para programar, después se reemplaza por el diccionario real.

activeDeck = None #Cambia dinamicamente durante la ejecución del juego

def initializePlayers(players):
    
    initializedPlayers = players.copy()
    """
    for player in players:
        initializedPlayers[player["id"]] = {}
        initializedPlayers[player["id"]]["name"] = player["data"]["name"]
        initializedPlayers[player["id"]]["human"] = player["data"]["human"]
        initializedPlayers[player["id"]]["bank"] = player["data"]["bank"]
        initializedPlayers[player["id"]]["initialCard"] = "" 
        initializedPlayers[player["id"]]["priority"] = 0
        if player["data"]["type"] == "Moderated":
            initializedPlayers[player["id"]]["type"] = 40
        elif player["data"]["type"] == "Bold":
            initializedPlayers[player["id"]]["type"] = 50
        else:
            initializedPlayers[player["id"]]["type"] = 30
        initializedPlayers[player["id"]]["bet"] = 0
        initializedPlayers[player["id"]]["points"] = 20
        initializedPlayers[player["id"]]["cards"] = []
        initializedPlayers[player["id"]]["roundPoints"] = 0
    """

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
        players = p.get_players() #El motivo por el que no se ven en el juego los nuevos jugadores creados es porque al mostrar los jugadores en show/remove se usa
                                    #la lista de jugadores en el modulo engine, mientras que aquí estoy usando este.
                                    #Hacer que el dic de playersInSession se haga sin usar el p.get_players ya que es solo para los jugadores de la sesión, no todos.

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
