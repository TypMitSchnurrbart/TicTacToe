"""
Creating the widgets of the GUI
"""

from game.const import PLAY_BUTTONS, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT, X_ONE_VALUE, Y_ONE_VALUE
from game.const import Y_TWO_VALUE, Y_THR_VALUE, X_TWO_VALUE, X_THR_VALUE, PLAY_BUTTONS_SPACE
from game.process_button_clicked import *
from PyQt5.QtWidgets import QPushButton
from functools import partial

def create_buttons(window):

    for i in range(0, 9):
        PLAY_BUTTONS[i] = QPushButton("{0}".format(PLAY_BUTTONS_SPACE), window)

def move_buttons():

    PLAY_BUTTONS[0].setGeometry(X_ONE_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[1].setGeometry(X_TWO_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[2].setGeometry(X_THR_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[3].setGeometry(X_ONE_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[4].setGeometry(X_TWO_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[5].setGeometry(X_THR_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[6].setGeometry(X_ONE_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[7].setGeometry(X_TWO_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[8].setGeometry(X_THR_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)

def click_event_def():

    for i in range(0, 9):
        PLAY_BUTTONS[i].clicked.connect(partial(button_clicked, str(PLAY_BUTTONS[i])))
