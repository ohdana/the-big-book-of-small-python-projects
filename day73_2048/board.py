WIDTH = 4
HEIGHT = 4
EMPTY_CHAR = ' '

W, A, S, D = 'w', 'a', 's', 'd'

class Board:
    def __init__(self):
        self.canvas = self.init_canvas()

    def is_full(self):
        return all([self.is_full_row(row) for row in self.canvas])

    def move_cell(self, direction):
        pass

    def is_full_row(self, row):
        return all([not self.is_empty(cell) for cell in row])

    def is_empty(self, x, y):
        return self.get_cell(x, y) == EMPTY_CHAR

    def get_cell(self, x, y):
        if x < 0 or x >= WIDTH:
            return None
        if y < 0 or y >= HEIGHT:
            return None

        return self.canvas[y][x]

    def merge_cells(self, moving_cell, cell_dest):
        moving_cell_x, moving_cell_y = moving_cell
        cell_dest_x, cell_dest_y = cell_dest
        new_cell_dest_value = self.canvas[moving_cell_y][moving_cell_x] + self.canvas[cell_dest_y][cell_dest_x]
        self.remove_cell(moving_cell_x, moving_cell_y)
        self.set_cell_value(cell_dest_x, cell_dest_y, new_cell_dest_value)

    def remove_cell(self, x, y):
        self.set_cell_value(x, y, EMPTY_CHAR)

    def set_cell_value(self, x, y, value):
        self.canvas[y][x] = value

    def swap_cells(self, cell_1, cell_2):
        x_1, y_1 = cell_1
        x_2, y_2 = cell_2
        self.canvas[y_1][x_1], self.canvas[y_2][x_2] = self.canvas[y_2][x_2], self.canvas[y_1][x_1]

    def get_top_neighbour_coords(self, x, y):
        return x, y - 1

    def get_bottom_neighbour_coords(self, x, y):
        return x, y + 1

    def get_left_neighbour_coords(self, x, y):
        return x - 1, y

    def get_right_neighbour_coords(self, x, y):
        return x + 1, y

    def init_canvas(self):
        return [[EMPTY_CHAR] * WIDTH for i in range(HEIGHT)]

b = Board()
print(b.canvas)
