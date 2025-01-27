import random
import string

from menu import *
import utils
from sizes import *
import texts
import printing as p
import titles
from db_access_config import execute_transaction_in_db, insert_query

NIF_LENGTH = 9
NIF_NUMBERS_END_POSITION = 7
NIF_LETTER_POSITION = 8

MAX_POINTS = 7.5

RISK_PROFILES = {
    1: "Cautious",
    2: "Moderated",
    3: "Bold"
}

RISK_QUANTITIES = {
    "Cautious": 30,
    "Moderated": 40,
    "Bold": 50
}

def players_option(players):
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
                utils.press_to_continue()
                continue

            if option == MAX_OPTION_1:
                exit_submenu = True
            elif option == 1:
                players = create_new_player(players, True)
            elif option == 2:
                players = create_new_player(players, False)
            elif option == 3:
                show_players(players)
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()

    return players

def get_players_from_db(**kwargs):
    """
    Recogemos los jugadores de la base de datos con los parámetros indicados
    :param kwargs: Lista de argumentos clave-valor para filtrar la búsqueda de jugadores
    :return: (list) -> Lista de diccionarios con los jugadores recogidos de la base de datos
    """
    query = "SELECT * FROM player;"
    player_list_tuple = execute_transaction_in_db(query)
    # Convertimos la lista de tuplas en una lista de diccionarios
    PLAYER_KEYS = ("id","name","human","type")
    players = []
    for player in player_list_tuple:
        player_dict = dict(zip(PLAYER_KEYS,player))
        player_dict["type"] = RISK_PROFILES[player_dict["type"]]
        players.append(player_dict)
    
    return players

