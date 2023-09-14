import random

HEADS, TAILS = 'HEADS', 'TAILS'

class Coin:
    def __init__(self):
        self.sides = [HEADS, TAILS]

    def flip(self):
        return random.choice(self.sides)
