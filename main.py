"""
Main start file
"""

#imports
from game.gui import create_gui
from game.helper import set_game_start

if __name__ == "__main__":

    #Creating the GUI
    set_game_start()
    print("Initializing a GUI...")
    create_gui()

