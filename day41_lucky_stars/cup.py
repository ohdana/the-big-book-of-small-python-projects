import random

class Cup:
    def __init__(self, dice):
        self.dice = dice

    def pull(self, n_of_dice):
        dice = random.choices(self.dice, k=n_of_dice)
        return [die.roll() for die in dice]
