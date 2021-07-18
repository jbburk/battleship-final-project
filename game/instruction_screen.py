import arcade
import constants

#from start_screen import StartScreen

class InstructionScreen(arcade.View):
    def __init__(self,start_screen):
        super().__init__()
        self.start_screen = start_screen
        self.instructions_text = {0:["Welcome to Battleship!",100],
                                  1:["This is a super simple game, but here's how",0],
                                  2:["to play! Begin by placing your own ships on the",0],
                                  3:["left side of the board. Next, the computer will",0],
                                  4:["place its own ships on the left. Then, it'll be ",0],
                                  5:["your turn to start firing. Click on any spot on the",0],
                                  6:["right to fire on the computer's ships until you've hit",0],
                                  7:["all 5! Good luck Captain!",100]}
    
    def on_show(self):
        arcade.set_background_color(arcade.color.YELLOW)

        self.return_button = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = constants.SCREEN_WIDTH / 2, center_y = constants.SCREEN_HEIGHT / 4)
        self.return_button.color = arcade.color.BLUE
        self.return_button.height = 50

    
        self.mouse = arcade.Sprite(constants.CLICKER_IMAGE, center_x=700,center_y=700,image_height=20,image_width=12)
        
    def on_draw(self):
        arcade.start_render()
        #draw text for everything to be displayed
        for line in range(0,len(self.instructions_text)):
            new_line = self.instructions_text[line][0]
            arcade.draw_text(new_line,start_x = 95 + self.instructions_text[line][1], start_y=constants.SCREEN_HEIGHT - (line * 30) - 100,color=arcade.color.BLACK, font_size=24)
            #arcade.draw_text(self.instructions_text[line],start_x = 150, start_y=200,color=arcade.color.BLACK, font_size=15)

        self.return_button.draw()
        arcade.draw_text("Return to\n   main", (constants.SCREEN_WIDTH / 2) - 30, (constants.SCREEN_HEIGHT/4) - 15, color=arcade.color.WHITE)
        self.mouse.draw()

    def on_mouse_motion(self,x,y,dx,dy):
        self.mouse.center_x = x
        self.mouse.center_y = y

    def on_mouse_press(self,x,y,button,modifiers):
        if self.mouse.collides_with_sprite(self.return_button):
            #self.start_screen = StartScreen()
            self.window.show_view(self.start_screen)


