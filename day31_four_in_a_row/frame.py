FRAME_HORIZONTAL_CHAR = '-'
FRAME_VERTICAL_CHAR = '|'
FRAME_CORNER_CHAR = '+'
CELL_EMPTY_CHAR = '.'
N_OF_ROWS, N_OF_COLS = 6, 7
WINNING_COMBO_LENGTH = 4
TOP_ROW_POINTER = 2 # row 0 of the frame is the header, row 1 is the top outline of the frame

class Frame:
    def __init__(self, token_types):
        self.width = N_OF_COLS
        self.height = N_OF_ROWS
        self.token_types = token_types
        self.body = self.build()
        self.column_n_of_free_slots = [self.height for i in range(self.width)]

    def get_n_of_columns(self):
        return N_OF_COLS

    def get(self):
        return self.body

    def get_image(self):
        pass

    def throw_token(self, token_char, column_number):
        if not self.has_space_column(column_number):
            return

        self.update_canvas(token_char, column_number)
        self.column_n_of_free_slots[column_number - 1] -= 1

    def update_canvas(self, char, column_number):
        x, y = self.get_column_top_coords(column_number)
        self.body[y][x] = char

    def get_column_top_coords(self, column_number):
        x = column_number
        y = self.height + 1
        while self.body[y][x] != CELL_EMPTY_CHAR:
            y -= 1

        return x, y

    def show_canvas(self):
        lines = [''.join(line) for line in self.body]
        print('\n'.join(lines))

    def has_space_column(self, column_number):
        return self.column_n_of_free_slots[column_number - 1] > 0

    def has_space(self):
        return any([n > 0 for n in self.column_n_of_free_slots])

    def get_winner(self):
        for token in self.token_types:
            winning_combo = token * WINNING_COMBO_LENGTH
            if self.did_horizontal_line(winning_combo):
                return token
            if self.did_vertical_line(winning_combo):
                return token
            if self.did_diagonal_line(winning_combo):
                return token

    def did_horizontal_line(self, winning_combo):
        lines = [''.join(line) for line in self.body]
        for line in lines:
            if winning_combo in ''.join(line):
                return True

        return False

    def did_vertical_line(self, winning_combo):
        columns = self.get_columns()
        for column in columns:
            if winning_combo in ''.join(column):
                return True

        return False

    def did_diagonal_line(self, winning_combo):
        diagonals = self.get_diagonals()
        for diagonal in diagonals:
            if winning_combo in ''.join(diagonal):
                return True

        return False

    def get_diagonals(self):
        diagonals = []
        downward_diagonals_coords = self.get_downward_diagonals()
        upward_diagonals_coords = self.get_upward_diagonals()
        diagonals_coords = downward_diagonals_coords + upward_diagonals_coords
        for diagonal_coords in diagonals_coords:
            diagonal = []
            for x, y in diagonal_coords:
                diagonal.append(self.body[y][x])
            diagonals.append(diagonal)

        return diagonals

    def get_downward_diagonals(self):
        diagonals = []
        start_cells = []
        for i in range(self.height):
            start_cells.append((i, 0))
        for j in range(self.width):
            start_cells.append((0, j))

        diagonals = []
        for cell in set(start_cells):
            diagonals.append(self.build_downward_diagonal(cell))
        return diagonals

    def build_downward_diagonal(self, cell):
        x, y = cell
        cells = []
        while y <= self.width and x <= self.height:
            cells.append((x, y))
            x += 1
            y += 1
        return cells

    def get_upward_diagonals(self):
        diagonals = []
        start_cells = []
        for i in range(self.height):
            start_cells.append((i, 0))
        for j in range(self.width):
            start_cells.append((self.height, j))

        diagonals = []
        for cell in set(start_cells):
            diagonals.append(self.build_upward_diagonal(cell))
        return diagonals

    def build_upward_diagonal(self, cell):
        x, y = cell
        cells = []
        while x >= 0 and y >= 0:
            if y <= self.width and x <= self.height:
                cells.append((x, y))
            x -= 1
            y += 1
        return cells

    def is_in_bound_x(self, x):
        return 0 <= x <= self.height

    def is_in_bound_y(self, y):
        return 0 <= y <= self.width

    def get_columns(self):
        columns = []
        for i in range(self.width):
            columns.append([])

        for i in range(self.height):
            for j in range(self.width):
                columns[j].append(self.body[i + 2][j + 1])

        return columns

    def build(self):
        frame = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(CELL_EMPTY_CHAR)
            frame.append(new_line)
        self.add_top_bottom_borders(frame)
        self.add_left_right_borders(frame)
        self.add_corners(frame)
        self.add_header(frame)

        return frame

    def has_winner(self):
        return self.get_winner() is not None

    def get_horizontal_line(self, length):
        return [FRAME_HORIZONTAL_CHAR for i in range(length)]

    def add_header(self, frame):
        gap_char = [' ']
        header = gap_char + [str(i + 1) for i in range(self.width)] + gap_char
        frame.insert(0, header)

    def add_top_bottom_borders(self, frame):
        frame.insert(0, self.get_horizontal_line(self.width))
        frame.append(self.get_horizontal_line(self.width))

    def add_left_right_borders(self, frame):
        for line in frame:
            line.insert(0, FRAME_VERTICAL_CHAR)
            line.append(FRAME_VERTICAL_CHAR)

    def add_corners(self, frame):
        max_x = len(frame[0])
        max_y = len(frame)
        top_left = (0, 0)
        top_right = (max_x - 1, 0)
        bottom_right = (max_x - 1, max_y - 1)
        bottom_left = (0, max_y - 1)

        corners = [top_left, top_right, bottom_left, bottom_right]
        for corner in corners:
            x, y = corner
            frame[y][x] = FRAME_CORNER_CHAR
