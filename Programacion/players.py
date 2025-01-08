import menu
import utils
from sizes import *
import texts
import printing as p
import titles

NIF_LENGHT = 9
NIF_NUMBERS_END_POSITION = 7
NIF_LETTER_POSITION = 8

PROFILES = {
    1: "Cautious",
    2: "Moderated",
    3: "Bold"
}

def get_players_from_bbdd(**kwargs):
    """
    Recogemos los jugadores de la base de datos con los parámetros indicados
    :param kwargs: Lista de argumentos clave-valor para filtrar la búsqueda de jugadores
    :return: (list) -> Lista de diccionarios con los jugadores recogidos de la base de datos
    """

def get_players():
    # TEMPORAL
    players = {
        "11115555A":
           {
               "name": "Mario",
                "human": True,
                "bank": False,
                "profile": "Moderated"
            },
        "22226666B":
            {
                "name": "Ruben",
                "human": True,
                "bank": False,
                "profile": "Cautious"
            },
        "33337777C":
            {
                "name": "BotLine",
                "human": False,
                "bank": False,
                "profile": "Bold"
            },
        "44448888D":
            {
                "name": "TopLane",
                "human": False,
                "bank": False,
                "profile": "Moderated"
            }
    }

    return players

def create_human_player(players):
    """
    Generamos un nuevo jugador humano
    :param players: (list) -> Lista con los jugadores actuales
    :return: (list) -> Lista con los jugadores
    """

    utils.clear_screen()
    p.print_title(titles.TITLES["new_human_player"], padding=TOTAL_WIDTH)

    # Pedimos el nombre del jugador, deberá tener un largo de 1 a 32 carácteres (limitados en base de datos)
    while True:
        name_input = input("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_name"])
        if len(name_input) > 0 and len(name_input) <= 32 and name_input.isalpha():
            break

        # En caso que nos introduzca mal el nombre, volvemos a imprimir el título
        print()
        p.print_line(texts.TEXTS["error_demand_name"], padding=TOTAL_WIDTH, fill_char='!')
        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        utils.clear_screen()
        p.print_title(titles.TITLES["new_human_player"], padding=TOTAL_WIDTH)

    while True:
        # Recogemos el input del NIF (sólo verificamos que tenga 8 números y 1 letra, no si es 100% válido)
        nif_input = input("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_nif"])
        if len(nif_input) == 9:
            nif_numbers = nif_input[:NIF_NUMBERS_END_POSITION]
            nif_letter = nif_input[NIF_LETTER_POSITION]
            if nif_numbers.isdigit() and nif_letter.isalpha():
                break

        # En caso que no nos introduzca un NIF válida, deberemos:
        #   1. Mostrar mensaje de error
        #   2. Limpiar pantalla
        #   3. Imprimir el título
        #   4. Imprimir el mensaje de entrada del nombre
        print()
        p.print_line(texts.TEXTS["error_demand_nif"], padding=TOTAL_WIDTH, fill_char='!')
        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        utils.clear_screen()
        p.print_title(titles.TITLES["new_human_player"], padding=TOTAL_WIDTH)
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_name"] + name_input)

    # Pedimos al jugador el tipo de jugadas que realizará, en caso que esté controlado por la IA
    profile_input = ""
    while True:
        print()
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_profile"])
        menu.profile_menu(LEFT_SPACE_OPTIONS)
        try:
            option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
            if option >= 1 and option <= 3:
                profile_input = PROFILES[option]
                break
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

        # En caso que se imprima el mensaje de error, deberemos:
        #   1. Limipar pantalla
        #   2. Imprimir el títutlo
        #   3. Imprimir el mensaje de entrada del nombre
        #   4. Imprimir el mensaje de entrada del NIF
        utils.clear_screen()
        p.print_title(titles.TITLES["new_human_player"], padding=TOTAL_WIDTH)
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_name"] + name_input)
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_nif"] + nif_input)

    # A continuación, deberemos limipiar la pantalla y volver a mostrar los resultados:
    #   1. Limpiar pantalla
    #   2. Imprimir el título
    #   3. Imprimir el mensaje de entrada del nombre
    #   4. Imprimir el mensaje de entrada del NIF
    #   5. Imprimir el mensaje de entrada del Perfil
    #   6. Preguntamos si está correcto:
    #      Por defecto será Y, en caso de no tener una N
    #      Se guardará el jugador en la BBDD (TO_DO)
    #      Se crea un diccionario del jugador, se añade a la lista
    #   Se devuelve la lista de jugadores
    utils.clear_screen()
    p.print_title(titles.TITLES["new_human_player"], padding=TOTAL_WIDTH)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_name"] + name_input)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_nif"] + nif_input)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_profile"] + profile_input)

    print()
    is_ok = input("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_confirmation"])
    if is_ok.lower() != "n":
        # Debemos conectar con la BBDD para darlo de alta
        players[nif_input] = {
            "name": name_input,
            "human": True,
            "type": profile_input
        }
    return players

def modify_player(player, player_trait, new_value):
    """
    Modificamos un apartado del jugador que nos llega como parámetro
    :param player: (dict) -> Diccionario con todos los datos del jugador
    :param player_trait: (string) -> Valor de la clave en el diccionario del jugador a modificar
    :param new_value: (string) -> Nuevo valor a ponerle en la clave indicada
    :return: (dict) -> Devolvemos el valor del
    """
    # Revisamos si la clave a cambiar existe dentro del diccionario del jugador
    if player_trait in player.keys():
        player[player_trait] = new_value
        # Imprimimos mensajes indicando que se ha cambiado el valor
        print()
        p.print_line(texts.TEXTS["player_value_changed_ok"], padding=TOTAL_WIDTH, fill_char='=')
        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        # Conectar con la base de datos para cambiar el valor
    else:
        # Imprimimos mensajes indicando que la clave no existe
        print()
        p.print_line(texts.TEXTS["player_value_changed_error"] + player_trait, padding=TOTAL_WIDTH, fill_char='!')
        input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

    # Devolvemos el diccionario del jugador
    return player

def show_players(players):
    """
    Mostramos por pantalla los diferentes jugadores que tenemos guardados, separados por Bots y Humanos
    :param players: (list) -> Lista de los jugadores
    :return: None
    """
    utils.clear_screen()
    p.print_title(titles.TITLES["show_remove_players"], padding=TOTAL_WIDTH)
    input()
