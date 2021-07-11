import os
import arcade

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600
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


file_path = os.path.dirname(os.path.abspath(__file__))
#Image paths
BATTLESHIP_IMAGE = os.path.join(file_path,"assets","images","battleship_30x20.png")
EMPTY_SPOT_IMAGE = os.path.join(file_path, "assets", "images", "placeholder80x20.png") 
SELECTOR_IMAGE =  os.path.join(file_path, "assets", "images", "selector.png") 
DIVIDOR_IMAGE =  os.path.join(file_path, "assets", "images", "rock-dividor.png") 
BACKGROUND_IMAGE = os.path.join(file_path, "assets", "images","water.gif") 
TEST_PLACE_HOLDER = os.path.join(file_path, "assets", "images","placeholder90x20.png")

#test mouse replacement for start screen and instructions
CLICKER_IMAGE = os.path.join(file_path,"assets","images","clicker.png")
#Sound file paths
TEST_SOUND_FILE = os.path.join(file_path,"assets","example_sound.wav")


#Loaded sounds
TEST_SOUND = arcade.load_sound(TEST_SOUND_FILE)