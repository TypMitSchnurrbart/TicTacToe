"""
Creating and updating the GUI
"""

#Imports
import sys
from game.style import get_style
from game.widgets_play_buttons import create_buttons, move_buttons, click_event_def
from game.const import GUI_TITLE, X_SCREEN, Y_SCREEN, GUI_HEIGHT, GUI_WIDTH
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("{0}" .format(GUI_TITLE))
        self.setGeometry(Y_SCREEN, X_SCREEN, GUI_WIDTH, GUI_HEIGHT)
        self.setStyleSheet(get_style())

        #Methods of Window
        self.build_buttons()

        #Displaying the GUI
        self.show()

    def build_buttons(self):
        print("Creating Play Buttons...")
        create_buttons(self)
        move_buttons()
        click_event_def()
        print("Finished Play Button Build.")

def create_gui():

    # Initialize App
    app = QApplication(sys.argv)

    #Initialize Window Object
    window = Window()

    # System Main Loop
    print("Finished building a GUI.")
    sys.exit(app.exec())





