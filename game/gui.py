"""
Creating and updating the GUI
"""

#Imports
import sys
from game.style import get_style
from game.widgets import create_play_buttons, click_event_def, build_labels, create_widgets
from game.const import GUI_TITLE, X_SCREEN, Y_SCREEN, GUI_HEIGHT, GUI_WIDTH, PATH_WINDOW_ICON
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(GUI_TITLE)
        self.setGeometry(Y_SCREEN, X_SCREEN, GUI_WIDTH, GUI_HEIGHT)
        self.setWindowIcon(QIcon(PATH_WINDOW_ICON))
        self.setStyleSheet(get_style())

        #Initialize Instances of Wdigets
        self.main_text = QLabel()
        self.turn_text = QLabel()

        #Methods of Window
        self.build_buttons()
        self.build_widgets()

        #Displaying the GUI
        self.show()

    def build_buttons(self):
        print("Creating Play Buttons...")
        create_play_buttons(self)
        click_event_def()
        print("Finished Play Button Build.")

    def build_widgets(self):
        print("Starting other Widgets...")
        build_labels(self)
        create_widgets(self)
        print("Widgets started.")


def create_gui():
    # Initialize App
    app = QApplication(sys.argv)

    #Initialize Window Object
    ttt_gui = Window()

    # System Main Loop
    print("Finished building a GUI.")
    sys.exit(app.exec())





