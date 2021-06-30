import arcade
import constants
class Grid_Spot(arcade.Sprite):
    def __init__(self,image,center_x,center_y,width,height):
        super().__init__(image,center_x,center_y,image_width=width,image_height=height)
        self.top_left = [center_x - (constants.WIDTH / 2),center_y - (constants.HEIGHT / 2)]
        self.bottom_right = [center_x + (constants.WIDTH / 2), center_y + (constants.HEIGHT / 2)]
        

    


