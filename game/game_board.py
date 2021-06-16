class Game_Board:
    """
    Class to handle each side of the game board, the user's and the computer's

    Stereotype: Information Holder

    """

    def __init__(self):
        self.board = []
        for row in range(0,8):
            self.board.append([])
            for column in range(0,8):
                self.board[row].append("-")

    def place_ship(self,row,column):
        """Method used to place a new ship on the board"""
        if self.board[row][column] == "S":
            return "ship already present"
        else:
            self.board[row][column] = "S"

    def place_hit(self,row,column):
        """Method used to record a hit on the board"""
        self.board[row][column] = "H"

    def place_miss(self,row,column):
        """Method used to record a miss on the board"""
        self.board[row][column] = "M"

    def check_shot(self,row,column):
        """Method used to check a shot taken on the board and if the shot 
        results in a hit or miss, record that hit or miss on the board"""
        if self.board[row][column] == "H" or self.board[row][column] == "M":
            return "You've already fired there"

        elif self.board[row][column] == "S":
            self.place_hit(row,column)
            return "Hit!"
        
        elif self.board[row][column] == "-":
            self.place_miss(row,column)
            return "Miss!"
