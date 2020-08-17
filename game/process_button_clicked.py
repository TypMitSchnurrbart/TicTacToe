"""
Game procedure
"""

from game.buttons import Buttons
from game.helper import make_move
from game.const import BLUE, RED, HORST

def play_button_clicked(button):

    print(button)

    #Case if Horst is activ or not
    if HORST[0].get_activ() is False:

        #Making the turns, BLUE starts
        if (Buttons.get_round_counter() % 2) == 0:
            activ_player = BLUE
            inactiv_player = RED

        else:
            activ_player = RED
            inactiv_player = BLUE

        make_move(button, activ_player, inactiv_player)

    else:
        round_counter = Buttons.get_round_counter()
        #Default blue player starts, red is bot
        if (round_counter % 2) == 0:

            #First Player makes move
            activ_player = BLUE
            inactiv_player = RED

            game_over, button_taken = make_move(button, activ_player, inactiv_player)

            if round_counter != 8 and not game_over and not button_taken:

                #Bot makes his moves
                activ_player = RED
                inactiv_player = BLUE

                button = str(HORST[0].make_decision(activ_player))  # give active_player to get choosable

                make_move(button, activ_player, inactiv_player)

        else:
            exit("Round counter broken...")





