import random

PATTERN = '''
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
'''
EMPTY = '  '
WINNING_ORDER = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15']
WIDTH, HEIGHT = 4, 4
W, A, S, D = 'W', 'A', 'S', 'D'
DIRECTIONS = [W, A, S, D]

class GameEngine:
    def __init__(self):
        pass

    def start_game(self):
        self.init_canvas()

    def move(self, direction):
        if direction not in DIRECTIONS:
            return
        tile_to_move  = self.get_tile_to_move(direction)
        tile_to_move_value, tile_to_move_coords = tile_to_move
        self.swap_tiles(self.empty_tile, tile_to_move_coords)
        self.empty_tile = tile_to_move_coords

    def get_available_moves(self):
        neighbours = self.get_neighbours(*(self.empty_tile))

        return [direction for direction in neighbours.keys() if neighbours[direction][0]]

    def is_win(self):
        current_state = self.get_flat_list(self.canvas)
        for i in range(len(WINNING_ORDER)):
            if current_state[i] != WINNING_ORDER[i]:
                return False

        return True

    def get_tile_to_move(self, direction):
        x, y = self.empty_tile
        if direction == W:
            return self.get_bottom_neighbour(x, y)
        elif direction == A:
            return self.get_right_neighbour(x, y)
        elif direction == S:
            return self.get_top_neighbour(x, y)
        elif direction == D:
            return self.get_left_neighbour(x, y)

    def swap_tiles(self, tile_1, tile_2):
        x1, y1 = tile_1
        x2, y2 = tile_2
        self.canvas[y1][x1], self.canvas[y2][x2] = self.canvas[y2][x2], self.canvas[y1][x1]

    def show_canvas(self):
        formatting_params = self.get_flat_list(self.canvas)
        print(PATTERN.format(*formatting_params))

    def get_neighbours(self, x, y):
        left = self.get_left_neighbour(x, y)
        top = self.get_top_neighbour(x, y)
        right = self.get_right_neighbour(x, y)
        bottom = self.get_bottom_neighbour(x, y)

        return { D: left, S: top, A: right, W: bottom }

    def get_left_neighbour(self, x, y):
        return self.get_cell(x - 1, y), (x - 1, y)

    def get_top_neighbour(self, x, y):
        return self.get_cell(x, y - 1), (x, y - 1)

    def get_right_neighbour(self, x, y):
        return self.get_cell(x + 1, y), (x + 1, y)

    def get_bottom_neighbour(self, x, y):
        return self.get_cell(x, y + 1), (x, y + 1)

    def get_cell(self, x, y):
        if x < 0 or x >= WIDTH:
            return None

        if y < 0 or y >= HEIGHT:
            return None

        return self.canvas[y][x]

    def init_empty_canvas(self):
        self.canvas = []
        for j in range(HEIGHT):
            new_line = [EMPTY] * WIDTH
            self.canvas.append(new_line)

    def shuffle_canvas(self):
        n_of_random_moves = 300
        for i in range(n_of_random_moves):
            self.make_random_move()

    def make_random_move(self):
        available_directions = self.get_available_moves()
        random_direction = random.choice(available_directions)
        self.move(random_direction)

    def init_canvas(self):
        self.init_empty_canvas()
        self.fill_canvas_with_winning_order()
        self.shuffle_canvas()

    def fill_canvas_with_winning_order(self):
        tiles = WINNING_ORDER + [EMPTY]
        for j in range(HEIGHT):
            for i in range(WIDTH):
                tile = tiles.pop()
                self.canvas[j][i] = tile
                if tile == EMPTY:
                    self.empty_tile = (i, j)

    def get_flat_list(self, matrix):
        return [item for row in matrix for item in row]
