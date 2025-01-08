def print_title(title, padding = 0, fill_char = '*'):
    """
    Generamos el marco estándar para imprimir los títulos de las diferentes pantallas
    :param title: (string) -> String del título en formato ASCII Art
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :param fill_char: (char) -> Carácter con el que se completará el padding
    :return: None
    """
    # Imprimimos el límite superior
    print(''.center(padding, fill_char))

    # Iteramos por cada una de las líneas del texto en modo ASCII para centrar el texto
    line = ""
    for char in title:
        if char == '\n':
            line = line.center(padding)
            print(line)
            line = ""
            continue
        line += char

    # Imprimimos el límite inferior
    print('\n' + ''.center(padding, fill_char) + '\n')

def print_title_game(title, padding=0, fill_char='*', round=0, player_turn="Placeholder"):
    """
    Generamos el marco específico para imprimir el título en partida
    :param title: (string) -> String del título en formato ASCII Arta
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :param fill_char: (char) -> Carácter con el que se completará el padding
    :param round: (int) -> Nos indica el número de ronda en el que nos encontramos
    :param player_turn: (string) -> Nos indica el nombre del jugador que está realizando la tirada
    :return: None
    """
    # Imprimimos el límite superior
    print(''.center(padding, fill_char))

    # Iteramos por cada una de las líneas del texto en modo ASCII para centrar el texto
    line = ""
    for char in title:
        if char == '\n':
            line = line.center(padding)
            print(line)
            line = ""
            continue
        line += char

    # Imprimimos el límite inferior
    print('\n' + f' Round {round}, Turn of {player_turn} '.center(padding, fill_char) + '\n')

def print_line(text, padding = 0, fill_char = '*'):
    """
    Imprimimos los textos introducidos en una línea, centrandólo en un padding horizontal
    :param text: (string) -> String del error a imprimir por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :param fill_char: (char) -> Carácter con el que se completará el padding
    :return: None
    """
    print(text.center(padding, fill_char))

def print_menu(menu, padding):
    """
    Imprimimos el menú recibido por parámetro
    :param menu: (string) -> String con todas las opciones
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    # Iteramos por cada una de las opciones recibidas y las centramos
    line = ""
    for char in menu:
        if char == '\n':
            line = "".ljust(padding) + line
            print(line)
            line = ""
            continue
        line += char

def print_players(players, padding):
    if len(list(players)) <= 2:
        offset = 8
    else:
        offset = 2

    nameTxt = "Name".ljust(padding // len(list(players)) - offset)
    humanTxt = "Human".ljust(padding // len(list(players)) - offset)
    priorityTxt = "Priority".ljust(padding // len(list(players)) - offset)
    typeTxt = "Type".ljust(padding // len(list(players)) - offset)
    bankTxt = "Bank".ljust(padding // len(list(players)) - offset)
    betTxt = "Bet".ljust(padding // len(list(players)) - offset)
    pointsTxt = "Points".ljust(padding // len(list(players)) - offset)
    cardsTxt = "Cards".ljust(padding // len(list(players)) - offset)
    roundPointsTxt = "Roundpoints".ljust(padding // len(list(players)) - offset)
    
    for player in list(players):
        nameTxt += players[player]["name"].ljust(padding // len(list(players)) - offset)
        humanTxt += str(players[player]["human"]).ljust(padding // len(list(players)) - offset)
        priorityTxt += str(players[player]["priority"]).ljust(padding // len(list(players)) - offset)
        typeTxt += str(players[player]["type"]).ljust(padding // len(list(players)) - offset)
        bankTxt += str(players[player]["bank"]).ljust(padding // len(list(players)) - offset)
        betTxt += str(players[player]["bet"]).ljust(padding // len(list(players)) - offset)
        pointsTxt += str(players[player]["points"]).ljust(padding // len(list(players)) - offset)
        indCardsTxt = ""
        for card in players[player]["cards"]:
            indCardsTxt += card
            if players[player]["cards"].index(card) != len(players[player]["cards"]) - 1:
                indCardsTxt += ";"
            else:
                cardsTxt += indCardsTxt.ljust(padding // len(list(players)) - offset)
        if indCardsTxt == "":
            cardsTxt += "".ljust(padding // len(list(players)) - offset)
        roundPointsTxt += str(players[player]["roundPoints"]).ljust(padding // len(list(players)) - offset)

    print(nameTxt)
    print(humanTxt)
    print(priorityTxt)
    print(typeTxt)
    print(bankTxt)
    print(betTxt)
    print(pointsTxt)
    print(cardsTxt)
    print(roundPointsTxt)