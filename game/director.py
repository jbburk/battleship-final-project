import arcade
import random
import sys
from game_board import Game_Board
from game_status import Game_Status
from point import Point
from output_service import Output_Service
from grid_spot import Grid_Spot
from shot import attacks
import constants

from game_over_screen import GameOverScreen

#To-Do:
#1. Update the selector to handle checking collisions with empty spaces on each side of the board. 
#2. Add functionality for placing ships along with hits and misses on each side of board.

class Director(arcade.View):
    def __init__(self):
        super().__init__()

        self.output_service = Output_Service()
        
        #Variable to hold the current output shown to the user via text
        self.current_message = ""

        self.ship_mouse = arcade.Sprite(constants.BATTLESHIP_IMAGE,center_x=constants.SCREEN_WIDTH/2, center_y=constants.SCREEN_HEIGHT/2)
        self.fire_mouse = arcade.Sprite(constants.FIRE_IMAGE, center_x=constants.SCREEN_WIDTH/2, center_y=constants.SCREEN_HEIGHT/2)

        self.current_mouse = "ship"

        self.current_mouse_sprite = self.ship_mouse
    
        self.winner = None
        self.game_over = False

        #Setting up Sprite lists for all game Sprites
        self.user_board_coordinates = [] #List just to hold the values of each type of placement, ie: empty,
        self.computer_board_coordinates = [] #ship, hit, miss.

        self.user_sprite_coordinates = None #List containing all sprites on the user's side of the board
        self.computer_sprite_coordinates = None #List containing all sprites on the computer's side of the board
        self.all_sprites = None #List containing all sprites

        #Establishing instances of the game board class to handle each side's game board.
        self.user_board = Game_Board()
        self.computer_board = Game_Board()

        #Establishing instance of the game status class to handle the flow of the game
        self.game_status = Game_Status()

        #Establishing instance of class
        self.attacks = attacks(self.user_board_coordinates)

    #def setup(self):
    def on_show(self):
        #Background sounds/music 
        arcade.play_sound(constants.BACKGROUND_MUSIC)
        
        #self.mouse = arcade.Sprite(constants.CLICKER_IMAGE, center_x=700,center_y=700,image_height=20,image_width=12)
        
        self.user_ships = arcade.SpriteList()
        self.computer_ships = []
        self.user_sprite_coordinates = arcade.SpriteList()
        self.computer_sprite_coordinates = arcade.SpriteList()

        self.all_sprites = arcade.SpriteList()
        
        #Creating each coordinate's sprite for each side of the board
        for x in range(50,350,50):
            for y in range(100,400,50):
                #User side of game board
                empty_user_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = x, center_y = constants.SCREEN_HEIGHT - y, image_width=constants.WIDTH,image_height=constants.HEIGHT)
                self.user_sprite_coordinates.append(empty_user_spot)
                self.user_board_coordinates.append("e")
                self.all_sprites.append(empty_user_spot)

                #Computer side of board
                empty_computer_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = x + 400,center_y = constants.SCREEN_HEIGHT - y, image_width=constants.WIDTH,image_height=constants.HEIGHT)
                self.computer_sprite_coordinates.append(empty_computer_spot)
                self.computer_board_coordinates.append("e")
                self.all_sprites.append(empty_computer_spot)
                
        #Creating the center dividor between the sides of the board
        self.dividor = arcade.Sprite(constants.DIVIDOR_IMAGE,center_x = 375, center_y = constants.SCREEN_HEIGHT - 230, image_height=350,image_width = 20)
        self.all_sprites.append(self.dividor)


        #Setting the game's background
        arcade.set_background_color(arcade.color.AQUA)
        self.background_loaded = arcade.load_texture(constants.BACKGROUND_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background_loaded)

    def on_mouse_motion(self,x,y,dx,dy):
        """self.mouse.center_x = x
        self.mouse.center_y = y"""

        self.current_mouse_sprite.center_x = x
        self.current_mouse_sprite.center_y = y

    def on_mouse_press(self,x,y,button,modifiers):
        if not self.game_over:
            if button == arcade.MOUSE_BUTTON_LEFT:
                #Checking for clicks on sprites
                if self.game_status.is_placing_user_ships(): #If the user is placing ships 
                    for spot in self.user_sprite_coordinates: #Looping through all sprites themselves
                        spot_index = self.user_sprite_coordinates.index(spot)
                        if self.current_mouse_sprite.collides_with_sprite(spot): 
                            if spot_index not in self.user_ships: 
                                self.place_user_ship(spot)
                                self.user_board_coordinates[spot_index] = "s"
                                self.game_status.add_placed_ship()
                                self.current_message = f"Placed ship # {self.game_status.user_ships_placed}"
                                
                                #Sound effect for placing ship on user side
                                arcade.play_sound(constants.TEST_SOUND)
                                

                elif self.game_status.get_current_turn() == "user":
                    for spot in self.computer_sprite_coordinates:
                        if self.current_mouse_sprite.collides_with_sprite(spot):
                            shot_result = self.attacks.check_shot(self.computer_sprite_coordinates.index(spot),self.computer_board_coordinates)
                            if shot_result == "hit!":
                                spot.color = arcade.color.GREEN
                                self.computer_board_coordinates[self.computer_sprite_coordinates.index(spot)] = "h"
                                self.game_status.computer_ships_placed -= 1
                                self.current_message = "You got a hit!"

                                #Sound effect for a user hit
                                arcade.play_sound(constants.GRENADE)

                            if shot_result == "miss!":
                                spot.color = arcade.color.RED
                                self.computer_board_coordinates[self.computer_sprite_coordinates.index(spot)] = "m"
                                self.game_status.switch_turns()
                                self.current_message = "You missed! It's the Computer's turn!"

                                #Sound effect for user miss
                                arcade.play_sound(constants.BULLET)

                            if shot_result == "already fired there!":
                                self.current_message = "You already fired there! Try again! "
                        
                                #Sound effect for if the user fires somewhere they've already fired - could take out later
                                arcade.play_sound(constants.BUZZER)

    def on_update(self,delta_time):

        if self.game_status.get_current_turn() == "user":
            self.current_mouse_sprite = self.fire_mouse

        self.check_for_win()
        self.output_service.clear_screen()
        self.output_service.draw_all_sprites(self.all_sprites)
        
        #Creating labels for each side of board
        arcade.draw_text("Allies",start_x = 130, start_y = constants.SCREEN_HEIGHT - 60, color=arcade.color.BLACK, font_size=40, )
        arcade.draw_text("Enemies",start_x = 490, start_y = constants.SCREEN_HEIGHT - 60, font_size=40, color=arcade.color.RED)

        #Message label 
        arcade.draw_text(self.current_message,start_x = constants.MESSAGE_START_X, start_y = constants.MESSAGE_START_Y, color=arcade.color.BLUE, font_size=constants.MESSAGE_FONT_SIZE)

        if self.game_status.is_placing_computer_ships():
            while self.game_status.computer_ships_placed != 5:
                new_ship_coord = random.randint(0,len(self.computer_sprite_coordinates))                
                if new_ship_coord not in self.computer_ships:
                    self.computer_board_coordinates[new_ship_coord] = "s"
                    self.computer_ships.append(new_ship_coord)
                    self.game_status.add_placed_ship()

        if self.game_status.get_current_turn() == "computer":
            #Actual shot attempt
            attack_result, spot = self.attacks.computer_shot(self.user_board_coordinates)
            if attack_result == "hit!":
                new_x = self.user_sprite_coordinates[spot].center_x
                new_y = self.user_sprite_coordinates[spot].center_y
                self.user_sprite_coordinates[spot] = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = new_x, center_y = new_y, image_width=constants.WIDTH,image_height=constants.HEIGHT)
                self.user_sprite_coordinates[spot].color = arcade.color.GREEN
                self.all_sprites[spot] = self.user_sprite_coordinates[spot]
                self.user_board_coordinates[spot] = "h"
                
                self.game_status.user_ships_placed -= 1

                #Sound effect for a computer hit
                #arcade.play_sound(constants.SONG)

            elif attack_result == "miss!":
                self.user_sprite_coordinates[spot].color = arcade.color.RED
                self.user_board_coordinates[spot] = "m"
                self.game_status.switch_turns()

                #Sound effect for a computer miss
                #arcade.play_sound(constants.SONG)
        
        self.current_mouse_sprite.draw()
        
        
        #self.mouse.draw()

    def place_user_ship(self,sprite):
        sprite.color = arcade.color.BLUE
        new_center_x = sprite.center_x
        new_center_y = sprite.center_y
        
        sprite_list_index = self.user_sprite_coordinates.index(sprite)
        battleship = arcade.Sprite(constants.BATTLESHIP_IMAGE, center_x=new_center_x, center_y=new_center_y, image_width=constants.WIDTH, image_height=constants.HEIGHT)
        self.user_sprite_coordinates[sprite_list_index] = battleship
        self.user_board_coordinates[sprite_list_index] = sprite_list_index
        self.user_ships.append(battleship)
        self.all_sprites.remove(sprite)
        self.all_sprites.append(battleship)

    def check_for_win(self):
        computer_ships = self.game_status.computer_ships_placed
        user_ships = self.game_status.user_ships_placed
        if not self.game_status.placing_user_ships and not self.game_status.placing_computer_ships:
            if computer_ships == 0:
                self.winner = "user"
                self.game_over = True

            elif user_ships == 0:
                self.winner = "computer"
                self.game_over = True

            if self.game_over:
                if self.winner == "user":
                    #Sound effect for a win
                    arcade.play_sound(constants.WAR_THEME)

                else:
                    #Sound effect for a loss
                    arcade.play_sound(constants.MISSILE_SIREN)
                
                self.game_over_screen = GameOverScreen(self,self.winner)
                self.window.show_view(self.game_over_screen)

    #for testing purposes
    def on_key_press(self,symbol:int, modifiers:int):
        if symbol == arcade.key.Q:
            self.game_over_screen = GameOverScreen(self,self.winner)
            self.window.show_view(self.game_over_screen)