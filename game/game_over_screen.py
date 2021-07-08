import arcade
import constants
import sys

class GameOverScreen(arcade.View):
    def __init__(self,game_screen,winner):
        super().__init__()
        print(winner)
        self.winner = winner
        self.message = ""
        self.game_screen = game_screen

    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN_YELLOW)
        
        self.mouse = arcade.Sprite(constants.CLICKER_IMAGE, center_x = 300, center_y = 300,image_height=20,image_width=12)

        self.all_sprites = arcade.SpriteList()

        #Return to game
        self.return_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x=constants.SCREEN_WIDTH - 550, center_y=constants.SCREEN_HEIGHT - 400)
        self.return_button.color = arcade.color.BLUE
        self.return_button.width = 100
        self.return_button.height = 50
        self.all_sprites.append(self.return_button)

        #Exit button
        self.exit_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = constants.SCREEN_WIDTH - 220, center_y = constants.SCREEN_HEIGHT - 400)
        self.exit_button.color = arcade.color.RED
        self.exit_button.width = 100
        self.exit_button.height = 50
        self.all_sprites.append(self.exit_button)
        
    def on_draw(self):
        arcade.start_render()
        if self.winner == "user":
            self.message = "You won! Congratulations Captain!"

        else:
            self.message = "You lost! The computer beat you!\nBetter luck next time!"

        
        self.all_sprites.draw()

        arcade.draw_text(self.message,start_x = (constants.SCREEN_WIDTH/2) - 300, start_y = constants.SCREEN_HEIGHT / 2, color=arcade.color.WHITE,font_size=35)
        
        arcade.draw_text("Play Again",start_x=constants.SCREEN_WIDTH - 585, start_y=constants.SCREEN_HEIGHT - 410, color=arcade.color.WHITE)
        arcade.draw_text("Exit",start_x=constants.SCREEN_WIDTH - 230, start_y=constants.SCREEN_HEIGHT - 410, color=arcade.color.WHITE)
        
        self.mouse.draw()

    def on_mouse_motion(self,x,y,dx,dy):
        self.mouse.center_x = x
        self.mouse.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse.collides_with_sprite(self.return_button):
            self.window.show_view(self.game_screen)
        elif self.mouse.collides_with_sprite(self.exit_button):
            arcade.close_window()