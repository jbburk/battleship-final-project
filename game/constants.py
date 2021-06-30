import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Battleship!"
TOTAL_SHIPS = 5

#file_path = os.getcwd()
file_path = os.path.dirname(os.path.abspath(__file__))

ROW_COUNT = 8
COLUMN_COUNT = 8

#Variables for image size and margin
WIDTH = 30
HEIGHT = 20
MARGIN = 50


BATTLESHIP_IMAGE = os.path.join(file_path,"assets","images","battleship_20h.png")
EMPTY_SPOT_IMAGE = os.path.join(file_path, "assets", "images", "placeholder80x20.png") #file_path + "/assets/images/placeholder80x20.png"
SELECTOR_IMAGE =  os.path.join(file_path, "assets", "images", "selector.png") #file_path + "/assets/images/selector.png"
DIVIDOR_IMAGE =  os.path.join(file_path, "assets", "images", "dividor.png") #file_path + "/assets/images/dividor.png"
BACKGROUND_IMAGE = os.path.join(file_path, "assets", "images","water.gif") #file_path + "/assets/images/water.gif"