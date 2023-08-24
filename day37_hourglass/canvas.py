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
        self.bottleneck_x, self.bottleneck_y = self.get_bottleneck_coords()
        self.sand = []
        self.hourglass_outline = []
        self.init_sand()
        self.init_outline_coords()

    def get_initial_hourglass(self):
        top = self.get_full_top_half()
        bottom = self.get_empty_bottom_half()

        return self.get_hourglass(top, bottom)

    def get_bottleneck_coords(self):
        y = self.height // 2
        x = self.width // 2

        return y, x

    def all_sands_dropped(self):
        return all([self.is_in_bottom_half(sand) for sand in self.sand])

    def is_in_bottom_half(self, sand):
        y, x = sand
        return y > self.height // 2

    def draw_canvas(self):
        result = ''
        for i in range(self.height):
            line = ''
            for j in range(self.width):
                char = GAP_CHAR
                if (i, j) in self.hourglass_outline:
                    char = WALL_CHAR
                elif (i, j) in self.sand:
                    char = SAND_CHAR
                line += char
            result += '\n' + line
        print(result)

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

    def get_sand_to_drop_coords(self):
        return get_bottleneck_coords()

    def get_hourglass(self, top_half, bottom_half):
        return top_half + bottom_half[1:]

    def get_empty_top_half(self):
        return self.generate_empty_half()

    def get_empty_bottom_half(self):
        return list(reversed(self.get_empty_top_half()))

    def get_full_top_half(self):
        return self.generate_full_half()

    def get_full_bottom_half(self):
        return list(reversed(self.generate_full_half()))

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

    def tick(self):
        bottleneck_coords = self.get_bottleneck_coords()
        bottleneck_coord_y, bottleneck_coord_x = bottleneck_coords

        if (bottleneck_coord_y, bottleneck_coord_x) in self.sand:
            self.tick_top_middle_sand((bottleneck_coord_y, bottleneck_coord_x))

        top_half_sand = []
        bottom_half_sand = []
        for sand in self.sand:
            y, x = sand
            if y < bottleneck_coord_y:
                top_half_sand.append(sand)
            else:
                bottom_half_sand.append(sand)
        self.tick_top_half(top_half_sand)
        self.tick_bottom_half(bottom_half_sand)

    def tick_bottleneck_sand(self):
        pass

    def tick_top_half(self, top_half_sand):
        top_half_sand.sort()
        for sand in top_half_sand:
            y, x = sand
            if x < self.middle_x:
                self.tick_top_sand_down_right(sand)
            elif x > self.middle_x:
                self.tick_top_sand_down_left(sand)
            else:
                self.tick_top_middle_sand(sand)
            self.update_canvas()

    def tick_bottom_half(self, bottom_half_sand):
        bottom_half_sand.sort()
        for sand in bottom_half_sand:
            y, x = sand
            if x < self.middle_x:
                self.tick_bottom_sand_down_left(sand)
            elif x > self.middle_x:
                self.tick_bottom_sand_down_right(sand)
            else:
                self.tick_bottom_sand(sand)
            self.update_canvas()

    def update_canvas(self):
        self.canvas = self.get_compiled_canvas()

    def tick_top_sand_down_right(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        bottom_right_neighbour_x, bottom_right_neighbour_y = x + 1, y + 1
        bottom_right_neighbour = self.canvas[bottom_right_neighbour_y][bottom_right_neighbour_x]

        if self.is_empty_cell(bottom_neighbour_x, bottom_neighbour_y):
            self.update_sand_coords(sand, bottom_neighbour_x, bottom_neighbour_y)
        elif self.is_empty_cell(bottom_right_neighbour_x, bottom_right_neighbour_y):
            self.update_sand_coords(sand, bottom_right_neighbour_x, bottom_right_neighbour_y)

    def tick_top_sand_down_left(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        bottom_left_neighbour_x, bottom_left_neighbour_y = x - 1, y + 1
        bottom_left_neighbour = self.canvas[bottom_left_neighbour_y][bottom_left_neighbour_x]

        if self.is_empty_cell(bottom_neighbour_x, bottom_neighbour_y):
            self.update_sand_coords(sand, bottom_neighbour_x, bottom_neighbour_y)
        elif self.is_empty_cell(bottom_left_neighbour_x, bottom_left_neighbour_y):
            self.update_sand_coords(sand, bottom_left_neighbour_x, bottom_left_neighbour_y)

    def tick_top_middle_sand(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        if bottom_neighbour is GAP_CHAR:
            self.update_sand_coords(sand, x, y + 1)

    def tick_bottom_sand_down_right(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        bottom_right_neighbour_x, bottom_right_neighbour_y = x + 1, y + 1
        bottom_right_neighbour = self.canvas[bottom_right_neighbour_y][bottom_right_neighbour_x]

        if self.is_empty_cell(bottom_neighbour_x, bottom_neighbour_y):
            self.update_sand_coords(sand, bottom_neighbour_x, bottom_neighbour_y)
        elif self.is_empty_cell(bottom_right_neighbour_x, bottom_right_neighbour_y):
            self.update_sand_coords(sand, bottom_right_neighbour_x, bottom_right_neighbour_y)

    def tick_bottom_sand_down_left(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        bottom_left_neighbour_x, bottom_left_neighbour_y = x - 1, y + 1
        bottom_left_neighbour = self.canvas[bottom_left_neighbour_y][bottom_left_neighbour_x]

        if self.is_empty_cell(bottom_neighbour_x, bottom_neighbour_y):
            self.update_sand_coords(sand, bottom_neighbour_x, bottom_neighbour_y)
        elif self.is_empty_cell(bottom_left_neighbour_x, bottom_left_neighbour_y):
            self.update_sand_coords(sand, bottom_left_neighbour_x, bottom_left_neighbour_y)

    def tick_bottom_sand(self, sand):
        y, x = sand
        bottom_neighbour_x, bottom_neighbour_y = x, y + 1
        bottom_neighbour = self.canvas[bottom_neighbour_y][bottom_neighbour_x]
        if bottom_neighbour is GAP_CHAR:
            self.update_sand_coords(sand, x, y + 1)
            return
        elif bottom_neighbour is WALL_CHAR:
            return
        if self.has_left_right_neighbours(bottom_neighbour_x, bottom_neighbour_y):
            return
        fall_right = random.randint(1, 2) % 2 == 0
        if fall_right:
            if self.is_empty_cell(x + 1, y + 1):
                self.update_sand_coords(sand, x + 1, y + 1)
        else:
            if self.is_empty_cell(x - 1, y + 1):
                self.update_sand_coords(sand, x - 1, y + 1)

    def is_empty_cell(self, x, y):
        return self.canvas[y][x] == GAP_CHAR

    def update_sand_coords(self, sand, x, y):
        index = self.sand.index(sand)
        self.sand[index] = (y, x)

    def has_left_right_neighbours(self, x, y):
        has_left_neighbour = self.canvas[y][x - 1] is not GAP_CHAR
        has_right_neighbour = self.canvas[y][x + 1] is not GAP_CHAR

        return has_left_neighbour or has_right_neighbour

#hourglass = Hourglass()
#while True:
#    hourglass.show_canvas()
#    hourglass.tick()
#    time.sleep(0.1)
