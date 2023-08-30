from cup import Cup
from die import Die

N_OF_DICE = 3
MAX_SKULLS = 3
DIE_HEIGHT = 7
YES, NO = 'Y', 'N'
GOLD, SILVER, BRONZE = 'GOLD', 'SILVER', 'BRONZE'
STAR, SKULL, QUESTION = 'STAR', 'SKULL', 'QUESTION'
CUP_CONFIGURATION = { GOLD: 6, SILVER: 4, BRONZE: 3 }
GET_DIE_MAP = {}

class Turn:
    def __init__(self, player_name):
        self.player_name = player_name
        self.init_get_die_map()
        self.stars_collected = 0
        self.skulls_collected = 0
        self.turn_over = False

    def play(self):
        cup = self.init_cup()
        hand = self.make_initial_roll(cup)

        while not self.turn_over:
            roll_again = self.ask_whether_roll_again()
            if not roll_again:
                self.end_turn()
            else:
                hand = self.roll(cup, hand)

    def get_dice_to_keep(self, hand):
        dice_to_keep = []
        for die in hand:
            die_obj, roll_result = die
            if roll_result == QUESTION:
                dice_to_keep.append(die_obj)
        return dice_to_keep

    def roll(self, cup, hand):
        dice_to_keep = self.get_dice_to_keep(hand)
        n_of_new_dice = N_OF_DICE - len(dice_to_keep)

        if n_of_new_dice > cup.get_n_of_dice():
            print('There aren\'t enough dice left in the cup to continue {}\'s turn.'.format(self.player_name))
            self.end_turn()
            return

        new_dice = cup.pull(n_of_new_dice)
        roll_results = self.get_roll_results(dice_to_keep + new_dice)
        self.calculate_roll_results(roll_results)
        self.show_roll_results(roll_results)

        return roll_results

    def is_over(self):
        return self.turn_over

    def make_initial_roll(self, cup):
        return self.roll(cup, [])

    def get_roll_results(self, dice):
        return [(die, die.roll()) for die in dice]

    def calculate_roll_results(self, dice):
        self.calculate_stars_and_skulls(dice)
        if self.skulls_collected >= MAX_SKULLS:
            print('3 or more skulls means you\'ve lost your stars!')
            self.stars_collected = 0
            self.end_turn()

    def calculate_stars_and_skulls(self, dice):
        for die in dice:
            die_obj, roll_result = die
            if roll_result == STAR:
                self.stars_collected += 1
            elif roll_result == SKULL:
                self.skulls_collected += 1

    def end_turn(self):
        self.turn_over = True

    def get_stars_collected(self):
        return self.stars_collected

    def init_cup(self):
        return Cup(self.get_dice())

    def get_dice(self):
        dice = []
        for die_type in CUP_CONFIGURATION:
            n_of_dice = CUP_CONFIGURATION[die_type]
            for i in range(n_of_dice):
                die = GET_DIE_MAP[die_type]()
                dice.append(die)
        return dice

    def get_gold_die(self):
        die_sides = { STAR: 3, SKULL: 1, QUESTION: 2 }
        return Die(die_sides, GOLD)

    def get_silver_die(self):
        die_sides = { STAR: 2, SKULL: 2, QUESTION: 2 }
        return Die(die_sides, SILVER)

    def get_bronze_die(self):
        die_sides = { STAR: 1, SKULL: 3, QUESTION: 2 }
        return Die(die_sides, BRONZE)

    def init_get_die_map(self):
        GET_DIE_MAP[GOLD] = self.get_gold_die
        GET_DIE_MAP[SILVER] = self.get_silver_die
        GET_DIE_MAP[BRONZE] = self.get_bronze_die

    def ask_whether_roll_again(self):
        answer = input('Do you want to roll again? y/n: ')
        if not self.is_valid_y_n(answer):
            return self.ask_whether_roll_again()

        return answer.upper() == YES

    def is_valid_y_n(self, answer):
        return answer.upper() in [YES, NO]

    def show_roll_results(self, roll_results):
        self.show_dice(roll_results)
        print('Stars collected: {}   Skulls collected: {}'.format(self.stars_collected, self.skulls_collected))

    def show_dice(self, roll_results):
        lines = []
        dice_images = [die.get_image(die_face) for die, die_face in roll_results]
        for i in range(DIE_HEIGHT + 1):
            line = ' '.join([die_image[i] for die_image in dice_images])
            lines.append(line)
        image = '\n'.join(lines)
        print(image)
