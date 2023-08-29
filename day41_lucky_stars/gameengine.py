from turn import Turn

WINNING_SCORE = 13

class GameEngine:
    def __init__(self):
        pass

    def start_new_game(self, player_names):
        self.player_names = player_names
        self.init_player_scores_map()
        self.game_over = False

    def get_scores(self):
        return self.player_scores

    def is_over(self):
        return self.game_over

    def play(self):
        turn = 0
        while not self.game_over:
            player_name = self.player_names[turn]
            self.take_turn(player_name)
            turn = self.calculate_next_turn(turn)
            self.show_current_scores()
            if self.reached_winning_score(player_name):
                self.do_last_round(player_name)
                self.game_over = True

    def show_current_scores(self):
        scores = []
        for player in self.player_scores.keys():
            scores.append('{} = {}'.format(player, self.player_scores[player]))
        print('SCORES: \n{}'.format(' '.join(scores)))

    def take_turn(self, player_name):
        print('It is {}\'s turn.'.format(player_name))
        turn = Turn(player_name)
        while not turn.is_over():
            turn.play()
        points_collected = turn.get_points_collected()
        self.update_player_score(player_name, points_collected)
        print('{} got {} stars!'.format(player_name, points_collected))

    def reached_winning_score(self, player_name):
        return self.player_scores[player_name] >= WINNING_SCORE

    def do_last_round(self, player_name):
        print('{} has reached 13 points!!! Everyone else will get one more turn!'.format(player_name))
        input('Press Enter to continue...')
        last_round_players = [name for name in self.player_names if name is not player_name]
        for player in last_round_players:
            self.take_turn(player_name)

    def update_player_score(self, player_name, points):
        self.player_scores[player_name] += points

    def calculate_next_turn(self, turn):
        return (turn + 1) % len(self.player_names)

    def get_winners(self):
        max_score = self.get_max_score()
        winners = [name for name in self.player_scores.keys() if self.player_scores[name] == max_score]

        return winners

    def get_max_score(self):
        return max([score for score in self.player_scores.values()])

    def init_player_scores_map(self):
        self.player_scores = {}
        for name in self.player_names:
            self.player_scores[name] = 0
