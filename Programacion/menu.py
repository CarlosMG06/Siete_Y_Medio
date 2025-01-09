from printing import print_menu

def start_menu(padding = 0):
    """
    Generamos el texto del menú de inicio y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) Add/Remove/Show Players                                                            
2) Settings                                                                           
3) Play Game                                                                          
4) Ranking                                                                            
5) Reports                                                                            
6) Exit  
    """
    print_menu(text, padding)

def players_submenu(padding = 0):
    """
    Generamos el texto del submenú para gestionar los jugadores y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) New Human Player                                                                 
2) New Boot                                                               
3) Show/Remove Players                                                           
4) Go back
    """
    print_menu(text, padding)

def settings_submenu(padding = 0):
    """
    Generamos el texto del submenú para las configuraciones del juego y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) Set Game Players                                                                        
2) Set Card's Deck                                                                         
3) Set Max Rounds (Default 5 Rounds)                                                       
4) Go back 
    """
    print_menu(text, padding)

def card_deck_submenu(padding = 0):
    """
    Generamos el texto del submenú para la configuración del mazo y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) ESP - ESP48                                                                        
2) ESP - ESP40                                                                         
3) POK - POK                                                       
4) Go back 
    """
    print_menu(text, padding)

def ranking_submenu(padding = 0):
    """
    Generamos el texto del submenú revisar los rankings y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) Players With More Earnings                                                            
2) Players With More Games Played                                                        
3) Players With More Minutes Played                                                      
4) Go back 
    """
    print_menu(text, padding)

def reports_submenu(padding = 0):
    """
    Generamos el texto del submenú para seleccionar los diferentes informes y lo imprimimos por pantalla
    :param padding: (int) -> Medida máxima horizontal que debe tener el título
    :return: None
    """
    text = """1) Initial card more repeated by each user, only users who have played a minimum of 3 games.                                              
2) Player who makes the highest bet per game, find the round with the highest bet.                                                          
3) Player who makes the lowest bet per game.                                                     
4) Percentage of rounds won per player in each game (%), as well as their average bet for the game.                                               
5) List of games won by Bots.                                                                    
6) Rounds won by the bank in each game.                                                          
7) Number of users have been the bank in each game.                                              
8) Average bet per game.                                                                         
9) Average bet of the first round of each game.                                                  
10) Average bet of the last round of each game.                                                   
11) Go back 
    """
    print_menu(text, padding)