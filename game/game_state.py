"""
Controlling the game state
"""

from game.const import PLAY_BUTTONS, PLAY_BUTTON_OBJ, LABEL_ARRAY, TURN_TEXT, BLUE
from game.buttons import Buttons
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

def set_game_default(from_start):
    """
    Prepare the game to play
    """
    from game.widgets import click_event_def

    print("Setting game to default...")

    for i in range(0, 9):
        PLAY_BUTTON_OBJ[i] = Buttons()
        if not from_start:
            PLAY_BUTTONS[i].clicked.disconnect()
            PLAY_BUTTONS[i].setIcon(QIcon())

    if not from_start:
        click_event_def()
        LABEL_ARRAY[1].setText(TURN_TEXT .format(BLUE))

    Buttons.enum_round_counter(True)

def dummy():
    """
    Small dummy because the buttons crash if not assinged to anything
    """
    return

