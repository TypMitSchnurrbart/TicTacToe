"""
Creating the widgets of the GUI
"""

from game.const import *
from game.process_button_clicked import *
from game.game_state import set_game_default
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from functools import partial

def create_play_buttons(ttt_gui):

    for i in range(0, 9):
        PLAY_BUTTONS[i] = QPushButton(PLAY_BUTTONS_SPACE, ttt_gui)

    PLAY_BUTTONS[0].setGeometry(X_ONE_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[1].setGeometry(X_TWO_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[2].setGeometry(X_THR_VALUE, Y_ONE_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[3].setGeometry(X_ONE_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[4].setGeometry(X_TWO_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[5].setGeometry(X_THR_VALUE, Y_TWO_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[6].setGeometry(X_ONE_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[7].setGeometry(X_TWO_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
    PLAY_BUTTONS[8].setGeometry(X_THR_VALUE, Y_THR_VALUE, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)

def create_widgets(ttt_gui):

    # Create first functionally Button
    BUTTON_ARRAY.append(QPushButton(RESET_BUTTON_LABEL, ttt_gui))
    BUTTON_ARRAY[0].setGeometry(RESET_BUTTON_GEO[0], RESET_BUTTON_GEO[1], RESET_BUTTON_GEO[2], RESET_BUTTON_GEO[3])
    BUTTON_ARRAY[0].setObjectName("SideButton")
    BUTTON_ARRAY[0].clicked.connect(partial(set_game_default, bool(False)))

def click_event_def():

    for i in range(0, 9):
        PLAY_BUTTONS[i].clicked.connect(partial(play_button_clicked, str(PLAY_BUTTONS[i])))

def build_labels(ttt_gui):

    #Filling WIDGET_ARRAY with the Objects
    LABEL_ARRAY.append(QLabel(MAIN_TEXT, ttt_gui))
    LABEL_ARRAY.append(QLabel(TURN_TEXT .format(BLUE), ttt_gui)) #TODO Choosing who is starting!!!

    #Placing the WIDGETS (X, Y, WIDTH, HEIGHT)
    LABEL_ARRAY[0].setGeometry(MAIN_TEXT_GEO[0], MAIN_TEXT_GEO[1], MAIN_TEXT_GEO[2], MAIN_TEXT_GEO[3])
    LABEL_ARRAY[0].setFont(QFont("Helvetica", 30))

    LABEL_ARRAY[1].setGeometry(TURN_TEXT_GEO[0], TURN_TEXT_GEO[1], TURN_TEXT_GEO[2], TURN_TEXT_GEO[3])
    LABEL_ARRAY[1].setFont(QFont("Helvetica", 20))