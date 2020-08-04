"""
Game procedure
"""

from game.buttons import Buttons
from game.helper import make_move

def button_clicked(button):

    print(button)
    #TODO Recognice a victory or a draw! Therefore a reset has to happen if player wants so reset!

    #Making the turns
    if (Buttons.get_round_counter() % 2) == 0:
        activ_player = "blue"
        inactiv_player = "red"

    else:
        activ_player = "red"
        inactiv_player = "blue"

    print(f"Its {inactiv_player}'s turn!")
    make_move(button, activ_player)

