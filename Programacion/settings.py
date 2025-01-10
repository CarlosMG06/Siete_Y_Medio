import printing as p
import texts
import titles
import utils
from sizes import *
from menu import *

LIMIT_MIN_ROUNDS = 1
LIMIT_MAX_ROUNDS = 30

def settings_option():
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
                pass
            elif option == 2:
                pass
            elif option == 3:
                max_rounds = setup_max_rounds()

        # Controlamos si el jugador no nos introduce un número como opción, mostramos un mensaje de error y volvemos a comenzar
        except ValueError:
            print()
            p.print_line(texts.TEXTS["value_error"], padding=TOTAL_WIDTH, fill_char='=')
            input("\n" + texts.TEXTS["continue"].center(TOTAL_WIDTH))

    return max_rounds

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