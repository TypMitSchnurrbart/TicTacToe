"""
Stylesheet for PyQt5
"""

from game.const import BUTTON_BACKGROUND_COLOR, WINDOW_BACKGROUND_COLOR

def get_style():
    """
    Creating the style for the Wdigets
    :return: {str} style; containing the style sheet
    """

    print("Loading the styles...")

    style = """
    
    QMainWindow {{
        background-color: {1};
    }}
    
    QPushButton {{
        background-color: {0};
        
    }}
    
    """ .format(BUTTON_BACKGROUND_COLOR, WINDOW_BACKGROUND_COLOR)

    print("Styles applied.")
    return style