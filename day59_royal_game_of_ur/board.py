PATTERN = '''
                    {}              {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|*{}*< {} < {} < {} |           |*{}*< {} |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
| {} > {} > {} >*{}*> {} > {} > {} > {} |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|*{}*< {} < {} < {} |           |*{}*< {} |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                    {}              {}
'''
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
CELLS = [H, G, F, E, T, S, I, J, K, L, M, N, O, P, D, C, B, A, R, Q]
O_TOKEN, X_TOKEN = 'O', 'X'
TOKEN_TYPES = [O_TOKEN, X_TOKEN]
N_OF_TOKENS_PER_PLAYER = 7
NO_TOKEN = ' '
HOME, GOAL = 'home', 'goal'
PATH_O = [HOME, A, B, C, D, I, J, K, L, M, N, O, P, Q, R, GOAL]
PATH_X = [HOME, E, F, G, H, I, J, K, L, M, N, O, P, S, T, GOAL]
TOKEN_TYPE_PATH_MAP = { O_TOKEN: PATH_O, X_TOKEN: PATH_X }
FLOWERS_CELLS = [D, H, L, R, T]
MIDDLE_FLOWER_CELL = L

class Board:
    def __init__(self):
        self.tokens_map = self.init_tokens_map(TOKEN_TYPES)
        self.init_tokens(TOKEN_TYPES, N_OF_TOKENS_PER_PLAYER)

    def is_middle_flower_cell(self, cell):
        return cell == MIDDLE_FLOWER_CELL

    def is_flower_cell(self, cell):
        return cell in FLOWERS_CELLS

    def get_tokens_to_move(self, token_type):
        unique_token_cells = set(self.tokens_map[token_type])
        return [self.get_display_cell_name(cell) for cell in unique_token_cells if cell != GOAL]

    def is_available_middle_flower_cell(self, my_token_type):
        opponent_token_type = self.get_opponent_token_type(my_token_type)
        if MIDDLE_FLOWER_CELL in self.tokens_map[opponent_token_type]:
            return False
        return True

    def get_display_cell_name(self, cell):
        if HOME in cell:
            return HOME
        if GOAL in cell:
            return GOAL
        return cell

    def get_dest_cell(self, token_type, src_cell, n_of_steps):
        path = TOKEN_TYPE_PATH_MAP[token_type]
        src_cell_index_in_path = path.index(src_cell)
        dest_cell_index_in_path = src_cell_index_in_path + n_of_steps
        if dest_cell_index_in_path >= len(path):
            dest_cell_index_in_path = len(path) - 1

        return path[dest_cell_index_in_path]

    def init_tokens_map(self, token_types):
        tokens_map = {}
        for token_type in token_types:
            tokens_map[token_type] = []
        return tokens_map

    def are_all_tokens_at_goal(self, token_type):
        token_type_cells = self.tokens_map[token_type]

        return all([cell == GOAL for cell in token_type_cells])

    def make_move(self, token_type, src_cell, n_of_steps):
        dest_cell = self.get_dest_cell(token_type, src_cell, n_of_steps)
        self.send_opponent_tokens_home(token_type, dest_cell)
        self.move_token(token_type, src_cell, dest_cell)

        return dest_cell

    def send_opponent_tokens_home(self, my_token_type, cell):
        if cell == HOME or cell == GOAL:
            return
        opponent_token_type = self.get_opponent_token_type(my_token_type)
        opponent_cells = self.tokens_map[opponent_token_type]
        while cell in opponent_cells:
            self.send_token_home(opponent_token_type, cell)

    def get_opponent_token_type(self, my_token_type):
        if my_token_type is O_TOKEN:
            return X_TOKEN

        return O_TOKEN

    def move_token(self, token_type, src_cell, dest_cell):
        token_type_cells = self.tokens_map[token_type]
        if src_cell in token_type_cells:
            token_type_cells.remove(src_cell)
        token_type_cells.append(dest_cell)

    def send_token_home(self, token_type, src_cell=None):
        self.move_token(token_type, src_cell, HOME)

    def init_tokens(self, token_types, n_of_tokens_per_player):
        for token_type in token_types:
            self.init_tokens_of_type(token_type, n_of_tokens_per_player)

    def init_tokens_of_type(self, token_type, n_of_tokens):
        for i in range(n_of_tokens):
            self.send_token_home(token_type)

    def build(self):
        x_home_goal = self.get_home_goal_formatted_token_count(X_TOKEN)
        o_home_goal = self.get_home_goal_formatted_token_count(O_TOKEN)
        formatting_params = x_home_goal + [self.get_token_for_cell(cell) for cell in CELLS] + o_home_goal
        return PATTERN.format(*formatting_params)

    def get_home_goal_formatted_token_count(self, token_type):
        home_count = self.tokens_map[token_type].count(HOME)
        goal_count = self.tokens_map[token_type].count(GOAL)
        return [self.get_formatted_token_count(token_type, home_count), self.get_formatted_token_count(token_type, goal_count)]

    def get_formatted_token_count(self, token_type, token_count):
        if not token_count:
            token_type = NO_TOKEN
        elif token_count > 1:
            return '{}x{}'.format(token_count, token_type)

        return ' {} '.format(token_type)

    def get_token_for_cell(self, cell):
        x_cells = self.tokens_map[X_TOKEN]
        o_cells = self.tokens_map[O_TOKEN]
        token_type = NO_TOKEN
        token_count = 0

        if cell in x_cells:
            token_type = X_TOKEN
            token_count = x_cells.count(cell)

        if cell in o_cells:
            token_type = O_TOKEN
            token_count = o_cells.count(cell)

        return self.get_formatted_token_count(token_type, token_count)
