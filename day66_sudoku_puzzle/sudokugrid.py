import random, copy
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
VALID_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CANVAS = '''
   A B C   D E F   G H I
1  {} {} {} | {} {} {} | {} {} {}
2  {} {} {} | {} {} {} | {} {} {}
3  {} {} {} | {} {} {} | {} {} {}
   ------+-------+------
4  {} {} {} | {} {} {} | {} {} {}
5  {} {} {} | {} {} {} | {} {} {}
6  {} {} {} | {} {} {} | {} {} {}
   ------+-------+------
7  {} {} {} | {} {} {} | {} {} {}
8  {} {} {} | {} {} {} | {} {} {}
9  {} {} {} | {} {} {} | {} {} {}'''
MAP = None

class SudokuGrid:
    def init_map(self):
        global MAP
        MAP = []
        column_groups = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        row_groups = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

    def __init__(self):
        self.canvas = self.init_canvas()
        self.original = copy.deepcopy(self.canvas)
        self.moves = []

    def are_valid_numbers(self, numbers):
        return sorted(numbers) == VALID_NUMBERS

    def get_row_numbers(self, cell_id):
        pass

    def get_column_numbers(self, cell_id):
        pass

    def get_square_numbers(self, cell_id):
        pass

    def get_cell(self, cell_id):
        pass

    def is_solved(self):
        pass

    def get_canvas(self):
        pass

    def init_canvas(self):
        pass

    def get_original(self):
        pass

    def undo(self):
        if not self.moves:
            return
        last_move = self.moves.pop()
        self.revert_move(last_move)

    def revert_move(self, move):
        pass

    def cross_product(self, list_1, list_2):
        result = []
        for i in list_1:
            for j in list_2:
                result += '{}{}'.format(i, j)
        return result
