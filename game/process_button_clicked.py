"""
Game procedure
"""

from game.buttons import Buttons
from game.helper import make_move
from game.const import LABEL_ARRAY, BLUE, RED, TURN_TEXT

def play_button_clicked(button):

    print(button)


    #Making the turns, BLUE starts TODO maybe chooseable who starts?
    if (Buttons.get_round_counter() % 2) == 0:
        activ_player = BLUE
        inactiv_player = RED

    else:
        activ_player = RED
        inactiv_player = BLUE

    make_move(button, activ_player, inactiv_player)

