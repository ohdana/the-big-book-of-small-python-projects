SAND_CHAR = chr(9618)  # Character 9617 is '▒'
WALL_CHAR = chr(9608)  # Character 9608 is '█'
GAP_CHAR = ' '
WIDTH = 19

class Hourglass:
    def __init__(self):
        self.width = WIDTH
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

    def drop_new_sand(self):
        if self.all_sands_dropped():
            return

        self.update_new_sand_to_drop_coords()
        self.adjust_sand_rest()

    def adjust_sand_rest(self):
        sand_to_fall = self.get_sand_to_fall()
        #sand_to_fall_index = self.sand.index(sand_to_fall)
        #self.sand[sand_to_fall_index] = self.get_bottleneck_coords()

    def get_sand_to_fall(self):
        canvas = self.get_compiled_canvas()
        topmost_sand_y = self.get_topmost_sand_y()
        topmost_sand_no_gaps_line_y = self.get_topmost_sand_no_gaps_line_y(canvas)
        funnel_depth = topmost_sand_no_gaps_line_y - topmost_sand_y
        if funnel_depth > 2:
            self.remove_sand_from_side(canvas, topmost_sand_y, topmost_sand_no_gaps_line_y)
        else:
            self.remove_sand_from_center(canvas, topmost_sand_y, topmost_sand_no_gaps_line_y)

    def get_topmost_sand_no_gaps_line_y(self, canvas):
        result = 0
        for i in range(len(canvas)):
            line = canvas[i]
            if not any([char == SAND_CHAR for char in line]):
                continue
            left_wall_x = line.index(WALL_CHAR) + 1
            right_wall_x = line[left_wall_x:].index(WALL_CHAR) + left_wall_x
            between_walls = line[left_wall_x:right_wall_x]
            all_sand_between_walls = all([char == SAND_CHAR for char in  between_walls])
            if all_sand_between_walls:
                return i

    def get_topmost_sand_y(self):
        return min([y for y, x in self.sand])

    def update_new_sand_to_drop_coords(self):
        bottleneck_coords = self.get_bottleneck_coords()
        bottleneck_cell_index = self.sand.index(bottleneck_coords)
        bottleneck_coord_y, bottleneck_coord_x = bottleneck_coords
        self.sand[bottleneck_cell_index] = (bottleneck_coord_y + 1, bottleneck_coord_x)

hourglass = Hourglass()
hourglass.drop_new_sand()
canvas = hourglass.get_compiled_canvas()
hourglass.canvas = canvas
hourglass.show_canvas()
