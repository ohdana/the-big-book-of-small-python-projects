import random

from cell import Cell
from canvasnavigator import CanvasNavigator

TWO, FOUR = 2, 4
MIN_PERCENT, MAX_PERCENT = 1, 100
PERCENT_PROBABILITY_OF_NEW_TWO = 75
WIDTH = 4
HEIGHT = 4
CANVAS_CELL_WIDTH = 5

W, A, S, D = 'w', 'a', 's', 'd'

class Board:
    def __init__(self):
        self.canvas_navigator = self.init_canvas_navigator()
        self.cells = self.init_cells()
        self.flush_move_log()

    def is_full(self):
        return len(self.cells) == (WIDTH * HEIGHT)

    def has_been_moved_any_cell(self):
        return (len(self.moved_cells) + len(self.merged_cells)) > 0

    def move(self, direction):
        self.flush_move_log()
        ordered_cells_coords = self.canvas_navigator.get_ordered_coords_to_move(direction)
        for coords in ordered_cells_coords:
            cell = self.get_cell(coords)
            if cell:
                self.move_cell(cell, direction)

    def flush_move_log(self):
        self.merged_cells = []
        self.moved_cells = []

    def mark_as_merged(self, coords):
        self.merged_cells.append(coords)

    def mark_as_moved(self, coords):
        self.moved_cells.append(coords)

    def move_cell(self, cell, direction):
        neighbour_coords = self.get_neighbour_coords(cell, direction)
        if not self.is_valid_coords(neighbour_coords):
            return
        neighbour = self.get_cell(neighbour_coords)
        if not neighbour:
            self.update_coords(cell, neighbour_coords)
            self.move_cell(cell, direction)
            self.mark_as_moved(cell.get_coords())
        elif neighbour and self.have_equal_value(cell, neighbour):
            self.merge_cells(cell, neighbour)
            self.mark_as_merged(neighbour_coords)

    def update_coords(self, cell, coords):
        self.remove_cell(cell)
        cell.set_coords(*coords)
        self.add_cell(cell)

    def remove_cell(self, cell):
        cells_coords = cell.get_coords()
        if cells_coords in self.cells:
            self.cells.pop(cells_coords)

    def merge_cells(self, moving_cell, target_cell):
        new_target_cell_value = moving_cell.get_value() + target_cell.get_value()
        self.remove_cell(moving_cell)
        target_cell.set_value(new_target_cell_value)

    def have_equal_value(self, cell, neighbour):
        return cell.get_value() == neighbour.get_value()

    def is_valid_coords(self, coords):
        x, y = coords
        if x < 0 or x >= WIDTH:
            return False

        if y < 0 or y >= HEIGHT:
            return False

        return True

    def get_neighbour_coords(self, cell, direction):
        x, y = cell.get_coords()
        return self.canvas_navigator.get_neighbour_coords(x, y, direction)

    def get_cell(self, coords):
        if coords in self.cells:
            return self.cells[coords]

    def add_cell(self, cell):
        self.cells[cell.get_coords()] = cell

    def get_new_cell(self, x, y, value):
        return Cell(x, y, value)

    def init_cells(self):
        return {}

    def init_canvas_navigator(self):
        return CanvasNavigator(WIDTH, HEIGHT)

    def add_new_random_cell(self):
        coords = self.generate_free_coords()
        value = self.generate_new_cell_value()
        cell = self.get_new_cell(*coords, value)
        self.add_cell(cell)

    def generate_free_coords(self):
        occupied_coords = [coords for coords in self.cells.keys()]
        new_coords = self.get_random_coords()
        if new_coords in occupied_coords:
            return self.generate_free_coords()

        return new_coords

    def get_random_coords(self):
        random_x = random.randint(0, WIDTH - 1)
        random_y = random.randint(0, HEIGHT - 1)

        return random_x, random_y

    def generate_new_cell_value(self):
        random_value = random.randint(MIN_PERCENT, MAX_PERCENT)
        if random_value <= PERCENT_PROBABILITY_OF_NEW_TWO:
            return TWO
        return FOUR

    def get_canvas(self):
        labels = self.get_labels_for_canvas()
        return self.get_canvas_pattern().format(*labels)

    def get_labels_for_canvas(self):
        coords = self.canvas_navigator.get_coords_up_to_down_left_to_right()
        return [self.get_cell_label(coords_pair) for coords_pair in coords]

    def get_cell_label(self, coords):
        cell_value = ''
        cell = self.get_cell(coords)
        if cell:
            cell_value = str(cell.get_value())
        right_gap = ' ' * ((CANVAS_CELL_WIDTH - len(cell_value)) // 2)
        left_gap = ' ' * (CANVAS_CELL_WIDTH - len(right_gap) - len(cell_value))

        return '{}{}{}'.format(left_gap, cell_value, right_gap)

    def get_canvas_pattern(self):
        return '''
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
