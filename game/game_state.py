"""
Controlling the game state
"""

from game.const import PLAY_BUTTONS, PLAY_BUTTON_OBJ, LABEL_ARRAY, TURN_TEXT, BLUE, HORST
from game.buttons import Buttons
from game.bot import Bot
from PyQt5.QtGui import QIcon

def game_standby():
    """
    Setting the game to a stanby mode; so no input possible via the play_buttons
    :return:
    """
    for i in range(0, 9):
        PLAY_BUTTONS[i].clicked.disconnect()
        PLAY_BUTTONS[i].clicked.connect(dummy)
    return

def set_game_default(from_start, with_bot=False):
    """
    Prepare the game to play
    """
    from game.widgets import click_event_def

    print("Setting game to default...")

    #Deleting the Bot List
    if not from_start:
        diff_cache = HORST[0].get_difficulty()
    HORST.clear()

    #Clearing the game sheet
    for i in range(0, 9):
        PLAY_BUTTON_OBJ[i] = Buttons()
        if not from_start:
            PLAY_BUTTONS[i].clicked.disconnect()
            PLAY_BUTTONS[i].setIcon(QIcon())

    #Set Start Environment
    if not from_start:
        click_event_def()
        LABEL_ARRAY[1].setText(TURN_TEXT .format(BLUE)) #TODO Here if starter can be choosen

    #Reset Round Counter to 0
    Buttons.enum_round_counter(True)

    if with_bot:
        #Create a Activ Horst
        HORST.append(Bot(True, diff_cache))
    else:
        #Inactiv Horst
        HORST.append(Bot())


def dummy():
    """
    Small dummy because the buttons crash if not assinged to anything
    """
    return

