from board import Board

W, A, S, D = 'w', 'a', 's', 'd'

class Game:
    def __init__(self):
        self.board = self.init_board()
        self.board.add_new_random_cell()

    def make_move(self, direction):
        self.board.move(direction)
        if self.board.has_been_moved_any_cell():
            self.board.add_new_random_cell()

    def can_make_move(self):
        return not self.board.is_full()

    def show_board(self):
        canvas = self.board.get_canvas()
        print(canvas)

    def init_board(self):
        return Board()
