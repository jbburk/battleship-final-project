import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Battleship!"
TOTAL_SHIPS = 5

#Board dimensions
ROW_COUNT = 8
COLUMN_COUNT = 8

#Variables for image size and margin
WIDTH = 30
HEIGHT = 20
MARGIN = 50

#Info message variables
MESSAGE_START_X = 400
MESSAGE_START_Y = 740
MESSAGE_FONT_SIZE = 15
#Image paths
file_path = os.path.dirname(os.path.abspath(__file__))
BATTLESHIP_IMAGE = os.path.join(file_path,"assets","images","battleship_20h.png")
EMPTY_SPOT_IMAGE = os.path.join(file_path, "assets", "images", "placeholder80x20.png") 
SELECTOR_IMAGE =  os.path.join(file_path, "assets", "images", "selector.png") 
DIVIDOR_IMAGE =  os.path.join(file_path, "assets", "images", "dividor.png") 
BACKGROUND_IMAGE = os.path.join(file_path, "assets", "images","water.gif") 
TEST_PLACE_HOLDER = os.path.join(file_path, "assets", "images","placeholder90x20.png")