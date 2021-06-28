import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Battleship!"
TOTAL_SHIPS = 5


#file_path = os.getcwd()
file_path = os.path.dirname(os.path.abspath(__file__))

BATTLESHIP_IMAGE = file_path +  "/assets/images/battleship_20h.png"
EMPTY_SPOT_IMAGE = file_path + "/assets/images/placeholder80x20.png"
SELECTOR_IMAGE = file_path + "/assets/images/selector.png"
DIVIDOR_IMAGE = file_path + "/assets/images/dividor.png"
BACKGROUND_IMAGE = file_path + "/assets/images/water.gif"
