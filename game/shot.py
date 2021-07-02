from math import e
import random

class attacks():
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list

    def check_shot(self, coordinate, coordinate_list):
        #print(f"Value at {coordinate}: {coordinate_list[coordinate]}") #Remove after
        if coordinate_list[coordinate] == "s":
            return "hit!"

        elif coordinate_list[coordinate] == "e":
            return "miss!"
        
        else:           
            return "already fired there!"         

    def computer_shot(self, sprite_list):
        """
        Purpose: To generate random shot from the computer to the user
        """
        
        shot_coordinate = random.randint(0, len(sprite_list)-1)

        print(f"Attempted shot: {shot_coordinate}")
        return self.check_shot(shot_coordinate, sprite_list),shot_coordinate

    
