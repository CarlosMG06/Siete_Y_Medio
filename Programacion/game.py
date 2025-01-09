#Primero recoger cartas
#Imprimir titulo (print title)
#Repartir una carta a jugadores para prioridad

import mazos
import utils
import printing
import titles
import texts

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

activeDeck = None

def start_game(padding):
    if activeDeck != None:
        aa = True
        while aa:
            #Printeando la pantalla con los jugadores y puntos.
            utils.clear_screen()
            printing.print_title(titles.TITLES["game_title"], padding=padding)
            printing.print_players(players6, padding)
            print("")
            printing.print_line("Enter to continue", padding, " ")

            #Para salir por ahora es poniendo "quit" ya que aún no tiene funcionalidad.
            if input() == "quit":
                aa = False
    else:
        printing.print_line(texts.TEXTS["invalidDeck"], padding, "=")
        input()
