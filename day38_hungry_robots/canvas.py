import random, math, time

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
CALCULATE_COORDS_MAP = {}
Q, W, E, D, C, X, A, Z = 'Q', 'W', 'E', 'D', 'C', 'X', 'A', 'Z'
DIRECTIONS = [Q, W, E, D, C, X, A, Z]

class Canvas:
    def __init__(self, n_of_alive_robots, n_of_dead_robots, n_of_teleport):
        self.n_of_alive_robots = n_of_alive_robots
        self.n_of_dead_robots = n_of_dead_robots
        self.n_of_teleport = n_of_teleport
        self.player_eaten = False
        self.allocate_objects()
        self.init_calculate_coords_map()

    def allocate_objects(self):
        self.walls, self.alive_robots, self.dead_robots = [], [], []
        self.player = None
        self.allocate_walls()
        self.allocate_robots()
        self.allocate_player()

    def get_player_available_directions(self):
        x, y = self.player
        return self.get_available_directions(x, y)

    def get_available_directions(self, x, y):
        direction_coords_map = {}
        for direction in DIRECTIONS:
            new_x, new_y = CALCULATE_COORDS_MAP[direction](x, y)
            if self.is_wall(new_x, new_y):
                continue
            direction_coords_map[direction] = (new_x, new_y)

        return direction_coords_map

    def is_player_eaten(self):
        return self.player_eaten

    def are_all_robots_dead(self):
        return len(self.alive_robots) == 0

    def move_robots(self):
        for robot in self.alive_robots:
            self.move_robot(robot)

    def move_robot(self, robot):
        direction = self.choose_robot_direction(robot)
        robot_index = self.alive_robots.index(robot)
        new_robot_coords = CALCULATE_COORDS_MAP[direction](*robot)
        if self.is_robot(*new_robot_coords):
            self.crash_robot(robot)
            return
        elif self.is_player(*new_robot_coords):
            self.player_eaten = True
        self.alive_robots[robot_index] = new_robot_coords

    def choose_robot_direction(self, robot):
        x, y = robot
        direction_distance_map = {}
        available_directions = self.get_available_directions(x, y)
        for direction in available_directions.keys():
            new_x, new_y = available_directions[direction]
            direction_distance_map[direction] = self.get_crowfly_distance_to_player(new_x, new_y)

        return self.get_min_value_key(direction_distance_map)

    def get_min_value_key(self, dictionary):
        min_value = min(dictionary.values())
        min_value_keys = [key for key in dictionary if dictionary[key] == min_value]

        return random.choice(min_value_keys)

    def get_crowfly_distance_to_player(self, x, y):
        player_x, player_y = self.player
        return math.sqrt((player_x - x)**2 + (player_y - y)**2)

    def move_player(self, direction):
        if direction.upper() not in DIRECTIONS:
            return
        new_x, new_y = CALCULATE_COORDS_MAP[direction.upper()](*self.player)
        if self.is_empty(new_x, new_y):
            self.player = (new_x, new_y)

    def get_n_of_teleport(self):
        return self.n_of_teleport

    def teleport(self):
        if self.n_of_teleport < 1:
            return
        new_x, new_y = self.get_random_empty_cell()
        self.player = (new_x, new_y)
        self.n_of_teleport -= 1

    def crash_robot(self, robot):
        if robot in self.alive_robots:
            self.alive_robots.remove(robot)
            self.dead_robots.append(robot)

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

    def get_canvas(self):
        canvas = self.generate_canvas_with_objects()
        lines = [''.join(line) for line in canvas]
        return '\n'.join(lines)

    def show_canvas(self):
        print(self.get_canvas())

    def init_calculate_coords_map(self):
        CALCULATE_COORDS_MAP[Q] = self.q
        CALCULATE_COORDS_MAP[W] = self.w
        CALCULATE_COORDS_MAP[E] = self.e
        CALCULATE_COORDS_MAP[D] = self.d
        CALCULATE_COORDS_MAP[C] = self.c
        CALCULATE_COORDS_MAP[X] = self.x
        CALCULATE_COORDS_MAP[A] = self.a
        CALCULATE_COORDS_MAP[Z] = self.z

    def q(self, x, y):
        return x - 1, y - 1
    def w(self, x, y):
        return x, y - 1
    def e(self, x, y):
        return x + 1, y - 1
    def d(self, x, y):
        return x + 1, y
    def c(self, x, y):
        return x + 1, y + 1
    def x(self, x, y):
        return x, y + 1
    def a(self, x, y):
        return x - 1, y
    def z(self, x, y):
        return x - 1, y + 1

#canvas = Canvas(INITIAL_NUM_ALIVE_ROBOTS, INITIAL_NUM_DEAD_ROBOTS, INITIAL_NUM_TELEPORTS)
#while True:
#    canvas.show_canvas()
#    canvas.move_robots()
#    time.sleep(0.5)
