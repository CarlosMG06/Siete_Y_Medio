import printing as p
import players as pl
import texts
import titles
import utils
import game
from sizes import *
from menu import *

LIMIT_MIN_ROUNDS = 1
LIMIT_MAX_ROUNDS = 30

def settings_option(players):
    """
    Imprimimos y gestionamos el funcionamiento del submenú de Settings
    :return: (int) -> Número de rondas
    """
    exit_submenu = False
    max_rounds = 5

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
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                continue

            if option == MAX_OPTION_1:
                exit_submenu = True
            elif option == 1:
                setup_players(players)
            elif option == 2:
                set_deck()
            elif option == 3:
                max_rounds = setup_max_rounds()

        # Controlamos si el jugador no nos introduce un número como opción, mostramos un mensaje de error y volvemos a comenzar
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

    return max_rounds

def setup_players(players):
    exit_setPlayersSubmenu = False
    while not exit_setPlayersSubmenu:

        exit_showSelectedPlayers = False
        while not exit_showSelectedPlayers:
            utils.clear_screen()
            p.print_title(titles.TITLES["set_game_players"], padding=TOTAL_WIDTH)

            p.print_line_centered("Actual Players In Game", fill_char="*")
            p.print_selected_players(game.selectedPlayers)
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            break

        utils.clear_screen()
        p.print_title(titles.TITLES["set_game_players"], padding=TOTAL_WIDTH)
        pl.show_players_no_input(players)
        p.print_line(
            "Option (id to add to game), -id to remove player, sh to show actual players in game, -1 to go back",
            padding=TOTAL_WIDTH, fill_char=" ")
        eleccion = str(input())
        if eleccion == "-1":
            break

        if len(eleccion) == 9:  # La longitud de un DNI
            players_dic = pl.player_list_to_dic(players)
            if eleccion in players_dic.keys():
                game.selectedPlayers[eleccion] = players_dic[eleccion]
                p.print_line(game.selectedPlayers[eleccion]["name"] + " has been added to the game",
                             padding=TOTAL_WIDTH, fill_char=" ")
                input()
            else:
                p.print_line(eleccion + " isn't a valid player", padding=TOTAL_WIDTH, fill_char=" ")
                input()

        if len(eleccion) == 10:  # La longitud de un DNI con un menos delante
            if eleccion[1:] in game.selectedPlayers.keys():
                p.print_line(eleccion[1:] + " has been deleted from the game", padding=TOTAL_WIDTH, fill_char=" ")
                del game.selectedPlayers[eleccion[1:]]
                input()
            else:
                p.print_line(eleccion[1:] + " isn't currently playing", padding=TOTAL_WIDTH, fill_char=" ")
                input()

def set_deck():
    exit_decksubmenu = False
    while not exit_decksubmenu:
        utils.clear_screen()
        p.print_title(titles.TITLES["decks"], padding=TOTAL_WIDTH)
        # imprimir el menu ya hecho en modulo menu.py
        decks_submenu(padding=LEFT_SPACE_OPTIONS)
        eleccion = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))

        if eleccion < MIN_OPTION or eleccion > MAX_OPTION_1:
            print()
            p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            continue

        if eleccion == MAX_OPTION_1:
            exit_decksubmenu = True

        if eleccion == 1:
            game.activeDeck = mazos.esp48
            input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + "Active deck set to: ESP48")

        if eleccion == 2:
            game.activeDeck = mazos.esp40
            input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + "Active deck set to: ESP40")

        if eleccion == 3:
            game.activeDeck = mazos.poker
            input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + "Active deck set to: Poker")

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
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
            else:
                print()
                p.print_line(texts.TEXTS["setup_max_rounds"] + str(new_max_rounds) + " ", padding=TOTAL_WIDTH, fill_char='*')
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                exit = True

        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

    return new_max_rounds