import random

INITIAL_NUM_ALIVE_ROBOTS = 10
INITIAL_NUM_DEAD_ROBOTS = 2
INITIAL_NUM_TELEPORTS = 2

WIDTH = 30
HEIGHT = 20
NUM_WALLS = 100
EMPTY_CHAR = ' '
PLAYER_CHAR = '@'
ROBOT_CHAR = 'R'
DEAD_ROBOT_CHAR = 'X'
WALL_CHAR = chr(9617)  # Character 9617 is '░'

class Canvas:
    def __init__(self, n_of_alive_robots, n_of_dead_robots, n_of_teleport):
        self.n_of_alive_robots = n_of_alive_robots
        self.n_of_dead_robots = n_of_dead_robots
        self.n_of_teleport = n_of_teleport
        self.allocate_objects()

    def allocate_objects(self):
        self.walls = []
        self.alive_robots = []
        self.dead_robots = []
        self.player = None
        self.allocate_walls()
        self.allocate_robots()
        self.allocate_player()

    def move_robots(self):
        pass

    def crash_robot(self, robot):
        pass

    def get_random_empty_cell(self):
        random_x = random.randint(0, WIDTH - 1)
        random_y = random.randint(0, HEIGHT - 1)
        if not self.is_empty(random_x, random_y):
            return self.get_random_empty_cell()
        return random_x, random_y

    def add_frame(self):
        for i in range(WIDTH):
            self.walls.append((i, 0))
            self.walls.append((i, HEIGHT - 1))

        for j in range(HEIGHT):
            self.walls.append((0, j))
            self.walls.append((WIDTH - 1, j))

    def update_cell(self, char, x, y):
        self.canvas[y][x] = char

    def allocate_walls(self):
        self.add_frame()
        for i in range(NUM_WALLS):
            x, y = self.get_random_empty_cell()
            self.walls.append((x, y))

    def allocate_robots(self):
        self.allocate_alive_robots()
        self.allocate_dead_robots()

    def allocate_alive_robots(self):
        for i in range(self.n_of_alive_robots):
            x, y = self.get_random_empty_cell()
            self.alive_robots.append((x, y))

    def allocate_dead_robots(self):
        for i in range(self.n_of_dead_robots):
            x, y = self.get_random_empty_cell()
            self.dead_robots.append((x, y))

    def allocate_player(self):
        x, y = self.get_random_empty_cell()
        self.player = (x, y)

    def is_empty(self, x, y):
        return not (self.is_wall(x, y) or self.is_robot(x, y) or self.is_player(x, y))

    def is_wall(self, x, y):
        return (x, y) in self.walls

    def is_robot(self, x, y):
        return (x, y) in (self.alive_robots + self.dead_robots)

    def is_player(self, x, y):
        return (x, y) == self.player

    def get_char(self, x, y):
        if (x, y) == self.player:
            return PLAYER_CHAR
        elif (x, y) in self.alive_robots:
            return ROBOT_CHAR
        elif (x, y) in self.dead_robots:
            return DEAD_ROBOT_CHAR
        elif (x, y) in self.walls:
            return WALL_CHAR
        else:
            return EMPTY_CHAR

    def generate_canvas_with_objects(self):
        canvas = []
        for i in range(HEIGHT):
            new_line = []
            for j in range(WIDTH):
                char = self.get_char(j, i)
                new_line.append(char)
            canvas.append(new_line)
        return canvas

    def get_canvas(self):
        canvas = self.generate_canvas_with_objects()
        lines = [''.join(line) for line in canvas]
        return '\n'.join(lines)

    def show_canvas(self):
        print(self.get_canvas())

canvas = Canvas(INITIAL_NUM_ALIVE_ROBOTS, INITIAL_NUM_DEAD_ROBOTS, INITIAL_NUM_TELEPORTS)
canvas.show_canvas()
