from board import Board

W, A, S, D = 'w', 'a', 's', 'd'

class Game:
    def __init__(self):
        self.board = self.init_board()

    def init_board(self):
        return Board()

    def make_move(self, move):
        pass

    def can_make_move(self):
        return not board.is_full()

    def show_board(self):
        pass
