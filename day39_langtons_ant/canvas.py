import random, time, copy

FRAME_CHAR = '.'
WHITE_CELL = ' '
BLACK_CELL = chr(9618) # Character 9618 is '▒'
UP, RIGHT, DOWN, LEFT = '^', '>', 'v', '<'
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
ANT_DIRECTION_MAP = {}

class Canvas:
    def __init__(self, width, height, n_of_ants):
        self.init_ant_direction_map()
        self.width = width
        self.height = height
        self.init_ants(n_of_ants)
        self.black_cells = []

    def init_ants(self, n_of_ants):
        self.ants = {}
        self.allocate_ants(n_of_ants)

    def allocate_ants(self, n_of_ants):
        for i in range(n_of_ants):
            x, y = self.get_random_empty_cell()
            direction = random.choice(DIRECTIONS)
            self.ants[(x, y)] = direction

    def get_random_empty_cell(self):
        random_x = random.randint(0, self.width - 1)
        random_y = random.randint(0, self.height - 1)
        if not self.is_empty(random_x, random_y):
            return self.get_random_empty_cell()
        return random_x, random_y

    def get_canvas(self):
        canvas = self.generate_canvas()
        lines = [''.join(line) for line in canvas]
        return '\n'.join(lines)

    def is_empty(self, x, y):
        return not self.is_ant(x, y)

    def generate_canvas(self):
        canvas = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                char = self.get_char(j, i)
                new_line.append(char)
            canvas.append(new_line)

        self.add_frame(canvas)
        return canvas

    def is_black_cell(self, x, y):
        return (x, y) in self.black_cells

    def turn_clockwise(self, ant):
        new_char_index = (DIRECTIONS.index(self.ants[ant]) + 1 + len(DIRECTIONS)) % len(DIRECTIONS)
        new_ant_char = DIRECTIONS[new_char_index]
        self.ants[ant] = new_ant_char

    def turn_counterclockwise(self, ant):
        new_char_index = (DIRECTIONS.index(self.ants[ant]) - 1 + len(DIRECTIONS)) % len(DIRECTIONS)
        new_ant_char = DIRECTIONS[new_char_index]
        self.ants[ant] = new_ant_char

    def turn_180(self, ant):
        new_char_index = (DIRECTIONS.index(self.ants[ant]) + 2 + len(DIRECTIONS)) % len(DIRECTIONS)
        new_ant_char = DIRECTIONS[new_char_index]
        self.ants[ant] = new_ant_char

    def add_frame(self, canvas):
        canvas.insert(0, [FRAME_CHAR] * self.width)
        canvas.append([FRAME_CHAR] * self.width)
        for line in canvas:
            line[0] = FRAME_CHAR
            line[self.width - 1] = FRAME_CHAR

    def show_canvas(self):
        print(self.get_canvas())

    def get_char(self, x, y):
        if self.is_ant(x, y):
            return self.ants[(x, y)]
        elif (x, y) in self.black_cells:
            return BLACK_CELL
        else:
            return WHITE_CELL

    def is_ant(self, x, y):
        return (x, y) in self.ants.keys()

    def tick(self):
        ants_deep_copy = copy.deepcopy(self.ants)
        for ant in ants_deep_copy:
            self.tick_ant(ant)

    def tick_ant(self, ant):
        if self.is_black_cell(*ant):
            self.turn_counterclockwise(ant)
        else:
            self.turn_clockwise(ant)
        self.flip_cell_colour(*ant)
        self.make_step_forward(ant)

    def make_step_forward(self, ant):
        ant_char = self.ants[ant]
        new_coords = ANT_DIRECTION_MAP[ant_char](*ant)
        if not self.is_valid_coords(*new_coords):
            self.turn_180(ant)
        old_ant = self.ants.pop(ant)
        self.ants[new_coords] = old_ant

    def is_valid_coords(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False

        return True

    def flip_cell_colour(self, x, y):
        if self.is_black_cell(x, y):
            self.black_cells.remove((x, y))
        else:
            self.black_cells.append((x, y))

    def up(self, x, y):
        return (x, y - 1)

    def down(self, x, y):
        return (x, y + 1)

    def left(self, x, y):
        return (x - 1, y)

    def right(self, x, y):
        return (x + 1, y)

    def init_ant_direction_map(self):
        ANT_DIRECTION_MAP[UP] = self.up
        ANT_DIRECTION_MAP[DOWN] = self.down
        ANT_DIRECTION_MAP[LEFT] = self.left
        ANT_DIRECTION_MAP[RIGHT] = self.right
