class Game_Status:
    def __init__(self):
        self.placing_user_ships = True
        self.placing_computer_ships = False
        self.user_turn = False
        self.computer_turn = False
        self.user_ships_placed = 0
        self.computer_ships_placed = 0

        self.ships_sunk = {"user":0,"computer":0}

    def add_placed_ship(self):
        if self.placing_user_ships:
            #print(f"Current ships placed: {self.user_ships_placed}")
            if self.user_ships_placed == 4:
                self.end_placing_user_ships()
                self.user_ships_placed = 5
            else:
                self.user_ships_placed += 1
                
        else:
            if self.computer_ships_placed == 4:
                self.end_placing_computer_ships()
                self.computer_ships_placed = 5
                self.user_turn = True
            else:
                self.computer_ships_placed += 1


    def is_placing_user_ships(self):
        return self.placing_user_ships
    
    def is_placing_computer_ships(self):
        return self.placing_computer_ships

    def get_current_turn(self):
        if self.user_turn:
            return "user"
        if self.computer_turn:
            return "computer"


    def end_placing_user_ships(self):
        self.placing_user_ships = False
        self.placing_computer_ships = True

    def end_placing_computer_ships(self):
        self.placing_computer_ships = False
        self.user_turn = True

    def switch_turns(self):
        self.user_turn = not self.user_turn
        self.computer_turn = not self.computer_turn

    def ship_sunk(self,side):
        self.ships_sunk[side] = self.ships_sunk.get(side) + 1