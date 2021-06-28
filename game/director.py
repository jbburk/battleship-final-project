import arcade
from game_board import Game_Board
from point import Point
from output_service import Output_Service
import constants
#for now
import tkinter.messagebox as tk_mb

class Director(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    
        self.output_service = Output_Service()

        self.user_ships = arcade.SpriteList()
        self.computer_ships = arcade.SpriteList()
        self.empty_spots = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.user_board = Game_Board()
        self.computer_board = Game_Board()

    def setup(self):
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

            self.selector = arcade.Sprite(constants.SELECTOR_IMAGE)
            self.all_sprites.append(self.selector)

            arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background_loaded)

    def on_mouse_press(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.selector.center_x = x
            self.selector.center_y = y
    
    def on_update(self,delta_time):
        self.output_service.clear_screen()
        self.output_service.draw_all_sprites(self.all_sprites)







