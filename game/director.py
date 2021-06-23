import arcade
from game.game_board import Game_Board

class Director:
    def __init__(self):
        self.user_board = Game_Board()
        self.computer_board = Game_Board()

        print(self.user_board.board)
        print()
        print(self.computer_board.board)
        