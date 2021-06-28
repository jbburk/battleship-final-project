import arcade
from game_board import Game_Board
from point import Point
import constants

class Director(arcade.Window):
    def __init__(self,input_service,width,height,title):
        super().__init__(width,height,title)
        
    """
    def on_update(self):
        for sprite in self.all_sprites:
            sprite.draw()"""







