from director import Director
import constants as constants
from asciimatics.screen import Screen 
import arcade


def main(screen):
        director = Director(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
        director.setup()
        
Screen.wrapper(main)
arcade.run()
