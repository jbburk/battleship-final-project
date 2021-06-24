import arcade
from game.point import Point

class Input_Service:
    def __init__(self,screen):
        self.screen = screen
        self._keys = {}
        self.keys[119] = Point(0, -1) #Up
        self.keys[115] = Point(0, 1) #Left
        self.keys[97] = Point(-1, 0) #Down
        self.keys[100] = Point(1, 0) #Right
        self.keys[13] = "Enter"


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
