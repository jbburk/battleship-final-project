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
BOMB_BACKGROUND = os.path.join(file_path, "assets", "images","bomb_background.png")

#test mouse replacement for start screen and instructions
CLICKER_IMAGE = os.path.join(file_path,"assets","images","clicker.png")
#Sound file paths
TEST_SOUND_FILE = os.path.join(file_path,"assets","example_sound.wav")
BACKGROUND_MUSIC_FILE = os.path.join(file_path,"assets","battle_sound1.wav")
CANNON_FILE = os.path.join(file_path,"assets","cannon.wav")
RIFLE_FILE = os.path.join(file_path,"assets","rifle.wav")
GRENADE_FILE = os.path.join(file_path,"assets","grenade.wav")
BUZZER_FILE = os.path.join(file_path,"assets","buzzer1.wav")
MISSILE_FILE = os.path.join(file_path,"assets","missile_siren.wav")
WAR_THEME_FILE = os.path.join(file_path,"assets","wartheme.wav")
WOOSH_FILE = os.path.join(file_path,"assets","woosh1.wav")
BULLET_FILE = os.path.join(file_path,"assets","bullet.wav")


#Loaded sounds
TEST_SOUND = arcade.load_sound(TEST_SOUND_FILE)
BACKGROUND_MUSIC = arcade.load_sound(BACKGROUND_MUSIC_FILE)
CANNON = arcade.load_sound(CANNON_FILE)
RIFLE = arcade.load_sound(RIFLE_FILE)
GRENADE = arcade.load_sound(GRENADE_FILE)
BUZZER = arcade.load_sound(BUZZER_FILE)
MISSILE_SIREN = arcade.load_sound(MISSILE_FILE)
WAR_THEME = arcade.load_sound(WAR_THEME_FILE)
BULLET = arcade.load_sound(BULLET_FILE)