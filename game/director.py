import arcade
from game_board import Game_Board
from game_status import Game_Status
from point import Point
from output_service import Output_Service
import constants

#To-Do:
#1. Update the selector to handle checking collisions with empty spaces on each side of the board. 
#2. Add functionality for placing ships along with hits and misses on each side of board.

class Director(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)


        #TESTING VARIALBE 
        self.touching = False


        self.output_service = Output_Service()

        #Setting up Sprite lists for all game Sprites
        self.user_ships = None
        self.computer_ships = None
        self.empty_spots = None
        self.all_sprites = None

        #Establishing instances of the game board class to handle each side's game board.
        self.user_board = Game_Board()
        self.computer_board = Game_Board()

        #Establishing instance of the game status class to handle the flow of the game
        self.game_status = Game_Status()

    def setup(self):
        self.user_ships = arcade.SpriteList()
        self.computer_ships = arcade.SpriteList()
        self.empty_spots = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        
        self.user_grid_sprites = []
        self.computer_grid_sprites = []

        for row in range(constants.ROW_COUNT):
            self.user_grid_sprites.append([])
            self.computer_grid_sprites.append([])
            for column in range(constants.COLUMN_COUNT):
                new_user_place = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = (column + 1) * 50, center_y = constants.SCREEN_HEIGHT - row * 50 + 100, image_width=30,image_height=20)
                new_computer_place = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = ((column + 1) * 50) + 500, center_y = constants.SCREEN_HEIGHT - row * 50 + 100, image_width = 30, image_height = 20)
                self.empty_spots.append(new_user_place)
                self.empty_spots.append(new_computer_place)
                self.user_grid_sprites[row].append(new_user_place)
                self.computer_grid_sprites[row].append(new_computer_place)
                self.all_sprites.append(new_user_place)
                self.all_sprites.append(new_computer_place)
        """
        #Creating each coordinate's sprite for each side of the board
        for x in range(50,450,50):
            for y in range(100,600,50):
                #User side of game board
                empty_user_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = x, center_y = constants.SCREEN_HEIGHT - y, image_width=30,image_height=20)
                self.empty_spots.append(empty_user_spot)
                self.all_sprites.append(empty_user_spot)

                #Computer side of board
                empty_computer_spot = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = x + 500,center_y = constants.SCREEN_HEIGHT - y, image_width = 30, image_height = 20)
                self.empty_spots.append(empty_computer_spot)
                self.all_sprites.append(empty_computer_spot)
        """
        #Creating the center dividor between the sides of the board
        self.dividor = arcade.Sprite(constants.DIVIDOR_IMAGE,center_x = 480, center_y = 470)
        self.all_sprites.append(self.dividor)

        #Setting the game's background
        arcade.set_background_color(arcade.color.AQUA)
        self.background_loaded = arcade.load_texture(constants.BACKGROUND_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background_loaded)


        self.selector = arcade.Sprite(constants.SELECTOR_IMAGE)
        self.all_sprites.append(self.selector)

            
    def on_mouse_press(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.selector.center_x = x
            self.selector.center_y = y
            for empty_spot in self.empty_spots:
                if self.selector.collides_with_sprite(empty_spot):
                    self.empty_spots.remove(empty_spot)
                    self.touching = True
                else:
                    self.touching = False

        """sprite_selected = arcade.get_sprites_at_point((x,y), self.empty_spots)
        sprite_selected[0].color = arcade.color.BLUE"""
        column = int(x // (constants.WIDTH + constants.MARGIN))
        row = int(y // (constants.HEIGHT + constants.MARGIN))
        if x < 500:
            self.user_grid_sprites[row][column].color = arcade.color.BLUE
        elif x >= 550:
            self.computer_grid_sprites[row][column].color = arcade.color.BLUE


    
    def get_click_selection(self):
        pass


    def on_update(self,delta_time):
        self.output_service.clear_screen()
        self.output_service.draw_all_sprites(self.all_sprites)
        
        #Creating labels for each side of board
        arcade.draw_text("Allies",start_x = 175, start_y = 740, color=arcade.color.BLACK, font_size=40, )
        arcade.draw_text("Enemies",start_x = 640, start_y = 740, font_size=40, color=arcade.color.RED)
        
        
        #Checking for touching empty spot - TESTING 
        

        arcade.draw_text(f"Touching: {self.touching}",start_x = 500, start_y = 775,color=arcade.color.BLACK)



