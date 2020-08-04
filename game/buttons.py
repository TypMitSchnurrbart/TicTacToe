"""
Class that describes the buttons
"""

class Buttons():

    round_counter = 0

    def __init__(self, is_occupied=False, occupied_by=None):

        self.is_occupied = is_occupied
        self.occupied_by = occupied_by


    def get_is_occupied(self):
        return self.is_occupied

    def set_is_occupied(self, occupation):
            self.is_occupied = occupation

    def get_occupied_by(self):
        return self.occupied_by

    def set_occupied_by(self, player):
        self.occupied_by = player

    @staticmethod
    def enum_round_counter(reset):

        if reset is  False:
            Buttons.round_counter += 1
        else:
            Buttons.round_counter = 0

    @staticmethod
    def get_round_counter():
        return Buttons.round_counter


