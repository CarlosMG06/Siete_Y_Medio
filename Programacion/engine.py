import settings
import utils
import printing as p
from menu import *
import titles
import texts
import players as pl
from sizes import *
import game
import mazos

# Constantes necesarias para la impresión del título
TOTAL_WIDTH = 128               # Espacio total de la línea, desde el inicio de la línea
LEFT_SPACE_OPTIONS = 51         # Espacio necesario para dejar espacio al inicio de la línea
LEFT_SPACE_OPTIONS_REPORTS = 16 # Espacio necesario para dejar espacio al inicio de la línea para el submenú de reportes
MIN_OPTION = 1                  # Mínima opción a comprobar
# Diferents opciones máximas a comprobar
MAX_OPTION_1 = 4
MAX_OPTION_2 = 6
MAX_OPTION_3 = 11

def start_engine():
    exit = False

    players = pl.get_players()
    cards_to_use = ""
    max_rounds = 5

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
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                continue

            if option == MIN_OPTION:
                exit_submenu = False

                while not exit_submenu:
                    utils.clear_screen()
                    p.print_title(titles.TITLES["players"], padding=TOTAL_WIDTH)
                    players_submenu(padding=LEFT_SPACE_OPTIONS)
                    try:
                        option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
                        if option < MIN_OPTION or option > MAX_OPTION_1:
                            print()
                            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                            continue

                        if option == MAX_OPTION_1:
                            exit_submenu = True
                        elif option == 1:
                            players = pl.create_human_player(players)
                        elif option == 2:
                            players = pl.create_bot_player(players)
                        elif option == 3:
                            pl.show_players(players)
                    except ValueError:
                        print()
                        p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            elif option == 2:
                settings.settings_option(players)
            elif option == 3:
                game.start_game(padding=TOTAL_WIDTH)
            elif option == 4:
                exit_submenu = False

                while not exit_submenu:
                    utils.clear_screen()
                    p.print_title(titles.TITLES["rankings"], padding=TOTAL_WIDTH)
                    ranking_submenu(padding=LEFT_SPACE_OPTIONS)
                    try:
                        option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
                        if option < MIN_OPTION or option > MAX_OPTION_1:
                            print()
                            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                            continue

                        if option == MAX_OPTION_1:
                            exit_submenu = True
                        elif option == 1:
                            pass
                        elif option == 2:
                            pass
                        elif option == 3:
                            pass
                    except ValueError:
                        print()
                        p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            elif option == 5:
                exit_submenu = False

                while not exit_submenu:
                    utils.clear_screen()
                    p.print_title(titles.TITLES["reports"], padding=TOTAL_WIDTH)
                    reports_submenu(padding=LEFT_SPACE_OPTIONS_REPORTS)
                    try:
                        option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS_REPORTS) + texts.TEXTS["option"] + ": "))
                        if option < MIN_OPTION or option > MAX_OPTION_3:
                            print()
                            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                            continue

                        if option == MAX_OPTION_3:
                            exit_submenu = True
                        elif option == 1:
                            pass
                        elif option == 2:
                            pass
                        elif option == 3:
                            pass
                        elif option == 4:
                            pass
                        elif option == 5:
                            pass
                        elif option == 6:
                            pass
                        elif option == 7:
                            pass
                        elif option == 8:
                            pass
                        elif option == 9:
                            pass
                        elif option == 10:
                            pass
                    except ValueError:
                        print()
                        p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            elif option == MAX_OPTION_2:
                exit = True
                print()
                p.print_line(texts.TEXTS["exit"], padding=TOTAL_WIDTH, fill_char='-')
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))