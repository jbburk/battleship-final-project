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
        """first_empty_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = 350, center_y = 600)
        first_empty_spot.draw()"""

        for x in range(50,450,50):
            for y in range(100,600,50):
                #user side of game board
                empty_user_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = x, center_y = constants.SCREEN_HEIGHT - y, image_width=30,image_height=20)
                self.empty_spots.append(empty_user_spot)
                self.all_sprites.append(empty_user_spot)

                #Computer side of board
                empty_computer_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = x + 500,center_y = constants.SCREEN_HEIGHT - y, image_width = 30, image_height = 20)
                self.empty_spots.append(empty_computer_spot)
                self.all_sprites.append(empty_computer_spot)



        self.dividor = arcade.Sprite(constants.DIVIDOR_IMAGE,center_x = 480, center_y = 470)
        self.all_sprites.append(self.dividor)

        arcade.set_background_color(arcade.color.AQUA)
        self.background_loaded = arcade.load_texture(constants.BACKGROUND_IMAGE)


        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background_loaded)
        

    def on_update(self):
        for sprite in self.all_sprites:
            sprite.draw()







