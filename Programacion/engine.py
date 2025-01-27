import players as pl
import printing as p
import rankings
import reports
import utils
import settings
import titles
import texts
import game
from menu import *
from players import players_option
from sizes import *

MIN_PLAYERS = 2
MAX_PLAYERS = 6

def start_engine():
    exit = False
    players = pl.get_players_from_db()

    while not exit:
        # Limpiamos la pantalla e imprimimos el título principal
        utils.clear_screen()
        p.print_title(titles.TITLES["principal"], padding=TOTAL_WIDTH)
        start_menu(padding=LEFT_SPACE_OPTIONS)

        # Tratamos la recogida de la opción:
        #   1. Debemos tratar el caso en que no nos introduzcan un número
        #       Imprimimos mensaje de error y volvemos al inicio del bucle
        #   2. Debemos tratar el caso que nos indique una opción con fuera del rango [1-6]
        #       Imprimimos mensaje de error y volvemos al inicio del bucle
        #   3. Si es correcto, deberemos ir a la opción correspondiente
        try:
            option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
            if option < MIN_OPTION or option > MAX_OPTION_2:
                print()
                p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                utils.press_to_continue()
                continue

            if option == MIN_OPTION:
                players = players_option(players)
            elif option == 2:
                settings.settings_option(players)
            elif option == 3:
                # Controlamos la opción de entrada al juego:
                #   1. Revisamos que hayan de 2 a 6 jugadores seleccionados
                #   2. Revisamos que se haya seleccionado un mazo de cartas
                #   3. Vamos al juego
                #   En el caso que 1 y 2 falle, mostramos error correspondiente en el orden de 1 y 2, pero solo 1 error
                if len(game.selected_players) < MIN_PLAYERS or len(game.selected_players) > MAX_PLAYERS:
                    print()
                    p.print_line(texts.TEXTS["error_init_play_players"], padding=TOTAL_WIDTH, fill_char='=')
                    utils.press_to_continue()
                elif game.active_deck == None:
                    print()
                    p.print_line(texts.TEXTS["error_init_play_deck"], padding=TOTAL_WIDTH, fill_char='=')
                    utils.press_to_continue()
                else:
                    game.game_main(padding=TOTAL_WIDTH)
            elif option == 4:
                rankings.rankings_option()
            elif option == 5:
                reports.reports_option()
            elif option == MAX_OPTION_2:
                exit = True
                print()
                p.print_line(texts.TEXTS["exit"], padding=TOTAL_WIDTH, fill_char='-')
        except ValueError:
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()