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
    newDeck = {}
    keys = list(deck)

    for item in keys:
        eleccion = keys[random.randint(0, len(keys) - 1)]
        while eleccion in newDeck:
            eleccion = keys[random.randint(0, len(keys) - 1)]
        
        newDeck[eleccion] = deck[eleccion]

    return newDeck

def press_to_continue():
    input("\n" + texts.TEXTS['continue'].center(sizes.TOTAL_WIDTH))

def generate_random_number(start, end):
    if math.floor(start) == 0:
        start =+ 1
    return random.randint(math.floor(start), math.floor(end))