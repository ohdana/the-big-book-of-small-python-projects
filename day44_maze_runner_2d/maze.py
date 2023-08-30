import copy

EMPTY_CHAR = ' '
WALL_CHAR = '#'
EXIT_CHAR = 'E'
START_CHAR = 'S'
PLAYER_CHAR = '@'
DIRECTION_COORDS_MAP = {}
W, A, S, D = 'W', 'A', 'S', 'D'

class Maze:
    def __init__(self, filename):
        self.init_direction_coords_map()
        self.canvas = self.get_maze(filename)
        self.set_width_height()
        self.set_start_exit_coords()
        self.player = self.start

    def show_canvas(self):
        canvas = self.get_canvas_with_player()
        lines = [''.join(line) for line in canvas]
        print(''.join(lines))

    def get_canvas_with_player(self):
        player_x, player_y = self.player
        canvas = copy.deepcopy(self.canvas)
        canvas[player_y][player_x] = PLAYER_CHAR

        return canvas

    def get_maze(self, filename):
        maze_file = open(filename, "r")
        return [[*line] for line in maze_file]

    def is_completed(self):
        return self.player == self.end

    def make_step(self, direction):
        new_x, new_y = DIRECTION_COORDS_MAP[direction](*self.player)
        self.player = (new_x, new_y)

    def move(self, direction):
        while self.is_available_direction(*self.player, direction):
            self.make_step(direction)

    def is_empty(self, x, y):
        return self.canvas[y][x] != WALL_CHAR

    def get_available_directions(self):
        player_x, player_y = self.player
        all_directions = [W, A, S, D]
        available_directions = [direction for direction in all_directions if self.is_available_direction(player_x, player_y, direction)]

        return available_directions

    def is_available_direction(self, x, y, direction):
        new_x, new_y = DIRECTION_COORDS_MAP[direction](x, y)
        if self.out_of_bounds(new_x, new_y):
            return False

        if not self.is_empty(new_x, new_y):
            return False

        return True

    def set_width_height(self):
        self.height = len(self.canvas)
        self.width = len(self.canvas[0])

    def set_start_exit_coords(self):
        self.start, self.end = None, None
        for y in range(self.height):
            for x in range(self.width):
                if self.canvas[y][x] == START_CHAR:
                    self.start = (x, y)
                elif self.canvas[y][x] == EXIT_CHAR:
                    self.end = (x, y)
                if self.start and self.end:
                    break

    def out_of_bounds(self, x, y):
        if x < 0 or y < 0:
            return True

        if x >= self.width or y >= self.height:
            return True

        return False

    def w(self, x, y):
        return x, y - 1

    def a(self, x, y):
        return x - 1, y

    def s(self, x, y):
        return x, y + 1

    def d(self, x, y):
        return x + 1, y

    def init_direction_coords_map(self):
        DIRECTION_COORDS_MAP[W] = self.w
        DIRECTION_COORDS_MAP[A] = self.a
        DIRECTION_COORDS_MAP[S] = self.s
        DIRECTION_COORDS_MAP[D] = self.d

maze = Maze('maze11x11s1.txt')
