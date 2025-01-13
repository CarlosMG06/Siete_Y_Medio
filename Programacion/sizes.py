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
MAX_OPTION_4 = 3

# Márgenes para las columnas al mostrar los jugadores (Total debe ser 63, mitad - 1)
SP_COLUMN_ID = 13
SP_COLUMN_NAME = 35
SP_COLUMN_TYPE = 15

# Márgenes para los diferentes reportes
# Hacemos un +X para tener los mismos espacios al principio que al final
PADDING_ID_PLAYER = 6
PADDING_ID_GAME = 3

RP_ID_GAME = 10
RP_ID_PLAYER = 15
RP_MAX_BET = 15
RP_MIN_BET = 15
RP_ROUNDS = 10
RP_AVG_BET = 16
RP_WIN_ROUNDS = 16
RP_PCE_WON = 18
RP_SUIT = 14
RP_INITIAL_CARD = 22
RP_TIMES_REPEATED = 18
RP_TOTAL_GAMES = 14
RP_POINTS_WON = 14
RP_USER_BEEN_BANK = 28

RP_1_WIDTH = RP_ID_PLAYER + RP_SUIT + RP_INITIAL_CARD + RP_TIMES_REPEATED + RP_TOTAL_GAMES + PADDING_ID_PLAYER
RP_2_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_MAX_BET + PADDING_ID_GAME
RP_3_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_MIN_BET + PADDING_ID_GAME
RP_4_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_ROUNDS + RP_AVG_BET + RP_WIN_ROUNDS + RP_PCE_WON + PADDING_ID_GAME
RP_5_WIDTH = RP_ID_GAME + RP_POINTS_WON + PADDING_ID_GAME
RP_61_WIDTH = RP_ID_GAME + RP_ID_PLAYER + RP_WIN_ROUNDS + PADDING_ID_GAME
RP_62_WIDTH = RP_ID_GAME + RP_WIN_ROUNDS + PADDING_ID_GAME
RP_7_WIDTH = RP_ID_GAME + RP_USER_BEEN_BANK + PADDING_ID_GAME
RP_8_WIDTH = RP_ID_GAME + RP_AVG_BET + PADDING_ID_GAME
RP_9_WIDTH = RP_ID_GAME + RP_AVG_BET + PADDING_ID_GAME
RP_10_WIDTH = RP_ID_GAME + RP_ROUNDS + RP_AVG_BET + PADDING_ID_GAME