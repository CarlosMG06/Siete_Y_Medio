import printing as p
import texts
import titles
import utils
from sizes import *
from menu import *

REPORT_LIMIT = 15
reports = {
    1: {
        "width": RP_1_WIDTH,
        "titles": [
            texts.TEXTS["report_id_player"],
            texts.TEXTS["report_suit"],
            texts.TEXTS["report_initial_card"],
            texts.TEXTS["report_times_repeated"],
            texts.TEXTS["report_games_played"]
                ],
        "widths": [
            RP_ID_PLAYER,
            RP_SUIT,
            RP_INITIAL_CARD,
            RP_TIMES_REPEATED,
            RP_TOTAL_GAMES
                ],
        "query": ""
    },
2: {
        "width": RP_2_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_id_player"],
            texts.TEXTS["report_max_bet"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_ID_PLAYER,
            RP_MAX_BET
                ],
        "query": ""
    },
3: {
        "width": RP_3_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_id_player"],
            texts.TEXTS["report_min_bet"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_ID_PLAYER,
            RP_MIN_BET
                ],
        "query": ""
    },
4: {
        "width": RP_4_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_id_player"],
            texts.TEXTS["report_rounds"],
            texts.TEXTS["report_avg_bet"],
            texts.TEXTS["report_rounds_won"],
            texts.TEXTS["report_pce_won"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_ID_PLAYER,
            RP_ROUNDS,
            RP_AVG_BET,
            RP_WIN_ROUNDS,
            RP_PCE_WON
                ],
        "query": ""
    },
5: {
        "width": RP_5_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_rounds_won"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_WIN_ROUNDS
                ],
        "query": ""
    },
6.1: {
        "width": RP_61_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_id_player"],
            texts.TEXTS["report_rounds_won"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_ID_PLAYER,
            RP_WIN_ROUNDS
                ],
        "query": ""
    },
6.2: {
        "width": RP_62_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_rounds_won"]
                ],
        "widths": [
                    RP_ID_GAME,
                    RP_WIN_ROUNDS
                ],
        "query": ""
    },
7: {
        "width": RP_7_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_user_been_bank"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_USER_BEEN_BANK
                ],
        "query": ""
    },
8: {
        "width": RP_8_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_avg_bet"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_AVG_BET
                ],
        "query": ""
    },
9: {
        "width": RP_9_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_avg_bet"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_AVG_BET
                ],
        "query": ""
    },
10: {
        "width": RP_10_WIDTH,
        "titles": [
            texts.TEXTS["report_id_game"],
            texts.TEXTS["report_rounds"],
            texts.TEXTS["report_avg_bet"]
                ],
        "widths": [
            RP_ID_GAME,
            RP_ROUNDS,
            RP_AVG_BET
                ],
        "query": ""
    }
}


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
                show_report(1)
            elif option == 2:
                show_report(2)
            elif option == 3:
                show_report(3)
            elif option == 4:
                show_report(4)
            elif option == 5:
                show_report(5)
            elif option == 6:
                select_option_6()
            elif option == 7:
                show_report(7)
            elif option == 8:
                show_report(8)
            elif option == 9:
                show_report(9)
            elif option == 10:
                show_report(10)
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

def show_report(option):
    rp_width = reports[option]["width"]
    rp_titles = reports[option]["titles"]
    rp_widths = reports[option]["widths"]
    rp_query = reports[option]["query"]

    page = 1
    # Recoger el count de todos los elementos que puedan recogerse de la base de datos
    total_pages = 10
    center_padding = (TOTAL_WIDTH - rp_width) // 2
    exit = False

    while not exit:
        # Limpiamos pantalla y mostramos título principal
        utils.clear_screen()
        p.print_title(titles.TITLES["reports"], padding=TOTAL_WIDTH)

        # Hacemos la cabecera de la tabla
        p.print_line(''.ljust(center_padding) + ''.ljust(rp_width, '*'))

        line = ''.ljust(center_padding)
        for index, title in enumerate(rp_titles):
            line += title.rjust(rp_widths[index])
        p.print_line(line)
        p.print_line(''.ljust(center_padding) + ''.ljust(rp_width, '*'))
        print()

        # Pedimos los datos a la base de datos limitados por 15, gestionando en que página nos encontramos
        line = ''.ljust(center_padding)
        for index, title in enumerate(rp_titles):
            line += '+' + ''.rjust(rp_widths[index] - 1, '-')
        p.print_line(line)

        # Gestionamos input del usuario para mostrar más resultados o salir al menú de reportes
        exit, page = handle_user_input(page, total_pages, center_padding)

def handle_user_input(page, total_pages, center_padding):
    if page == 1:
        text = texts.TEXTS["report_next_page"]
    elif page == total_pages:
        text = texts.TEXTS["report_back_page"]
    else:
        text = texts.TEXTS["report_next_page_back_page"]
    option = input('\n' + ''.ljust(center_padding) + text).strip()

    if option == '+' and page != total_pages:
        page += 1
    elif option == '-' and page != 1:
        page -= 1
    elif option.lower() == "exit":
        return True, page
    else:
        print()
        p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
    return False, page

def select_option_6():
    exit = False

    while not exit:
        # Limpiamos pantalla y mostramos título principal
        utils.clear_screen()
        p.print_title(titles.TITLES["reports"], padding=TOTAL_WIDTH)
        reports_option_6_submenu(padding=LEFT_SPACE_OPTIONS)
        try:
            option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
            if option < MIN_OPTION or option > MAX_OPTION_4:
                print()
                p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                continue

            if option == MAX_OPTION_4:
                exit = True
            elif option == 1:
                show_report(6.1)
            elif option == 2:
                show_report(6.2)
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))