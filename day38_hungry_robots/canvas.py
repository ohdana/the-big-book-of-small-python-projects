import random

WIDTH = 30
HEIGHT = 20
NUM_WALLS = 100
EMPTY_CHAR = ' '
PLAYER_CHAR = '@'
ROBOT_CHAR = 'R'
DEAD_ROBOT_CHAR = 'X'
WALL_CHAR = chr(9617)  # Character 9617 is '░'

class Canvas:
    def __init__(self):
        self.canvas = self.generate_initial_canvas()
        self.allocate_walls()
        #self.allocate_robots()
        #self.allocate_player()

    def generate_initial_canvas(self):
        canvas = []
        for i in range(HEIGHT):
            new_line = []
            for j in range(WIDTH):
                new_line.append(EMPTY_CHAR)
            canvas.append(new_line)
        return canvas

    def allocate_walls(self):
        self.add_frame()
        for i in range(NUM_WALLS):
            x, y = self.get_random_empty_cell()
            self.update_cell(WALL_CHAR, x, y)

    def get_random_empty_cell(self):
        random_x = random.randint(0, WIDTH - 1)
        random_y = random.randint(0, HEIGHT - 1)
        if not self.is_empty(random_x, random_y):
            return self.get_random_empty_cell()
        return random_x, random_y

    def add_frame(self):
        self.canvas[0] = [WALL_CHAR] * WIDTH
        for line in self.canvas:
            line[0] = WALL_CHAR
            line[WIDTH - 1] = WALL_CHAR
        self.canvas[HEIGHT - 1] = [WALL_CHAR] * WIDTH

    def update_cell(self, char, x, y):
        self.canvas[y][x] = char

    def allocate_robots(self):
        pass

    def allocate_player(self):
        pass

    def is_empty(self, x, y):
        return self.canvas[y][x] == EMPTY_CHAR

    def is_wall(self, x, y):
        return self.canvas[y][x] == WALL_CHAR

    def is_robot(self, x, y):
        return self.canvas[y][x] in [ROBOT_CHAR, DEAD_ROBOT_CHAR]

    def is_player(self, x, y):
        return self.canvas[y][x] == PLAYER_CHAR

    def show_canvas(self):
        lines = [''.join(line) for line in self.canvas]
        print('\n'.join(lines))

canvas = Canvas()
canvas.show_canvas()
