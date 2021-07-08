import arcade
import constants

#from start_screen import StartScreen

class InstructionScreen(arcade.View):
    def __init__(self,start_screen):
        super().__init__()
        self.start_screen = start_screen
    
    def on_show(self):
        arcade.set_background_color(arcade.color.YELLOW)

        self.return_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = constants.SCREEN_WIDTH / 2, center_y = constants.SCREEN_HEIGHT / 2)
        self.return_button.color = arcade.color.BLUE
        self.return_button.height = 50
        
        self.mouse = arcade.Sprite(constants.CLICKER_IMAGE, center_x=700,center_y=700,image_height=20,image_width=12)
        

        

    def on_draw(self):
        arcade.start_render()
        #draw text for everything to be displayed
        self.return_button.draw()
        arcade.draw_text("Return to\n   main", (constants.SCREEN_WIDTH / 2) - 30, (constants.SCREEN_HEIGHT/2) - 15, color=arcade.color.WHITE)
        self.mouse.draw()

    def on_mouse_motion(self,x,y,dx,dy):
        self.mouse.center_x = x
        self.mouse.center_y = y

    def on_mouse_press(self,x,y,button,modifiers):
        if self.mouse.collides_with_sprite(self.return_button):
            #self.start_screen = StartScreen()
            self.window.show_view(self.start_screen)


