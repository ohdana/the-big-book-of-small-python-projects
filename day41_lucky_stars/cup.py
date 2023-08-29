import random

class Cup:
    def __init__(self, dice):
        self.dice = dice

    def pull(self, n_of_dice):
        dice = []
        for i in range(n_of_dice):
            random.shuffle(self.dice)
            random_die = self.dice.pop()
            dice.append(random_die)
        return dice

    def get_n_of_dice(self):
        return len(self.dice)
