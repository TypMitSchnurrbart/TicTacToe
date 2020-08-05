"""
Main start file
"""

#imports
from game.gui import create_gui
from game.game_state import set_game_default

if __name__ == "__main__":

    #Setting up the game environment
    set_game_default(True)

    #Creating the GUI
    print("Initializing a GUI...")
    create_gui()

