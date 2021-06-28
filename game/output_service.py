import arcade

class Output_Service:
    def clear_screen(self):
        arcade.start_render()

    def draw_all_sprites(self,sprite_list):
        for sprite in sprite_list:
            sprite.draw()

    def flush_buffer(self):
        pass


