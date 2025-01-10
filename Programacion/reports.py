import printing as p
import players as pl
import texts
import titles
import utils
from sizes import *
from menu import *

REPORT_LIMIT = 15

def reports_option():
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
                report_1()
            elif option == 2:
                report_2()
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

def report_1():
    pass

def report_2():
    page = 1
    # Recoger el count de todos los elementos que puedan recogerse de la base de datos
    total_pages = 10
    center_padding = (TOTAL_WIDTH - RP_2_WIDTH) // 2
    exit = False

    while not exit:
        # Limpiamos pantalla y mostramos título principal
        utils.clear_screen()
        p.print_title(titles.TITLES["reports"], padding=TOTAL_WIDTH)

        # Hacemos la cabecera de la tabla
        p.print_line(''.ljust(center_padding) + ''.ljust(RP_2_WIDTH, '*'))
        p.print_line(''.ljust(center_padding) + texts.TEXTS["report_2_id_game"].rjust(RP_2_ID_GAME) + texts.TEXTS["report_2_id_player"].rjust(RP_2_ID_PLAYER) + texts.TEXTS["report_2_round"].rjust(RP_2_ROUND) + texts.TEXTS["report_2_max_bet"].rjust(RP_2_MAX_BET))
        p.print_line(''.ljust(center_padding) + ''.ljust(RP_2_WIDTH, '*'))
        print()

        # Pedimos los datos a la base de datos limitados por 15, gestionando en que página nos encontramos
        p.print_line(''.ljust(center_padding) + '1920'.rjust(RP_2_ID_GAME) + '12345678O'.rjust(RP_2_ID_PLAYER) + '25'.rjust(RP_2_ROUND) + '28'.rjust(RP_2_MAX_BET))

        # Gestionamos input del usuario para mostrar más resultados o salir al menú de reportes
        if page == 1:
            text = texts.TEXTS["report_next_page"]
        elif page == total_pages:
            text = texts.TEXTS["report_back_page"]
        else:
            text = texts.TEXTS["report_next_page_back_page"]
        option = input('\n' + ''.ljust(center_padding) + text)

        if option == '+' and page != total_pages:
            page += 1
        elif option == '-' and page != 1:
            page -= 1
        elif option.lower() == "exit":
            exit = True
            continue
        else:
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))