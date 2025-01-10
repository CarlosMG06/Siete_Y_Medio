# Constantes necesarias para la impresión del título
TOTAL_WIDTH = 128               # Espacio total de la línea, desde el inicio de la línea
HALF_WIDTH = 64                 # Mitad del espacio total
LEFT_SPACE_OPTIONS = 51         # Espacio necesario para dejar espacio al inicio de la línea
LEFT_SPACE_OPTIONS_REPORTS = 16 # Espacio necesario para dejar espacio al inicio de la línea para el submenú de reportes
MIN_OPTION = 1                  # Mínima opción a comprobar

# Diferents opciones máximas a comprobar
MAX_OPTION_1 = 4
MAX_OPTION_2 = 6
MAX_OPTION_3 = 11

# Márgenes para las columnas al mostrar los jugadores (Total debe ser 63, mitad - 1)
SP_COLUMN_ID = 13
SP_COLUMN_NAME = 35
SP_COLUMN_TYPE = 15

# Márgenes para los diferentes reportes
# Hacemos un +3 para tener los mismos espacios al principio que al final
RP_ID_GAME = 10
RP_ID_PLAYER = 15
RP_MAX_BET = 15
RP_MIN_BET = 15
RP_ROUNDS = 10
RP_AVG_BET = 16
RP_WIN_ROUNDS = 16
RP_PCE_WON = 18

RP_2_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_MAX_BET + 3
RP_3_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_MIN_BET + 3
RP_4_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_ROUNDS + RP_AVG_BET + RP_WIN_ROUNDS + RP_PCE_WON + 3