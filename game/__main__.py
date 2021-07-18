from director import Director
from start_screen import StartScreen
from instruction_screen import InstructionScreen
from game_over_screen import GameOverScreen
import constants as constants
from asciimatics.screen import Screen 
import arcade

def main():
        window = arcade.Window(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
        start_screen = StartScreen()
        window.show_view(start_screen)
        
main()
arcade.run()
