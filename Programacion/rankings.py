import math

import printing as p
import texts
import titles
import utils
from sizes import *
from menu import *
from db_access_config import execute_query_in_db

RANKING_LIMIT = 10
RANKING_TO_ORDER_COLUMNS = {
    1: {
        "column": "earnings",
        "title": "ranking_more_earnings"
    },
    2: {
        "column": "games_played",
        "title": "ranking_more_games_played"
    },
    3: {
        "column": "minutes_played",
        "title": "ranking_more_minutes_played"
    },
}
RANKING_TITLES = [
    texts.TEXTS["ranking_id_player"],
    texts.TEXTS["ranking_name"],
    texts.TEXTS["ranking_earnings"],
    texts.TEXTS["ranking_games_played"],
    texts.TEXTS["ranking_minutes_played"]
]
RANKING_WIDTHS = [
    R_PLAYER_ID,
    R_NAME,
    R_EARNINGS,
    R_GAMES_PLAYED,
    R_MINUTES_PLAYED
]

def rankings_option():
    exit_submenu = False

    while not exit_submenu:
        utils.clear_screen()
        p.print_title(titles.TITLES["reports"], padding=TOTAL_WIDTH)
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
            else:
                show_ranking(option)
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

def show_ranking(column_to_order):
    """
    Mostramos el ranking que corresponde por pantalla
    :param column_to_order: (int) -> Número de la opción por la que hemos de ordenar el ranking
    :return: None
    """
    page = 1
    center_padding = (TOTAL_WIDTH - RANKING_WIDTH) // 2
    exit = False

    # Pedimos los datos a la base de datos, ordenados según corresponde, y calculamos las páginas totales
    query = f"SELECT * FROM v_ranking ORDER BY {RANKING_TO_ORDER_COLUMNS[column_to_order]["column"]} desc;"
    data = execute_query_in_db(query)
    total_pages = math.ceil(len(data)/RANKING_LIMIT)

    while not exit:
        # Limpiamos pantalla y mostramos título principal
        utils.clear_screen()
        p.print_title(titles.TITLES[RANKING_TO_ORDER_COLUMNS[column_to_order]["title"]], padding=TOTAL_WIDTH)

        # Hacemos la cabecera de la tabla
        p.print_line(''.ljust(center_padding) + ''.ljust(RANKING_WIDTH, '*'))
        line = ''.ljust(center_padding) + ''.ljust(R_PADDING)
        for index, title in enumerate(RANKING_TITLES):
            if index < 2:
                line += title.ljust(RANKING_WIDTHS[index])
            else:
                line += title.rjust(RANKING_WIDTHS[index])
        p.print_line(line)
        p.print_line(''.ljust(center_padding) + ''.ljust(RANKING_WIDTH, '*'))

        # Mostramos los datos limitados por 10, gestionando en que página nos encontramos
        for row in data[RANKING_LIMIT*(page-1) : RANKING_LIMIT*page]:
            line = ''.ljust(center_padding) + ''.ljust(R_PADDING)
            for index, column in enumerate(row):
                if index < 2:
                    line += str(column).ljust(RANKING_WIDTHS[index])
                else:
                    line += str(column).rjust(RANKING_WIDTHS[index])
            p.print_line(line)
        
        # Gestionamos input del usuario para mostrar más resultados o salir al menú de reportes
        exit, page = handle_user_input(page, total_pages, center_padding)

def handle_user_input(page, total_pages, center_padding):
    """
    Manejamos el input del usuario a la hora de avanzar, retroceder o salir de la pantalla de Reportes
    :param page: (int) -> Página en la que nos encontramos actualmente
    :param total_pages: (int) -> Total de páginas que tenemos disponibles
    :param center_padding: (int) -> Padding que tenemos a la izquierda para que el texto quede a la misma altura que
    columna izquierda del reporte
    :return: (tuple) -> Bool, si ha de salir o no, Int, número de página
    """
    text = ''
    if page != total_pages:
        text += texts.TEXTS["query_next_page"]
    if page != 1:
        text += texts.TEXTS["query_back_page"]
    text += texts.TEXTS["ranking_exit"]
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