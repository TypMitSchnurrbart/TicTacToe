"""
Helper methods of the one and only HORST
"""

from game.const import PLAY_BUTTON_OBJ

def make_decision_list():

    decision_list = []

    for i in range(0, 9):

        if PLAY_BUTTON_OBJ[i].get_is_occupied() is False:
            decision_list.append(i)
        else:
            pass

    return decision_list