import arcade
import constants

from instruction_screen import InstructionScreen
from director import Director

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        
  

    def on_show(self):
        #arcade.set_background_color(arcade.color.SKY_BLUE)
        self.window.set_mouse_visible(False)
        self.start_sprites = arcade.SpriteList()
        
        self.mouse = arcade.Sprite(constants.CLICKER_IMAGE, center_x=300,center_y=300,image_height=20,image_width=12)
        
        self.instructions_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = constants.SCREEN_WIDTH - 550 , center_y=constants.SCREEN_HEIGHT - 300)
        self.instructions_button.color=arcade.color.RED
        self.instructions_button.width = 100
        self.instructions_button.height = 50
        self.start_sprites.append(self.instructions_button)

        self.start_game_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = constants.SCREEN_WIDTH - 220, center_y = constants.SCREEN_HEIGHT - 300)
        self.start_game_button.color = arcade.color.DARK_YELLOW
        self.start_game_button.width = 100
        self.start_game_button.height=50
        self.start_sprites.append(self.start_game_button)


    def on_draw(self):
        arcade.start_render()
        self.background_loaded = arcade.load_texture(constants.BACKGROUND_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background_loaded)
        
        self.start_sprites.draw()
        arcade.draw_text("Welcome to Battleship!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size = 45, anchor_x = "center")
        arcade.draw_text("Instructions", constants.SCREEN_WIDTH - 585, constants.SCREEN_HEIGHT - 310,arcade.color.WHITE )
        arcade.draw_text("Start Game", constants.SCREEN_WIDTH - 255,constants.SCREEN_HEIGHT - 310, arcade.color.WHITE)
        self.mouse.draw()

    def on_mouse_motion(self,x,y,dx,dy):
        self.mouse.center_x = x
        self.mouse.center_y = y

    def on_mouse_press(self,x,y,button,modifiers):
        if self.mouse.collides_with_sprite(self.instructions_button):
            self.open_instructions()
        if self.mouse.collides_with_sprite(self.start_game_button):
            self.start_game()

    def open_instructions(self):
        self.instructions_screen = InstructionScreen(self) 
        self.window.show_view(self.instructions_screen)

    def start_game(self):
        self.game_screen = Director()
        self.window.show_view(self.game_screen)


