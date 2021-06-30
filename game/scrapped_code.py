 """self.user_grid_sprites = []
        self.computer_grid_sprites = []

        for row in range(constants.ROW_COUNT):
            self.user_grid_sprites.append([])
            self.computer_grid_sprites.append([])
            for column in range(constants.COLUMN_COUNT):
                user_x = (column + 1) * 50
                user_y = SCREEN_HEIGHT - ((row + 1) * 50)
                computer_x  = ((column + 1) * 50) + 500
                computer_y = SCREEN_HEIGHT - ((row + 1) * 50)

                user_x = column * (constants.WIDTH + constants.MARGIN) + (constants.WIDTH / 2 + constants.MARGIN)
                user_y = row * (constants.HEIGHT + constants.MARGIN) + (constants.HEIGHT / 2 + constants.MARGIN)

                computer_x = (column * (constants.WIDTH + constants.MARGIN) + (constants.WIDTH / 2 + constants.MARGIN)) + 500
                computer_y = row * (constants.HEIGHT + constants.MARGIN) + (constants.HEIGHT / 2 + constants.MARGIN)

                new_user_place = arcade.Sprite(constants.EMPTY_SPOT_IMAGE, center_x = user_x , center_y = user_y, image_width=30,image_height=20)
                new_computer_place = arcade.Sprite(constants.EMPTY_SPOT_IMAGE,center_x = computer_x, center_y = computer_y, image_width=30, image_height=20)
                
                self.empty_spots.append(new_user_place)
                self.empty_spots.append(new_computer_place)
                self.user_grid_sprites[row].append(new_user_place)
                self.computer_grid_sprites[row].append(new_computer_place)
                self.all_sprites.append(new_user_place)
                self.all_sprites.append(new_computer_place)
                print(f"{row},{column}")

        print(len(self.user_grid_sprites),len(self.user_grid_sprites[0]))
        """


         """sprite_selected = arcade.get_sprites_at_point((x,y), self.empty_spots)
        sprite_selected[0].color = arcade.color.BLUE"""