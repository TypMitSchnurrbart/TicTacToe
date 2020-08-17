"""
Helper File
"""

from game.const import PLAY_BUTTON_OBJ, PLAY_BUTTONS, BUTTON_IMAGE_SIZE, BLUE, RED, LABEL_ARRAY, DRAW_TEXT, TURN_TEXT
from game.const import VICTORY_TEXT, PATH_BLUE_CIRCLE, PATH_RED_CROSS
from game.buttons import Buttons
from game.game_state import game_standby
from PyQt5 import QtGui, QtCore

def make_move(button, activ_player, inactiv_player):
    """
    Makes the move and sets the Button as inactive
    :param button: {str} containing object of play_buttons (list)
    :param activ_player: {str} blue or red
    :param inactiv_player: {string} blue or red
    :return:
    """

    click_cache = 0
    button_taken = False
    game_over = False

    #Searching for the right index to button
    for i in range(0, 9):
        if button == str(PLAY_BUTTONS[i]):
            click_cache = i

    #If buttons not already taken, set it taken
    if PLAY_BUTTON_OBJ[click_cache].get_is_occupied() is False:
        PLAY_BUTTON_OBJ[click_cache].set_is_occupied(True)
        PLAY_BUTTON_OBJ[click_cache].set_occupied_by(activ_player)

        #Roundcounter + 1 and changing button graphic; also check if winner
        Buttons.enum_round_counter(False)
        game_over = change_button_look(click_cache, activ_player)

        #Only Set Turn Text to next player if game isnt already over
        if not game_over:
            LABEL_ARRAY[1].setText(TURN_TEXT.format(inactiv_player))

    #If buttons is already taken
    else:
        print("This Button is already taken!")
        button_taken = True

    return game_over, button_taken

def change_button_look(button_index, activ_player):
    """
    Change the Icon of the buttons that got selected
    :param button_index: {int} index of Play_buttons list containing the button objects on gui side
    :param activ_player: {str} blue or red
    :return:
    """

    #Blue Circle is getting set
    if activ_player == BLUE:
        PLAY_BUTTONS[button_index].setIcon(QtGui.QIcon(PATH_BLUE_CIRCLE))
        PLAY_BUTTONS[button_index].setIconSize(QtCore.QSize(BUTTON_IMAGE_SIZE, BUTTON_IMAGE_SIZE))

    #Red Cross is getting set
    elif activ_player == RED:
        PLAY_BUTTONS[button_index].setIcon(QtGui.QIcon(PATH_RED_CROSS))
        PLAY_BUTTONS[button_index].setIconSize(QtCore.QSize(BUTTON_IMAGE_SIZE, BUTTON_IMAGE_SIZE))

    #Check round counter in console
    print(Buttons.get_round_counter())

    #Check if game is over
    game_over = check_if_end(activ_player)

    return game_over

def check_if_end(activ_player):
    """
    Routine to get information about the end of the game
    :param activ_player: {str} red or blue
    :return:
    """

    counter = Buttons.get_round_counter()
    winner_found = False

    #Find the winner, first possbile after 5 round
    if counter >= 5:
        if PLAY_BUTTON_OBJ[4].get_occupied_by() == activ_player:
            if PLAY_BUTTON_OBJ[3].get_occupied_by() == PLAY_BUTTON_OBJ[5].get_occupied_by() == activ_player:
                winner_found = True
            if PLAY_BUTTON_OBJ[1].get_occupied_by() == PLAY_BUTTON_OBJ[7].get_occupied_by() == activ_player:
                winner_found = True
            if PLAY_BUTTON_OBJ[0].get_occupied_by() == PLAY_BUTTON_OBJ[8].get_occupied_by() == activ_player:
                winner_found = True
            if PLAY_BUTTON_OBJ[6].get_occupied_by() == PLAY_BUTTON_OBJ[2].get_occupied_by() == activ_player:
                winner_found = True

        if PLAY_BUTTON_OBJ[0].get_occupied_by() == activ_player:
            if PLAY_BUTTON_OBJ[3].get_occupied_by() == PLAY_BUTTON_OBJ[6].get_occupied_by() == activ_player:
                winner_found = True
            if PLAY_BUTTON_OBJ[1].get_occupied_by() == PLAY_BUTTON_OBJ[2].get_occupied_by() == activ_player:
                winner_found = True

        if PLAY_BUTTON_OBJ[8].get_occupied_by() == activ_player:
            if PLAY_BUTTON_OBJ[7].get_occupied_by() == PLAY_BUTTON_OBJ[6].get_occupied_by() == activ_player:
                winner_found = True
            if PLAY_BUTTON_OBJ[5].get_occupied_by() == PLAY_BUTTON_OBJ[2].get_occupied_by() == activ_player:
                winner_found = True

    if winner_found is True:
        LABEL_ARRAY[1].setText(VICTORY_TEXT .format(activ_player))
        game_standby()
        return True

    #Draw Case
    elif counter == 9 and winner_found is False:
        LABEL_ARRAY[1].setText(DRAW_TEXT)
        game_standby()
        return True

    #No winner found, returning to game
    else:
        return False

