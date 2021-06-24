from director import Director
import constants as constants
from asciimatics.screen import Screen 
from input_service import Input_Service
import arcade

def main(screen):
    input_service = Input_Service(screen)
    #output_service = OutputService(screen)
    director = Director(input_service,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
    #director.start_game()
    
    
Screen.wrapper(main)
arcade.run()