def create_new_player(players, human):
    """
    Generamos un nuevo jugador
    :param players: (list) -> Lista con los jugadores actuales
    :param human: (bool) -> Si el jugador nuevo es humano o un bot
    :return: (list) -> Lista con los jugadores
    """

    if human:
        NEW_PLAYER_TITLE = titles.TITLES["new_human_player"]
        DEMAND_NAME_TEXT = texts.TEXTS["demand_human_name"]
        NIF_TEXT = texts.TEXTS["demand_nif"]
        DEMAND_PROFILE_TEXT = texts.TEXTS["demand_human_profile"]
    else:
        NEW_PLAYER_TITLE = titles.TITLES["new_bot_player"]
        DEMAND_NAME_TEXT = texts.TEXTS["demand_bot_name"]
        NIF_TEXT = texts.TEXTS["bot_nif"]
        DEMAND_PROFILE_TEXT = texts.TEXTS["demand_bot_profile"]
    
    utils.clear_screen()
    p.print_title(NEW_PLAYER_TITLE, padding=TOTAL_WIDTH)

    # Pedimos el nombre del jugador, deberá tener un largo de 1 a 32 carácteres (limitados en base de datos)
    while True:
        name_input = input("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_NAME_TEXT)
        if len(name_input) > 0 and len(name_input) <= 32 and name_input.isalpha():
            break

        # En caso que nos introduzca mal el nombre, volvemos a imprimir el título
        print()
        p.print_line(texts.TEXTS["error_demand_name"], padding=TOTAL_WIDTH, fill_char='!')
        utils.press_to_continue()
        utils.clear_screen()
        p.print_title(NEW_PLAYER_TITLE, padding=TOTAL_WIDTH)
    
    if human:
        while True:
            # Recogemos el input del NIF (sólo verificamos que tenga 8 números y 1 letra, no si es 100% válido)
            nif_input = input("".ljust(LEFT_SPACE_OPTIONS) + NIF_TEXT).upper()
            if len(nif_input) == 9:
                nif_numbers = nif_input[:NIF_NUMBERS_END_POSITION]
                nif_letter = nif_input[NIF_LETTER_POSITION]
                if nif_numbers.isdigit() and nif_letter.isalpha():
                    index = -1
                    for i in range(len(players)):
                        if players[i]["id"] == nif_input:
                            index = i
                            break

                if index == -1:
                    break
                else:
                    print()
                    p.print_line(texts.TEXTS["error_duplicated_nif"], padding=TOTAL_WIDTH, fill_char='!')
                    utils.press_to_continue()

            # En caso que no nos introduzca un NIF válido, deberemos:
            #   1. Mostrar mensaje de error
            #   2. Limpiar pantalla
            #   3. Imprimir el título
            #   4. Imprimir el mensaje de entrada del nombre
            else:
                print()
                p.print_line(texts.TEXTS["error_demand_nif"], padding=TOTAL_WIDTH, fill_char='!')
                utils.press_to_continue()
            utils.clear_screen()
            p.print_title(NEW_PLAYER_TITLE, padding=TOTAL_WIDTH)
            p.print_line("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_NAME_TEXT + name_input)
    else:
        # Generamos aleatoriamente un NIF para el bot
        while True:
            nif_input = (''.join(["{}".format(random.randint(0, 9)) for num in range(0, NIF_NUMBERS_END_POSITION + 1)]) +
                        random.choice(string.ascii_uppercase))
            index = -1
            for i in range(len(players)):
                if players[i]["id"] == nif_input:
                    index = i
                    break

            if index == -1:
                p.print_line("".ljust(LEFT_SPACE_OPTIONS) + NIF_TEXT + nif_input)
                break

    # Pedimos el perfil de riesgo del jugador, incluso si es humano, en caso que esté controlado por la IA
    while True:
        print()
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_PROFILE_TEXT)
        profile_menu(LEFT_SPACE_OPTIONS)
        try:
            profile_option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
            if profile_option >= 1 and profile_option <= 3:
                profile_input = RISK_PROFILES[profile_option]
                break
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()

        # En caso que se imprima el mensaje de error, deberemos:
        #   1. Limpiar pantalla
        #   2. Imprimir el título
        #   3. Imprimir el mensaje de entrada del nombre
        #   4. Imprimir el mensaje de entrada del NIF
        utils.clear_screen()
        p.print_title(NEW_PLAYER_TITLE, padding=TOTAL_WIDTH)
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_NAME_TEXT + name_input)
        p.print_line("".ljust(LEFT_SPACE_OPTIONS) + NIF_TEXT + nif_input)

    # A continuación, deberemos limpiar la pantalla y volver a mostrar los resultados:
    #   1. Limpiar pantalla
    #   2. Imprimir el título
    #   3. Imprimir el mensaje de entrada del nombre
    #   4. Imprimir el mensaje de entrada del NIF
    #   5. Imprimir el mensaje de entrada del Perfil
    #   6. Preguntamos si está correcto:
    #      Por defecto será Y, en caso de no tener una N
    #      Se guardará el jugador en la BBDD
    #      Se crea un diccionario del jugador, se añade a la lista
    #   Se devuelve la lista de jugadores
    utils.clear_screen()
    p.print_title(NEW_PLAYER_TITLE, padding=TOTAL_WIDTH)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_NAME_TEXT + name_input)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + NIF_TEXT + nif_input)
    p.print_line("".ljust(LEFT_SPACE_OPTIONS) + DEMAND_PROFILE_TEXT + profile_input)

    print()
    is_ok = input("".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_confirmation"])
    if is_ok.lower() != "n":
        db_player = {
            "id": nif_input,
            "player_name": name_input,
            "is_human": human,
            "risk_type": profile_option
        }
        query = insert_query(db_player, "player")
        execute_transaction_in_db(query, DML=True)
        
        player = {
            "id": nif_input,
            "name": name_input,
            "human": human,
            "type": profile_input
        }
        players.append(player)
    return players

def show_players(players):
    """
    Mostramos por pantalla los diferentes jugadores que tenemos guardados, separados por Bots y Humanos
    :param players: (list) -> Lista de los jugadores
    :return: None
    """
    while True:
        utils.clear_screen()
        # Imprimimos el marco superior que será siempre estático
        p.print_title(titles.TITLES["show_remove_players"], padding=TOTAL_WIDTH)
        p.print_line(texts.TEXTS["select_players"].center(TOTAL_WIDTH, '*'))
        p.print_line(texts.TEXTS["select_players_bot"].center(HALF_WIDTH - 1) + '||' + texts.TEXTS[
            "select_players_human"].center(HALF_WIDTH - 1))
        p.print_line(''.ljust(TOTAL_WIDTH, '-'))
        p.print_line(texts.TEXTS["select_players_id"].ljust(SP_COLUMN_ID) + texts.TEXTS["select_players_name"].ljust(
            SP_COLUMN_NAME) + texts.TEXTS["select_players_type"].ljust(SP_COLUMN_TYPE) + '||' + texts.TEXTS["select_players_id"].ljust(SP_COLUMN_ID) + texts.TEXTS["select_players_name"].ljust(
            SP_COLUMN_NAME) + texts.TEXTS["select_players_type"].ljust(SP_COLUMN_TYPE))
        p.print_line(''.ljust(TOTAL_WIDTH, '*'))

        # Separamos los tipos de jugadores y revisamos cuál es mayor
        bot_players, human_players = separate_players(players)
        most_players = 0
        if len(bot_players) >= len(human_players):
            most_players = len(bot_players)
        else:
            most_players = len(human_players)

        # Mostramos todos los jugadores
        for index in range(most_players):
            if index >= len(bot_players):
                bot_line = "".ljust(HALF_WIDTH - 1)
            else:
                bot_line = " " + bot_players[index]["id"].ljust(SP_COLUMN_ID - 1) + bot_players[index][
                    "name"].ljust(
                    SP_COLUMN_NAME) + bot_players[index]["type"].ljust(SP_COLUMN_TYPE)

            if index >= len(human_players):
                human_line = "".ljust(HALF_WIDTH - 1)
            else:
                human_line = " " + human_players[index]["id"].ljust(SP_COLUMN_ID - 1) + human_players[index][
                    "name"].ljust(
                    SP_COLUMN_NAME) + human_players[index]["type"].ljust(SP_COLUMN_TYPE)

            p.print_line(bot_line + '||' + human_line)

        # Cerramos la tabla
        p.print_line(''.ljust(TOTAL_WIDTH, '*'))

        # Generamos input para que el usuario pueda eliminar un jugador o salir
        option = input("\n" + "".ljust(LEFT_SPACE_OPTIONS_REPORTS) + texts.TEXTS["option_delete_player"])
        if option == "exit":
            return

        if len(option) == 10 and option[0] == "-":
            id = option[1:].upper()
            index = -1
            for i in range(len(players)):
                if players[i]["id"] == id:
                    index = i
                    break

            if index == -1:
                print()
                p.print_line(texts.TEXTS["error_demand_nif"], padding=TOTAL_WIDTH, fill_char='=')
                utils.press_to_continue()
            else:
                query = f"SELECT count(DISTINCT game_id) FROM player_game WHERE player_id = '{id}'"
                games_with_player = execute_transaction_in_db(query, one=True)
                if games_with_player > 0:

                    print()
                    p.print_line(texts.TEXTS["warning_delete_player"].replace("ALL # GAMES", "THE GAME") if games_with_player == 1 else
                        texts.TEXTS["warning_delete_player"].replace("#", str(games_with_player)), padding=TOTAL_WIDTH, fill_char='!')
                    sure = input("\n" + "".ljust(LEFT_SPACE_OPTIONS_REPORTS) + "Type 'CONFIRM' to confirm the deletion: ")
                    if sure != "CONFIRM":
                        print()
                        p.print_line(texts.TEXTS["cancel_delete_player"], padding=TOTAL_WIDTH, fill_char='·')
                        utils.press_to_continue()
                        continue
                del players[index]
                # Borramos de la BBDD
                query = f"DELETE FROM player WHERE id = '{id}';"
                execute_transaction_in_db(query, DML=True)

                print()
                p.print_line(texts.TEXTS["player_deleted"], padding=TOTAL_WIDTH, fill_char='*')
                utils.press_to_continue()
        else:
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()

def show_players_no_input(players):
    """
    Mostramos por pantalla los diferentes jugadores que tenemos guardados, separados por Bots y Humanos
    :param players: (list) -> Lista de los jugadores
    :return: None
    """

    # Imprimimos el marco superior que será siempre estático
    p.print_line(texts.TEXTS["select_players"].center(TOTAL_WIDTH, '*'))
    p.print_line(texts.TEXTS["select_players_bot"].center(HALF_WIDTH - 1) + '||' + texts.TEXTS[
        "select_players_human"].center(HALF_WIDTH - 1))
    p.print_line(''.ljust(TOTAL_WIDTH, '-'))
    p.print_line(texts.TEXTS["select_players_id"].ljust(SP_COLUMN_ID) + texts.TEXTS["select_players_name"].ljust(
        SP_COLUMN_NAME) + texts.TEXTS["select_players_type"].ljust(SP_COLUMN_TYPE) + '||' + texts.TEXTS["select_players_id"].ljust(SP_COLUMN_ID) + texts.TEXTS["select_players_name"].ljust(
        SP_COLUMN_NAME) + texts.TEXTS["select_players_type"].ljust(SP_COLUMN_TYPE))
    p.print_line(''.ljust(TOTAL_WIDTH, '*'))

    # Separamos los tipos de jugadores y revisamos cuál es mayor
    bot_players, human_players = separate_players(players)
    most_players = 0
    if len(bot_players) >= len(human_players):
        most_players = len(bot_players)
    else:
        most_players = len(human_players)

    # Mostramos todos los jugadores
    for index in range(most_players):
        if index >= len(bot_players):
            bot_line = "".ljust(HALF_WIDTH - 1)
        else:
            bot_line = " " + bot_players[index]["id"].ljust(SP_COLUMN_ID - 1) + bot_players[index][
                "name"].ljust(
                SP_COLUMN_NAME) + bot_players[index]["type"].ljust(SP_COLUMN_TYPE)

        if index >= len(human_players):
            human_line = "".ljust(HALF_WIDTH - 1)
        else:
            human_line = " " + human_players[index]["id"].ljust(SP_COLUMN_ID - 1) + human_players[index][
                "name"].ljust(
                SP_COLUMN_NAME) + human_players[index]["type"].ljust(SP_COLUMN_TYPE)

        p.print_line(bot_line + '||' + human_line)

    # Cerramos la tabla
    p.print_line(''.ljust(TOTAL_WIDTH, '*'))

def separate_players(players):
    """
    Separamos los jugadores según su tipo (Bot o Humanos) y los devolvemos en dos listas distintas
    :param players: (list) -> Lista con los diferentes jugadores que tenemos almacenados
    :return: (tuple) -> Tupla con dos listas, una de jugadores bot y otra con jugadores humanos
    """
    bot_players = []
    human_players = []
    for player in players:
        if player["human"]:
            human_players.append(player)
        else:
            bot_players.append(player)

    return bot_players, human_players

def cpu_demand_card(player, deck, players_results, players_bets):
    """
    Revisamos si el jugador bot puede (dependiendo de si es banca o su perfil) pedir carta para seguir jugando
    su turno
    :param player: (dict) -> Diccionario con todos los datos referentes al jugador
    :param deck: (dict) -> Diccionario con las diferentes cartas y sus valores
    :param players_results: (list) -> Lista con los resultados de los diferentes jugadores, necesario por si el
    jugador al que le estamos calculando la tirada es banca
    :return: (bool) -> Devolvemos True si puede coger carta o False si debe pasar
    """
    can_demand = False
    sum_valid = 0
    total_cards = 0

    # Iteramos por los valores de todas las cartas que tenemos en el mazo
    for card in deck.values():
        # Sumamos los puntos actuales con los de la carta que estamos revisando:
        #   SI nos da 7,5 o menos, añadiremos 1 al valor sum_valid
        # Aumentamos en 1 el valor de las cartas que estamos contando
        if player["cards_value"] + card["real_value"] <= MAX_POINTS:
            sum_valid += 1
        total_cards += 1

    # Calculamos el riesgo que tenemos de pasarnos en caso de pedir carta
    # (cartas_que_no_nos_pasarnos / total_de_cartas_en_el_mazo) * 100 para sacar porcentaje
    risk = 100 - ((sum_valid / total_cards) * 100)

    # Consultamos los riesgos según el tipo de jugador:
    #   1. El riesgo calculado es menor al riesgo de jugador, devolvemos True para coger carta
    #   2. Si es banca y algún jugador tiene más puntos que nosotros:
    #       2.1 Si estamos dentro de nuestro riesgo, devolvemos True para coger carta
    #       2.2 Si no estamos en nuestro riesgo pero nos quedamos sin puntos al perder, devolvemos True para coger carta
    #   3. Si el riesgo es mayor al de nuestro jugador y no somos banca, devolvemos False para saltar nuestro turno y
    #   quedarnos tal y como estamos
    if player["bank"]:
        better_plays = []
        for index, result in enumerate(players_results):
            if player["cards_value"] < result and result <= MAX_POINTS:
                better_plays.append(index)

        if len(better_plays) != 0:
            if risk <= RISK_QUANTITIES[player["type"]]:
                can_demand = True
            else:
                lost_points = 0
                for index in better_plays:
                    lost_points += players_bets[index]

                if player["points"] - lost_points <= 0:
                    can_demand = True

    elif risk <= RISK_QUANTITIES[player["type"]]:
        can_demand = True

    return can_demand

def cpu_make_bet(player):
    """
    Calculamos la apuesta que debería hacer la CPU según el tipo de jugador que sea
    :param player: (dict) -> Diccionario con todas las claves necesarias de cada jugador
    :return: (int) -> Valor a apostar
    """

    min_bet = 1
    max_bet = player["points"]

    if player["type"] == "Cautious":
        max_bet = int(player["points"] * 0.4)
    elif player["type"] == "Moderated":
        min_bet = int(player["points"] * 0.2)
        max_bet = (player["points"] * 0.6)
    elif player["type"] == "Bold":
        min_bet = int(player["points"] * 0.4)

    return utils.generate_random_number(min_bet, max_bet)

def player_list_to_dict(players):
    player_dict = {}
    for player in players:
        player_dict[player["id"]] = {
            "name": player["name"],
            "human": player["human"],
            "type": player["type"]
        }
    
    return player_dict
