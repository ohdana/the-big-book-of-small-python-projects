import random

TWO, FOUR = 2, 4
WIDTH = 4
HEIGHT = 4
EMPTY_CHAR = ' '
CANVAS_CELL_WIDTH = 5
CANVAS = '''
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
'''

W, A, S, D = 'w', 'a', 's', 'd'

class Board:
    def __init__(self):
        self.canvas = self.init_canvas()

    def is_full(self):
        cells = self.get_cells_coords_up_to_down_left_to_right()
        return all([not self.is_empty(*cell) for cell in cells])

    def move(self, direction):
        cells_to_move = self.get_ordered_cells_to_move(direction)
        for cell in cells_to_move:
            x, y = cell
            self.move_cell(x, y, direction)

    def add_new_cell(self):
        new_cell_value = self.generate_new_cell_value()
        new_cell_x, new_cell_y = self.get_random_empty_cell()
        self.set_cell_value(new_cell_x, new_cell_y, new_cell_value)

    def get_ordered_cells_to_move(self, direction):
        if direction == W:
            return self.get_ordered_cells_to_move_up()
        elif direction == A:
            return self.get_ordered_cells_to_move_left()
        elif direction == S:
            return self.get_ordered_cells_to_move_down()
        elif direction == D:
            return self.get_ordered_cells_to_move_right()

    def get_ordered_cells_to_move_up(self):
        return self.get_cells_coords_up_to_down_left_to_right()

    def get_ordered_cells_to_move_left(self):
        cells = []
        for column_number in range(WIDTH):
            for row_number in range(HEIGHT):
                cells.append((column_number, row_number))
        return cells

    def get_ordered_cells_to_move_down(self):
        cells = []
        for row_number in range(HEIGHT):
            for column_number in range(WIDTH):
                cells.append((column_number, HEIGHT - row_number - 1))
        return cells

    def get_ordered_cells_to_move_right(self):
        cells = []
        for column_number in range(WIDTH):
            for row_number in range(HEIGHT):
                cells.append((WIDTH - column_number - 1, row_number))
        return cells

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

    def get_neighbour_coords(self, x, y, direction):
        if direction == W:
            return self.get_top_neighbour_coords(x, y)
        elif direction == A:
            return self.get_left_neighbour_coords(x, y)
        elif direction == S:
            return self.get_bottom_neighbour_coords(x, y)
        elif direction == D:
            return self.get_right_neighbour_coords(x, y)

    def get_top_neighbour_coords(self, x, y):
        return x, y - 1

    def get_bottom_neighbour_coords(self, x, y):
        return x, y + 1

    def get_left_neighbour_coords(self, x, y):
        return x - 1, y

    def get_right_neighbour_coords(self, x, y):
        return x + 1, y

    def generate_new_cell_value(self):
        random_value = random.randint(1, 100)
        if random_value <= 75:
            return TWO
        return FOUR

    def get_random_empty_cell(self):
        random_x = random.randint(0, WIDTH - 1)
        random_y = random.randint(0, HEIGHT - 1)
        if not self.is_empty(random_x, random_y):
            return self.get_random_empty_cell()
        return random_x, random_y

    def init_canvas(self):
        return [[EMPTY_CHAR] * WIDTH for i in range(HEIGHT)]

    def move_cell(self, x, y, direction):
        #mark merged?
        neighbour_coords = self.get_neighbour_coords(x, y, direction)
        neighbour_x, neighbour_y = neighbour_coords
        neighbour = self.get_cell(neighbour_x, neighbour_y)
        cell = self.get_cell(x, y)
        if self.is_empty(neighbour_x, neighbour_y):
            self.swap_cells((x, y), neighbour_coords)
            self.move_cell(neighbour_x, neighbour_y, direction)
        elif neighbour == cell:
            self.merge_cells((x, y), neighbour_coords)

    def get_canvas(self):
        labels = self.get_labels_for_canvas()
        return CANVAS.format(*labels)

    def get_cells_coords_up_to_down_left_to_right(self):
        cells = []
        for row_number in range(HEIGHT):
            for column_number in range(WIDTH):
                cells.append((column_number, row_number))
        return cells

    def get_labels_for_canvas(self):
        cells = self.get_cells_coords_up_to_down_left_to_right()
        return [self.get_cell_label(*cell) for cell in cells]

    def get_cell_label(self, x, y):
        cell_value = str(self.get_cell(x, y))
        right_gap = ' ' * ((CANVAS_CELL_WIDTH - len(cell_value)) // 2)
        left_gap = ' ' * (CANVAS_CELL_WIDTH - len(right_gap) - len(cell_value))
        return '{}{}{}'.format(left_gap, cell_value, right_gap)
