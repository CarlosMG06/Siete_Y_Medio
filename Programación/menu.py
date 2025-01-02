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