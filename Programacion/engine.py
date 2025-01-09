import utils
import printing as p
from menu import *
import settings
import titles
import texts
import players as pl
from sizes import *

def start_engine():
    exit = False

    players = pl.get_players()
    cards_to_use = ""

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
                exit_submenu = False

                while not exit_submenu:
                    utils.clear_screen()
                    p.print_title(titles.TITLES["settings"], padding=TOTAL_WIDTH)
                    settings_submenu(padding=LEFT_SPACE_OPTIONS)
                    try:
                        option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
                        if option < MIN_OPTION or option > MAX_OPTION_1:
                            print()
                            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                            continue

                        elif option == 1:
                            pass

                        elif option == 2:
                            settings.set_cards_deck()

                        elif option == 3:
                            settings.set_max_rounds()

                        elif option == MAX_OPTION_1:
                            exit_submenu = True
                    except ValueError:
                        print()
                        p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
                        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            elif option == 3:
                pass
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