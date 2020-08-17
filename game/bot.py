"""
Class of the bot
"""

from game.bot_helper import make_decision_list
from game.const import PLAY_BUTTONS, HORST

import random

class Bot:
    """
    Class describing the bot in all its cases
    """

    def __init__(self, activ=False, difficulty=0):
        """
        Constructor for a bot, default value activ
        :param activ: {bool} default is False
        """
        self.activ = activ
        self.difficulty = difficulty
        print(f"Initiating a bot as {self.activ} and level {self.difficulty}")

    def set_activ(self, activ):
        self.activ = activ

    def get_activ(self):
        return self.activ

    def set_difficulty(self, diff):

        print(f"Setting Horst to {diff}")
        self.difficulty = diff

    def get_difficulty(self):
        return self.difficulty

    def make_decision(self, bot_color):
        """
        Make decision based on difficulty and own color
        :param bot_color: {str} active color of bot
        :return: {obj} Button to press in list via index
        """

        decision_list = make_decision_list()

        #Easy Setting
        if self.difficulty == 0:

            index = decision_list[random.randint(0, len(decision_list) - 1)]
            return PLAY_BUTTONS[index]

        #Hard Setting
        elif self.difficulty == 1:
            #TODO get widget that shows mode; choosing difficulty widget; here make a hardware that looks after
            #TODO own and hostile winning conditions
            pass 
        else:
            print("Wrong diffuculty setting!")