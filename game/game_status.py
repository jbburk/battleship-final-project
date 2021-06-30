class Game_Status:
    def __init__(self):
        self.placing_user_ships = True
        self.placing_computer_ships = False
        self.user_turn = False
        self.computer_turn = False

    def end_placing_user_ships(self):
        self.placing_user_ships = False
        self.placing_computer_ships = True

    def end_placing_computer_ships(self):
        self.placing_computer_ships = False
        self.user_turn = True

    def switch_turns(self):
        self.user_turn = not self.user_turn
        self.computer_turn = not self.computer_turn

    