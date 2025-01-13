import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

import printing as p
import texts
import titles
import utils
from sizes import *
from menu import *

SAVE_REPORT_PATH = os.path.dirname(os.path.abspath(__file__)).replace("Programacion", "Marcas/Reports")

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
        "query": "",
        "file_name": "init_card_most_repeated_player.xml"
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
        "query": "",
        "file_name": "game_max_bet_player.xml"
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
        "query": "",
        "file_name": "game_min_bet_player.xml"
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
        "query": "",
        "file_name": "pce_won_rounds_avg_bet.xml"
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
        "query": "",
        "file_name": "won_game_bots.xml"
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
        "query": "",
        "file_name": "bank_wins_distinguish_user.xml"
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
        "query": "",
        "file_name": "bank_wins.xml"
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
        "query": "",
        "file_name": "banks_players.xml"
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
        "query": "",
        "file_name": "game_avg_bet.xml"
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
        "query": "",
        "file_name": "first_round_avg_bet.xml"
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
        "query": "",
        "file_name": "last_round_avg_bet.xml"
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
            elif option == 6:
                select_option_6()
            else:
                show_report(option)
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

def show_report(option):
    rp_width = reports[option]["width"]
    rp_titles = reports[option]["titles"]
    rp_widths = reports[option]["widths"]
    rp_query = reports[option]["query"]
    rp_file_name = reports[option]["file_name"]

    page = 1
    # Recoger el count de todos los elementos que puedan recogerse de la base de datos
    total_pages = 10
    center_padding = (TOTAL_WIDTH - rp_width) // 2
    exit = False

    # Exportamos los resultados a XML
    results = []
    for row in range(10):
        result = {}
        for columns in range(len(rp_titles)):
            key = rp_titles[columns].replace(" ", "-")
            result[key] = "PlaceHolder"
        results.append(result)
    export_to_xml(results, rp_file_name)

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

def export_to_xml(results_dict, file_name):
    path = os.path.join(SAVE_REPORT_PATH, file_name)
    results = ET.Element('Resultados')

    for result in results_dict:
        row = ET.SubElement(results, 'Fila')
        for key, value in result.items():
            node = ET.SubElement(row, key)
            node.text = value

    xml = prettify(results)

    file = open(path, 'wb')
    file.write(xml)
    file.close()

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(encoding='utf-8', indent="  ")