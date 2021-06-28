from director import Director
import constants as constants
from asciimatics.screen import Screen 
from input_service import Input_Service
from point import Point
from game_board import Game_Board
import arcade

def main(screen):
    user_ships = arcade.SpriteList()
    computer_ships = arcade.SpriteList()
    empty_spots = arcade.SpriteList()
    all_sprites = arcade.SpriteList()

    user_board = Game_Board()
    computer_board = Game_Board()
    beginning_selector_point = Point(50,50)
    selector = arcade.Sprite(constants.TEST_SELECTOR_IMAGE, center_x = beginning_selector_point.get_x(),center_y = beginning_selector_point.get_y())
    all_sprites.append(selector)

    middle_x = constants.SCREEN_WIDTH / 2

    for x in range(50,450,50):
        for y in range(100,600,50):
            #user side of game board
            empty_user_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = x, center_y = constants.SCREEN_HEIGHT - y, image_width=30,image_height=20)
            empty_spots.append(empty_user_spot)
            all_sprites.append(empty_user_spot)

            #Computer side of board
            empty_computer_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = x + 500,center_y = constants.SCREEN_HEIGHT - y, image_width = 30, image_height = 20)
            empty_spots.append(empty_computer_spot)
            all_sprites.append(empty_computer_spot)

        dividor = arcade.Sprite(constants.DIVIDOR_IMAGE,center_x = 480, center_y = 470)
        all_sprites.append(dividor)

        arcade.set_background_color(arcade.color.AQUA)
        background_loaded = arcade.load_texture(constants.BACKGROUND_IMAGE)

        selector = arcade.Sprite(constants.TEST_SELECTOR_IMAGE, center_x = 200, center_y = 400)
        all_sprites.append(selector)

        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,background_loaded)
        
        for sprite in all_sprites:
            sprite.draw()
            


        input_service = Input_Service(screen,selector)
        #output_service = OutputService(screen)
        director = Director(input_service,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
        #director.start_game()


    
Screen.wrapper(main)
arcade.run()
