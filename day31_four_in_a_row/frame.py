FRAME_HORIZONTAL_CHAR = '-'
FRAME_VERTICAL_CHAR = '|'
FRAME_CORNER_CHAR = '+'
CELL_EMPTY_CHAR = '.'
WINNING_COMBO_LENGTH = 4
TOP_ROW_POINTER = 2 # row 0 of the frame is the header, row 1 is the top outline of the frame

class Frame:
    def __init__(self, width, height, token_types):
        self.width = width
        self.height = height
        self.token_types = token_types
        self.body = self.build()
        self.column_n_of_free_slots = [height for i in range(width)]

    def get(self):
        return self.body()

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
        #return self.body[TOP_ROW_POINTER][column_number] == CELL_EMPTY_CHAR
        return self.column_n_of_free_slots[column_number - 1]

    def has_space(self):
        #top_row = self.body[TOP_ROW_POINTER]
        #return any([cell == CELL_EMPTY_CHAR for cell in top_row])
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
            if winning_combo in line:
                return True

        return False

    def did_vertical_line(self, winning_combo):
        columns = self.get_columns()
        for column in columns:
            if winning_combo in column:
                return True

        return False

    def did_diagonal_line(self, winning_combo):
        diagonals = self.get_diagonals()
        for diagonal in diagonals:
            if winning_combo in diagonal:
                return True

        return False

    def get_diagonals(self):
        diagonals = []
        #for i in range(self.height):
        #    for j in range(self.width):
        #        diagonals.append()
        return diagonals

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

frame = Frame(5, 7, ['X', 'O'])
frame.throw_token('X', 2)
frame.throw_token('X', 2)
frame.throw_token('X', 2)
frame.throw_token('X', 2)
frame.show_canvas()
#print(frame.get_winner())
lines = [''.join(line) for line in frame.get_columns()]
print('\n'.join(lines))
