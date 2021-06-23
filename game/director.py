import arcade
from game.game_board import Game_Board
from game.point import Point

from game import constants

import os #for now
print(os.getcwd())
file_path = os.getcwd()



class Director(arcade.Window):
    def __init__(input_service,self,width,height,title):
        super().__init__(width,height,title)
        self.user_board = Game_Board()
        self.computer_board = Game_Board()
        self.beginning_selector_point = Point(50,50)
  
        self.user_ships = arcade.SpriteList()
        self.computer_ships = arcade.SpriteList()
        self.empty_spots = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.divider_sprite = arcade.Sprite()

        middle_x = constants.SCREEN_WIDTH / 2

        #testing sprite
        first_empty_spot = arcade.Sprite(constants.BATTLESHIP_IMAGE, center_x = 350, center_y = 400)
        first_empty_spot.draw()

        #arcade.draw_rectangle_filled(,center_x=middle_x,center_y=0, width = 10, height=constants.SCREEN_HEIGHT, color=arcade.color.BLUE)
"""
        self.user_spot_coords = []
        for x in range(50,350,50):
            for y in range(0,400,50):
                self.user_spot_coords.append([x,y])
        
        for item in self.user_spot_coords:
            x = item[0]
            y = item[1]

            new_spot_point = Point(x,y)

            new_spot = arcade.Sprite(constants.BATTLESHIP_IMAGE,center_x = x,center_y = y, )
            self.empty_spots.append(new_spot)
            new_spot.draw()
            """
        







