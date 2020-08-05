"""
Const data base
"""

#GUI Parameters--------------------------------------------------------------------

GUI_TITLE = "TikTacToe by Alexander Müller"

X_SCREEN = 65
Y_SCREEN = 360
GUI_WIDTH = 1200
GUI_HEIGHT = 800

#PLAY_BUTTONS----------------------------------------------------------------------

PLAY_BUTTONS = ["", "", "", "", "", "", "", "", ""]
PLAY_BUTTONS_SPACE = ""
PLAY_BUTTON_OBJ = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

X_ONE_VALUE = 50
Y_ONE_VALUE = 50

PLAY_BUTTON_WIDTH = 200
PLAY_BUTTON_HEIGHT = 200

X_MARGIN = PLAY_BUTTON_WIDTH + 50
Y_MARGIN = PLAY_BUTTON_HEIGHT + 50

X_TWO_VALUE = X_ONE_VALUE + X_MARGIN
X_THR_VALUE = X_TWO_VALUE + X_MARGIN

Y_TWO_VALUE = Y_ONE_VALUE + Y_MARGIN
Y_THR_VALUE = Y_TWO_VALUE + Y_MARGIN

BUTTON_IMAGE_SIZE = 185

#Widgets---------------------------------------------------------------------------

BUTTON_ARRAY = []
RESET_BUTTON_LABEL = "New Player vs. Player Game"

LABEL_ARRAY = []
MAIN_TEXT = "         Welcome to\n a Game of TicTacToe! "
TURN_TEXT = "\t   It's {0} turn!"

#(X, Y, WIDTH, HEIGHT)
MAIN_TEXT_GEO = [772, 40, 405, 100]
TURN_TEXT_GEO = [772, 200, 405, 100]

RESET_BUTTON_GEO = [950, 400, 200, 80]

#DisplayedText---------------------------------------------------------------------

BLUE = "Blue"
RED = "Red"
DRAW_TEXT = "\t   Booring! It's a draw!"
VICTORY_TEXT = " The Game Is Over! {0} Wins!"


#Style Paramters-------------------------------------------------------------------

BUTTON_BACKGROUND_COLOR = "#323B3E"
WINDOW_BACKGROUND_COLOR = "#FF9900"
SIDE_BUTTON_BACKGROUND = "#FA6921"
LABEL_BACKGROUND = "#F8F349"

#Path------------------------------------------------------------------------------

PATH_WINDOW_ICON = "D:\GitHub\TicTacToe\game\graphics\Window_Icon.png"
PATH_RED_CROSS = "D:\GitHub\TicTacToe\game\graphics\Red_cross_edit.png"
PATH_BLUE_CIRCLE = "D:\GitHub\TicTacToe\game\graphics\Blue_circle_edit.png"
