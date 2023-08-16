import random

CURSOR_CHAR = '>'
FRAME_TOP_LEFT_CHAR = chr(9484)  # Character 9484 is '┌'
FRAME_BOTTOM_LEFT_CHAR = chr(9492)  # Character 9492 is '└'
FRAME_TOP_RIGHT_CHAR = chr(9488)  # Character 9488 is '┐'
FRAME_BOTTOM_RIGHT_CHAR = chr(9496)  # Character 9496 is '┘'
FRAME_HORIZONTAL_CHAR = chr(9472)  # Character 9472 is '─'
FRAME_VARTICAL_CHAR = chr(9474)  # Character 9474 is '│'

class Frame:
    def __init__(self, width, height, available_chars):
        self.available_chars = available_chars
        self.width = width
        self.height = height
        self.canvas = self.get_new_canvas()
        self.fill_up()

    def get(self):
        return self.canvas

    def get_new_canvas(self):
        frame = self.build_frame()
        canvas = self.add_cursor(frame)

        return canvas

    def update_cell(self, x, y, char):
        self.canvas[y][x] = char

    def build_frame(self):
        canvas = []
        canvas.append([FRAME_HORIZONTAL_CHAR] * (self.width + 2))
        for i in range(self.height):
            new_line = [FRAME_VARTICAL_CHAR] + [' '] * self.width + [FRAME_VARTICAL_CHAR]
            canvas.append(new_line)
        canvas.append([FRAME_HORIZONTAL_CHAR] * (self.width + 2))

        top_left_x, top_left_y = 0, 0
        bottom_right_x, bottom_right_y = self.width + 1, self.height + 1
        top_right_x, top_right_y = self.width + 1, 0
        bottom_left_x, bottom_left_y = 0, self.height + 1

        canvas[top_left_y][top_left_x] = FRAME_TOP_LEFT_CHAR
        canvas[bottom_left_y][bottom_left_x] = FRAME_BOTTOM_LEFT_CHAR
        canvas[top_right_y][top_right_x] = FRAME_TOP_RIGHT_CHAR
        canvas[bottom_right_y][bottom_right_x] = FRAME_BOTTOM_RIGHT_CHAR

        return canvas

    def add_cursor(self, canvas):
        cursor_x, cursor_y = 0, 1
        canvas[cursor_y][cursor_x] = CURSOR_CHAR

        return canvas

    def get_matching_neighbours(self, char, x, y, cells=None):
        if not cells:
            cells = []
        left = (x - 1, y)
        right = (x + 1, y)
        top = (x, y - 1)
        bottom = (x, y + 1)
        within_bounds = lambda x, y: 0 < x <= self.width and 0 < y <= self.height
        neighbours = [neighbour for neighbour in [left, top, right, bottom] if within_bounds(*neighbour)]

        for neighbour in neighbours:
            neighbour_x, neighbour_y = neighbour
            if self.canvas[neighbour_y][neighbour_x] == char:
                if not neighbour in cells:
                    cells.append(neighbour)
                    cells += self.get_matching_neighbours(char, neighbour_x, neighbour_y, cells)
                cells.append(neighbour)

        return list(set(cells))

    def is_filled_up_with_one_char(self):
        char = self.canvas[1][1]
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if self.canvas[i][j] != char:
                   return False

        return True

    def show_canvas(self):
        lines = [''.join(line) for line in self.canvas]
        print('\n'.join(lines))

    def fill_up(self):
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.canvas[i][j] = self.get_random_char()

    def get_random_char(self):
        return random.choice(self.available_chars)

#frame = Frame(10, 10, ['+', 'o', 'x'])
#frame.update_cell(1, 1, 'h')
#frame.show_canvas()
