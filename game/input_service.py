import arcade
#from arcade.gui.events import MOUSE_PRESS
from point import Point
import sys


#for now
import tkinter.messagebox as tk_mb


class Input_Service:
    def __init__(self,screen,selector):
        self.screen = screen
        self.selector = selector
        """self._keys = {}
        self.keys[119] = Point(0, -1) #Up
        self.keys[115] = Point(0, 1) #Left
        self.keys[97] = Point(-1, 0) #Down
        self.keys[100] = Point(1, 0) #Right
        self.keys[13] = "Enter"""


    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)


    """def return_key_press(self):
        event = self.screen.get_event()
        if isinstance(event, KeyboardEvent):
            self.current = self.keys.get(event.key_code, self.current)
            return self.current"""

    def on_key_press(self, key, modifiers):
        # Called whenever a key is pressed.
        if key == arcade.key.up or key == arcade.key.W:
            return Point(0, -1)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            return Point(0, 1)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            return Point(1, 0)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            return Point(-1, 0)

    def on_mouse_press(self,x,y,button,modifiers):
        tk_mb.showinfo(message="click")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.selector.center_x = x
            self.selector.center_y = y
            self.selector.draw() #For now

