import copy
import diagonals_builder, columns_builder, rows_builder

GAP_CHAR = ' '
FRAME_HORIZONTAL_CHAR = '-'
FRAME_VERTICAL_CHAR = '|'
FRAME_CORNER_CHAR = '+'
CELL_EMPTY_CHAR = '.'

N_OF_ROWS = 6
N_OF_COLS = 7
WINNING_COMBO_LENGTH = 4
LINES_COORDS = None

class Canvas:
    def __init__(self, token_types):
        self.width = N_OF_COLS
        self.height = N_OF_ROWS
        self.init_coords_maps()
        self.token_types = token_types
        self.grid = self.build_grid()
        self.column_n_of_free_slots = [self.height for i in range(self.width)]

    def get(self):
        return self.get_canvas()

    def get_winning_token(self):
        winning_combos = [token * WINNING_COMBO_LENGTH for token in self.token_types]
        lines = [self.build_line(line_coords) for line_coords in LINES_COORDS]
        for line in lines:
            for winning_combo in winning_combos:
                if winning_combo in line:
                    return winning_combo[0]

    def build_line(self, line_coords):
        return ''.join([self.grid[y][x] for x, y in line_coords])

    def has_space(self):
        return any([n > 0 for n in self.column_n_of_free_slots])

    def has_space_column(self, column_number):
        return self.column_n_of_free_slots[column_number - 1] > 0

    def get_column_numbers(self):
        return [i + 1 for i in range(N_OF_COLS)]

    def throw_token(self, token_char, column_number):
        if not self.has_space_column(column_number):
            return

        self.update_canvas(token_char, column_number)
        self.column_n_of_free_slots[column_number - 1] -= 1

    def update_canvas(self, char, column_number):
        x, y = self.get_column_top_coords(column_number)
        self.grid[y][x] = char

    def get_column_top_coords(self, column_number):
        x = column_number - 1
        y = self.height - 1
        while self.grid[y][x] != CELL_EMPTY_CHAR:
            y -= 1

        return x, y

    def get_canvas(self):
        canvas = copy.deepcopy(self.grid)
        self.add_top_bottom_borders(canvas)
        self.add_left_right_borders(canvas)
        self.add_corners(canvas)
        self.add_header(canvas)

        return canvas

    def show_canvas(self):
        lines = [''.join(line) for line in self.get_canvas()]
        print('\n'.join(lines))

    def build_grid(self):
        grid = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(CELL_EMPTY_CHAR)
            grid.append(new_line)
        return grid

    def get_horizontal_line(self, length):
        return [FRAME_HORIZONTAL_CHAR for i in range(length)]

    def add_header(self, canvas):
        header = [GAP_CHAR] + [str(i + 1) for i in range(self.width)] + [GAP_CHAR]
        canvas.insert(0, header)

    def add_top_bottom_borders(self, canvas):
        canvas.insert(0, self.get_horizontal_line(self.width))
        canvas.append(self.get_horizontal_line(self.width))

    def add_left_right_borders(self, canvas):
        for line in canvas:
            line.insert(0, FRAME_VERTICAL_CHAR)
            line.append(FRAME_VERTICAL_CHAR)

    def add_corners(self, canvas):
        max_x = len(canvas[0])
        max_y = len(canvas)
        top_left = (0, 0)
        top_right = (max_x - 1, 0)
        bottom_right = (max_x - 1, max_y - 1)
        bottom_left = (0, max_y - 1)

        corners = [top_left, top_right, bottom_left, bottom_right]
        for corner in corners:
            x, y = corner
            canvas[y][x] = FRAME_CORNER_CHAR

    def init_coords_maps(self):
        global LINES_COORDS
        rows_coords = rows_builder.get_rows(self.width, self.height)
        columns_coords = columns_builder.get_columns(self.width, self.height)
        diagonals_coords = diagonals_builder.get_diagonals(self.width, self.height)
        LINES_COORDS = rows_coords + columns_coords + diagonals_coords
