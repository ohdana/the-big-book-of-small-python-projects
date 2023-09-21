import random, copy
from gridreader import GridReader

NO_VALUE = '.'
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
VALID_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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
SQUARES = None

class SudokuGrid:
    def __init__(self):
        gridreader = GridReader('sudokupuzzles.txt')
        puzzle_numbers = gridreader.get_random_puzzle()
        self.set_original(puzzle_numbers)
        self.reset()
        self.init_map()

    def set_original(self, puzzle_numbers):
        self.original = {}
        for i in ROWS:
            for j in COLUMNS:
                cell_id = '{}{}'.format(j, i)
                cell_value = puzzle_numbers.pop(0)
                self.original[cell_id] = cell_value

    def make_move(self, cell_id, cell_new_value):
        cell_old_value = self.get_cell(cell_id)
        self.canvas[cell_id] = cell_new_value
        log_entry = (cell_id, cell_old_value, cell_new_value)
        self.moves.append(log_entry)

    def get_original(self):
        return self.original

    def reset(self):
        self.canvas = copy.deepcopy(self.original)
        self.moves = []

    def undo(self):
        if not self.moves:
            return
        last_move = self.moves.pop()
        self.revert_move(last_move)

    def revert_move(self, move):
        cell_id, cell_old_value, cell_new_value = move
        self.canvas[cell_id] = cell_old_value

    def are_valid_numbers(self, numbers):
        return sorted(numbers) == VALID_NUMBERS

    def get_numbers(self, cell_ids):
        return [self.get_cell(cell_id) for cell_id in cell_ids]

    def get_cell(self, cell_id):
        return str(self.canvas[cell_id])

    def is_solved(self):
        for row_id in ROWS:
            row_cell_ids = self.cross_product(COLUMNS, [row_id])
            row_numbers = self.get_numbers(row_cell_ids)
            is_solved_row = self.are_valid_numbers(row_numbers)
            if not is_solved_row:
                return False

        for column_id in COLUMNS:
            column_cell_ids = self.cross_product([column_id], ROWS)
            column_numbers = self.get_numbers(column_cell_ids)
            is_solved_column = self.are_valid_numbers(column_numbers)
            if not is_solved_column:
                return False

        for square_cell_ids in SQUARES:
            square_numbers = self.get_numbers(square_cell_ids)
            is_solved_square = self.are_valid_numbers(square_numbers)
            if not is_solved_square:
                return False

        return True

    def is_full(self):
        return not any([self.get_cell(cell_id) == NO_VALUE for cell_id in self.canvas])

    def get_canvas_formatting_params(self):
        params = []
        for i in ROWS:
            for j in COLUMNS:
                cell_id = '{}{}'.format(j, i)
                cell_value = self.get_cell(cell_id)
                if not cell_value:
                    cell_value = NO_VALUE
                params.append(cell_value)
        return params

    def show_canvas(self):
        formatting_params = self.get_canvas_formatting_params()
        formatted_canvas = CANVAS.format(*formatting_params)
        print(formatted_canvas)

    def cross_product(self, list_1, list_2):
        result = []
        for i in list_1:
            for j in list_2:
                result.append('{}{}'.format(i, j))
        return result

    def init_map(self):
        global SQUARES, CELLS
        SQUARES = []
        row_groups = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        column_groups = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        for column_group in column_groups:
            square = []
            for row_group in row_groups:
                cells = self.cross_product(column_group, row_group)
                square.append(cells)
            SQUARES += square
