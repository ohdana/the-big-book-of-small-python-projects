W, A, S, D = 'w', 'a', 's', 'd'

class CanvasNavigator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_ordered_coords_to_move(self, direction):
        if direction == W:
            return self.get_ordered_coords_to_move_up()
        elif direction == A:
            return self.get_ordered_coords_to_move_left()
        elif direction == S:
            return self.get_ordered_coords_to_move_down()
        elif direction == D:
            return self.get_ordered_coords_to_move_right()

    def get_ordered_coords_to_move_left(self):
        cells = []
        for row_number in range(self.height):
            for column_number in range(self.width):
                cells.append((column_number, row_number))
        print(cells)
        return cells

    def get_ordered_coords_to_move_down(self):
        cells = []
        for row_number in range(self.height):
            for column_number in range(self.width):
                cells.append((column_number, self.height - row_number - 1))
        return cells

    def get_ordered_coords_to_move_right(self):
        cells = []
        for column_number in range(self.width):
            for row_number in range(self.height):
                cells.append((self.width - column_number - 1, row_number))
        return cells

    def get_ordered_coords_to_move_up(self):
        return self.get_coords_up_to_down_left_to_right()

    def get_coords_up_to_down_left_to_right(self):
        cells = []
        for row_number in range(self.height):
            for column_number in range(self.width):
                cells.append((column_number, row_number))
        return cells

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
