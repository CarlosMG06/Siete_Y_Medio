import os
import random
import math
import texts
import sizes

def clear_screen():
    if os.name == 'nt':     # Windows
        os.system('cls')
    else:                   # Linux o macOS
        os.system('clear')


def shuffle_cards(deck):
    new_deck = {}
    keys = list(deck)

    for item in keys:
        option = keys[random.randint(0, len(keys) - 1)]
        while option in new_deck:
            option = keys[random.randint(0, len(keys) - 1)]
        
        new_deck[option] = deck[option]

    return new_deck

def press_to_continue():
    input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))

def generate_random_number(start, end):
    if math.floor(start) == 0:
        start =+ 1
    return random.randint(math.floor(start), math.floor(end))