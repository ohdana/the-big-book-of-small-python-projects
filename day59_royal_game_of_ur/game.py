from coin import Coin
from player import Player
from board import Board

N_OF_COINS = 4
HEADS, TAILS = 'HEADS', 'TAILS'
O_TOKEN, X_TOKEN = 'O', 'X'
TOKEN_TYPES = [O_TOKEN, X_TOKEN]

class Game:
    def __init__(self):
        self.init_game()

    def is_flower_cell(self, cell):
        return self.board.is_flower_cell(cell)

    def got_extra_move(self, dest_cell):
        return self.is_flower_cell(dest_cell)

    def init_game(self):
        self.coins = self.get_coins(N_OF_COINS)
        self.players = self.get_players(TOKEN_TYPES)
        self.board = Board()
        self.turn = 0
        self.last_move = None

    def get_tokens_to_move(self, token_type, n_of_steps):
        tokens = self.board.get_tokens_to_move(token_type)
        for src_cell in tokens:
            dest_cell = self.board.get_dest_cell(token_type, src_cell, n_of_steps)
            if self.board.is_middle_flower_cell(dest_cell):
                if not self.board.is_available_middle_flower_cell(token_type):
                    tokens.remove(src_cell)

        return tokens

    def get_board_image(self):
        return self.board.build()

    def is_winner(self, token_type):
        return self.board.are_all_tokens_at_goal(token_type)

    def make_move(self, token_type, src_cell, n_of_steps):
        dest_cell = self.board.make_move(token_type, src_cell, n_of_steps)
        self.set_last_move(token_type, dest_cell)

        return dest_cell

    def set_last_move(self, token_type, dest_cell):
        self.last_move = (token_type, dest_cell)

    def calculate_next_turn(self):
        player, cell = self.last_move
        if self.board.is_flower_cell(cell):
            return

        self.pass_turn()

    def pass_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def get_player_for_turn(self):
        return self.players[self.turn].get_token_type()

    def get_coins(self, n_of_coins):
        return [Coin() for x in range(n_of_coins)]

    def get_players(self, token_types):
        return [Player(token_type) for token_type in token_types]

    def flip_coins(self):
        coins_flip_result = [coin.flip() for coin in self.coins]
        heads = [coin_side for coin_side in coins_flip_result if coin_side is HEADS]

        return coins_flip_result, len(heads)
