from math import e
import random

class attacks():
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list

    
    def check_shot(self, coordinate, coordinate_list):
        if coordinate_list[coordinate] == "e":
            return "hit!"
        else:           
            return "already fired there!"         

    def computer_shot(self, sprite_list):
        """
        Purpose: To generate random shot from the computer to the user
        """

        shot_coordinate = random.randint(0, len(sprite_list))
        return self.check_shot(shot_coordinate, sprite_list)
