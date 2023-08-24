import time, random

SAND_CHAR = chr(9618)  # Character 9617 is '▒'
WALL_CHAR = chr(9608)  # Character 9608 is '█'
GAP_CHAR = ' '
WIDTH = 19

class Hourglass:
    def __init__(self):
        self.width = WIDTH
        self.middle_x = self.width // 2
        self.canvas = self.get_initial_hourglass()
        self.height = self.get_height()
        self.sand = []
        self.hourglass_outline = []
        self.init_sand()
        self.init_outline_coords()

    def get_initial_hourglass(self):
        top = self.get_full_top_half()
        bottom = self.get_empty_bottom_half()

        return self.get_hourglass(top, bottom)

    def get_compiled_canvas(self):
        result = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                char = GAP_CHAR
                if (i, j) in self.hourglass_outline:
                    char = WALL_CHAR
                elif (i, j) in self.sand:
                    char = SAND_CHAR
                line.append(char)
            result.append(line)

        return result

    def get_hourglass(self, top_half, bottom_half):
        return top_half + bottom_half[1:]

    def get_empty_top_half(self):
        return self.generate_empty_half()

    def get_empty_bottom_half(self):
        return list(reversed(self.get_empty_top_half()))

    def get_full_top_half(self):
        return self.generate_full_half()

    def init_sand(self):
        sand = []
        for i in range(self.height):
            for j in range(self.width):
                if self.canvas[i][j] == SAND_CHAR:
                    sand.append((i, j))
        self.sand = sand

    def init_outline_coords(self):
        outline = []
        for i in range(self.height):
            for j in range(self.width):
                if self.canvas[i][j] == WALL_CHAR:
                    outline.append((i, j))

        self.hourglass_outline = outline

    def generate_full_half(self):
        full_top_half = [WIDTH * [WALL_CHAR]]
        for i in range(2):
            new_line = [WALL_CHAR] + [GAP_CHAR] * (WIDTH - 2) + [WALL_CHAR]
            full_top_half.append(new_line)
        sand_top_line = [WALL_CHAR] + [SAND_CHAR] * 2 + [GAP_CHAR] * (WIDTH - 6) + [SAND_CHAR] * 2 + [WALL_CHAR]
        full_top_half.append(sand_top_line)
        for i in range(WIDTH // 2):
            new_line = [GAP_CHAR] * i + [WALL_CHAR] + [SAND_CHAR] * (WIDTH - (i + 1) * 2) + [WALL_CHAR] + [GAP_CHAR] * i
            full_top_half.append(new_line)

        return full_top_half

    def generate_empty_half(self):
        empty_top_half = [WIDTH * [WALL_CHAR]]
        for i in range(2):
            new_line = [WALL_CHAR] + [GAP_CHAR] * (WIDTH - 2) + [WALL_CHAR]
            empty_top_half.append(new_line)
        for i in range(WIDTH // 2):
            new_line = [GAP_CHAR] * i + [WALL_CHAR] + [GAP_CHAR] * (WIDTH - (i + 1) * 2) + [WALL_CHAR] + [GAP_CHAR] * i
            empty_top_half.append(new_line)

        return empty_top_half

    def get_height(self):
        return len(self.get_canvas())

    def get_canvas(self):
        return self.canvas

    def show_canvas(self):
        lines = [''.join(line) for line in self.get_canvas()]
        print('\n'.join(lines))

    def is_empty_cell(self, x, y):
        return self.canvas[y][x] == GAP_CHAR

    def is_wall_char(self, x, y):
        return self.canvas[y][x] == WALL_CHAR

    def update_sand_coords(self, sand, x, y):
        index = self.sand.index(sand)
        self.sand[index] = (y, x)

    def has_left_right_neighbours(self, x, y):
        has_left_neighbour = self.canvas[y][x - 1] is not GAP_CHAR
        has_right_neighbour = self.canvas[y][x + 1] is not GAP_CHAR

        return has_left_neighbour or has_right_neighbour

    def tick(self):
        for sand in self.sand:
            self.tick_sand(sand)
        random.shuffle(self.sand)

    def tick_sand(self, sand):
        y, x = sand
        new_x, new_y = x, y
        if self.check_if_can_fall_down(x, y):
            new_x, new_y = x, y + 1
        else:
            can_fall_down_left = self.check_if_can_fall_down_left(x, y)
            can_fall_down_right = self.check_if_can_fall_down_right(x, y)
            if can_fall_down_left and can_fall_down_right:
                direction = random.choice([-1, 1])
                new_x, new_y = x + direction, y + 1
            elif can_fall_down_left:
                new_x, new_y = x - 1, y + 1
            elif can_fall_down_right:
                new_x, new_y = x + 1, y + 1
        self.update_sand_coords(sand, new_x, new_y)
        self.update_canvas()

    def check_if_can_fall_down(self, x, y):
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        return self.is_empty_cell(bottom_neighbour_x, bottom_neighbour_y)

    def check_if_can_fall_down_left(self, x, y):
        left_neighbour_x, left_neighbour_y = x - 1, y
        is_wall_down_left = self.is_wall_char(left_neighbour_x, left_neighbour_y)
        if is_wall_down_left:
            return False
        bottom_left_neighbour_x, bottom_left_neighbour_y = x - 1, y + 1
        return self.is_empty_cell(bottom_left_neighbour_x, bottom_left_neighbour_y)

    def check_if_can_fall_down_right(self, x, y):
        right_neighbour_x, right_neighbour_y = x + 1, y
        is_wall_down_right = self.is_wall_char(right_neighbour_x, right_neighbour_y)
        if is_wall_down_right:
            return False
        bottom_right_neighbour_x, bottom_right_neighbour_y = x + 1, y + 1
        return self.is_empty_cell(bottom_right_neighbour_x, bottom_right_neighbour_y)

    def update_canvas(self):
        self.canvas = self.get_compiled_canvas()
