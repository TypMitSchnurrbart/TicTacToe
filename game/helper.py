"""
Helper File
"""

from game.const import PLAY_BUTTON_OBJ, PLAY_BUTTONS, BUTTON_IMAGE_SIZE
from game.buttons import Buttons
from PyQt5 import QtGui, QtCore

def set_game_start():
    """
    Prepare the game to play
    """

    for i in range(0, 9):
        PLAY_BUTTON_OBJ[i] = Buttons()
    Buttons.enum_round_counter(True)

    print("It`s blue turn!")


def make_move(button, activ_player):
    """
    Makes the move and sets the Button as inactive
    :param button: {str} containing object of play_buttons (list)
    :param activ_player: {str} blue or red
    :return:
    """

    click_cache = 0

    for i in range(0, 9):
        if button == str(PLAY_BUTTONS[i]):
            click_cache = i

    if PLAY_BUTTON_OBJ[click_cache].get_is_occupied() is False:
        PLAY_BUTTON_OBJ[click_cache].set_is_occupied(True)
        PLAY_BUTTON_OBJ[click_cache].set_occupied_by(activ_player)

        Buttons.enum_round_counter(False)
        change_button_look(click_cache, activ_player)
    else:
        print("This Button is already taken!")
        # TODO



def change_button_look(button_index, activ_player):
    """
    Change the Icon of the buttons that got selected
    :param button_index: {int} index of Play_buttons list containing the button objects on gui side
    :param activ_player: {str} blue or red
    :return:
    """

    if activ_player == "blue":
        PLAY_BUTTONS[button_index].setIcon(QtGui.QIcon("D:\GitHub\TicTacToe\game\graphics\Blue_circle_edit.png"))
        PLAY_BUTTONS[button_index].setIconSize(QtCore.QSize(BUTTON_IMAGE_SIZE, BUTTON_IMAGE_SIZE))

    else:
        PLAY_BUTTONS[button_index].setIcon(QtGui.QIcon("D:\GitHub\TicTacToe\game\graphics\Red_cross_edit.png"))
        PLAY_BUTTONS[button_index].setIconSize(QtCore.QSize(BUTTON_IMAGE_SIZE, BUTTON_IMAGE_SIZE))

    print(Buttons.get_round_counter())

    check_if_end(activ_player)

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
        print(f"THE GAME IS FINISHED! {activ_player} WINS!")

    #Draw Case
    if counter == 9 and winner_found is False:
        print("Its a draw!!")
    #No winner found, resturning to game
    else:
        return

    #TODO Thinking about the end? How is it communicated and how will it be reseted without restarting the gui?
    #TODO Clear Icons and reset buttons should do the trick also the round_counter



