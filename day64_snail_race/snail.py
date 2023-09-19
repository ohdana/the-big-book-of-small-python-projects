import random

MAX_SPEED = 2
MIN_SPEED = 0.2

class Snail:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_speed(self):
        return random.uniform(MIN_SPEED, MAX_SPEED)
