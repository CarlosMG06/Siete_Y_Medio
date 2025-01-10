import os
import random

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