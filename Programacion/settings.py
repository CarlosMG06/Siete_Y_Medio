import printing as p
import players as pl
import texts
import titles
import utils
import game
from sizes import *
from menu import *
from decks import decks

LIMIT_MIN_ROUNDS = 1
LIMIT_MAX_ROUNDS = 30

def settings_option(players):
    """
    Imprimimos y gestionamos el funcionamiento del submenú de Settings
    :return: (int) -> Número de rondas
    """
    exit_submenu = False

    while not exit_submenu:
        # Limpiamos la pantalla, mostramos el título e imprimimos el submenú correspondiente
        utils.clear_screen()
        p.print_title(titles.TITLES["settings"], padding=TOTAL_WIDTH)
        settings_submenu(padding=LEFT_SPACE_OPTIONS)
        try:
            # Recogemos el input con la opción que escoge el jugador
            # SI la opción se encuentra fuera de los límites, mostramos mensaje de error
            # Realizamos estructura IF-ELIF para entrar en las opciones correspondientes
            option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))
            if option < MIN_OPTION or option > MAX_OPTION_1:
                print()
                p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                utils.press_to_continue()
                continue

            if option == MAX_OPTION_1:
                exit_submenu = True
            elif option == 1:
                setup_players(players)
            elif option == 2:
                set_deck()
            elif option == 3:
                setup_max_rounds()

        # Controlamos si el jugador no nos introduce un número como opción, mostramos un mensaje de error y volvemos a comenzar
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()

def setup_players(players):
    exit_set_players_submenu = False
    show_selected_players = True
    while not exit_set_players_submenu:

        if show_selected_players:
            utils.clear_screen()
            p.print_title(titles.TITLES["set_game_players"], padding=TOTAL_WIDTH)

            p.print_line_centered("Current Players In Game", fill_char="*")
            p.print_selected_players(game.selected_players)
            utils.press_to_continue()
        else:
            show_selected_players = True

        utils.clear_screen()
        p.print_title(titles.TITLES["set_game_players"], padding=TOTAL_WIDTH)
        pl.show_players_no_input(players)
        p.print_line(texts.TEXTS["option_setup_players"], padding=TOTAL_WIDTH, fill_char=" ")
        option = input()
        if option == "exit":
            break

        elif len(option) == 9:  # La longitud de un DNI
            id = option.upper()
            player_dict = pl.player_list_to_dict(players)
            if id in game.selected_players.keys():
                name = player_dict[id]["name"]
                print()
                p.print_line(f" {name} is already playing ", padding=TOTAL_WIDTH, fill_char=":")
                utils.press_to_continue()
            elif id in player_dict.keys():
                name = player_dict[id]["name"]
                game.selected_players[id] = player_dict[id]
                print()
                p.print_line(f" {name} has been added to the game ", padding=TOTAL_WIDTH, fill_char="+")
                utils.press_to_continue()       
            else:
                show_selected_players = False
                print()
                p.print_line(f" {id} isn't a valid player ", padding=TOTAL_WIDTH, fill_char="=")
                utils.press_to_continue()

        elif len(option) == 10 and option[0] == "-":  # La longitud de un DNI con un menos delante
            id = option[1:].upper()
            player_dict = pl.player_list_to_dict(players)
            if id in game.selected_players.keys():
                name = player_dict[id]["name"]
                print()
                p.print_line(f" {name} has been deleted from the game ", padding=TOTAL_WIDTH, fill_char="-")
                del game.selected_players[id]
                utils.press_to_continue()
            elif id in player_dict.keys():
                name = player_dict[id]["name"]
                print()
                p.print_line(f" {name} isn't currently playing ", padding=TOTAL_WIDTH, fill_char=":")
                utils.press_to_continue()
            else:
                show_selected_players = False
                print()
                p.print_line(f" {id} isn't a valid player ", padding=TOTAL_WIDTH, fill_char="=")
                utils.press_to_continue()
        
        elif option.lower() != "sh":
            show_selected_players = False
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()
            continue


def set_deck():
    exit_deck_submenu = False
    while not exit_deck_submenu:
        utils.clear_screen()
        p.print_title(titles.TITLES["decks"], padding=TOTAL_WIDTH)
        # imprimir el menu ya hecho en modulo menu.py
        decks_submenu(padding=LEFT_SPACE_OPTIONS)
        option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))

        if option < MIN_OPTION or option > MAX_OPTION_1:
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()
            continue

        if 1 <= option <= 3:
            game.active_deck_id = tuple(decks.keys())[option - 1]
            game.active_deck = decks[game.active_deck_id]
            print()
            p.print_line(f" Active deck set to: {game.active_deck_id} ", padding=TOTAL_WIDTH, fill_char='·')
            input("\n" + texts.TEXTS['continue'].center(TOTAL_WIDTH))
        
        if option == MAX_OPTION_1:
            exit_deck_submenu = True

def setup_max_rounds():
    """
    Configuramos el nuevo número de rondas máximas que se deberán jugar en la partida
    :return: (int) -> Nuevo número de rondas máximas a jugar en la partida
    """
    exit = False
    new_max_rounds = None

    while not exit:
        # Limpiamos la pantalla e imprimimos el título pertinente
        utils.clear_screen()
        p.print_title(titles.TITLES["set_max_rounds"], padding=TOTAL_WIDTH)

        # Realizamos la recogida del número para las nuevas rondas máximas a jugar
        try:
            new_max_rounds = int(input(''.ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["demand_max_rounds"]))

            # SI el número se encuentra fuera del rango que nosotros delimitamos, mostramos mensaje de error y volvemos a preguntar el número
            # SI NO, enseñamos mensaje indicando el nuevo número de rondas y salimos del bucle
            if new_max_rounds < LIMIT_MIN_ROUNDS or new_max_rounds > LIMIT_MAX_ROUNDS:
                print()
                p.print_line(texts.TEXTS["error_max_rounds"], padding=TOTAL_WIDTH, fill_char='=')
                utils.press_to_continue()
            else:
                game.max_rounds = new_max_rounds
                print()
                p.print_line(texts.TEXTS["setup_max_rounds"] + str(new_max_rounds) + " ", padding=TOTAL_WIDTH, fill_char='*')
                utils.press_to_continue()
                exit = True

        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            utils.press_to_continue()
