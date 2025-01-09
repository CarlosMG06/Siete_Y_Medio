from decks import decks, deck_names
import printing as p
import titles
import texts
import utils
from sizes import *
from menu import card_deck_submenu

# Configuración por defecto
game_settings = {
    "players": {},
    "deck": decks[0],
    "max_rounds": 5
}

def set_players_game():
    pass

def show_players_game():
    pass

def set_max_rounds():
    exit_submenu = False
    while not exit_submenu:
        utils.clear_screen()
        p.print_title(titles.TITLES["max_rounds"], padding=TOTAL_WIDTH)
        try:
            max_rounds = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["max_rounds"] + ": "))

            if max_rounds < 1:
                print()
                p.print_line(texts.TEXTS["value_error_positive"], padding=TOTAL_WIDTH, fill_char='=')
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                continue

            exit_submenu = True
            game_settings["max_rounds"] = max_rounds
            p.print_line(f"Set number of rounds to {max_rounds}", padding=TOTAL_WIDTH, fill_char=' ')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

def set_cards_deck():
    exit_submenu = False
    while not exit_submenu:
        utils.clear_screen()
        p.print_title(titles.TITLES["deck"], padding=TOTAL_WIDTH)
        card_deck_submenu(padding=LEFT_SPACE_OPTIONS)
        try:
            option = int(input("\n" + "".ljust(LEFT_SPACE_OPTIONS) + texts.TEXTS["option"] + ": "))

            if option < MIN_OPTION or option > MAX_OPTION_1:
                print()
                p.print_line(texts.TEXTS["invalid_option"], padding=TOTAL_WIDTH, fill_char='=')
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
                continue

            exit_submenu = True
            if option != MAX_OPTION_1:
                game_settings["deck"] = decks[option - 1]
                p.print_line(f"Set deck of cards to {deck_names[option-1]}", padding=TOTAL_WIDTH, fill_char=' ')
                input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))