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

def doPasada(lista):
    resultado = []

    if len(lista) == 1:
        resultado = lista
        return resultado
    
    if lista[0] > lista[1]:
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux
    
    resultado.append(lista[0])
    resultado += doPasada(lista[1:])

    return resultado

def doBurbuja(lista):
    resultado = []

    if len(lista) != 1:
        lista = doPasada(lista)
        resultado = doBurbuja(lista[:-1])
        resultado.append(lista[-1])

    else:
        resultado = lista

    return resultado

def generate_random_number(start, end):
    return random.randint(start, end)