"""
Stylesheet for PyQt5
"""

from game.const import BUTTON_BACKGROUND_COLOR, WINDOW_BACKGROUND_COLOR, SIDE_BUTTON_BACKGROUND, LABEL_BACKGROUND

def get_style():
    """
    Creating the style for the Wdigets
    :return: {str} style; containing the style sheet
    """

    print("Loading the styles...")

    style = """
    
    QMainWindow {{
        background-color: {0};
    }}
    
    QPushButton {{
        background-color: {1};
        
    }}
    
    QPushButton#SideButton {{
        background-color: {2}
    }}
    
    QLabel {{
        background-color: {3}
    }}
    
    """ .format(WINDOW_BACKGROUND_COLOR,
                BUTTON_BACKGROUND_COLOR,
                SIDE_BUTTON_BACKGROUND,
                LABEL_BACKGROUND)



    print("Styles applied.")
    return style