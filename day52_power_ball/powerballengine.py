import random

MIN_REGULAR_NUMBER = 1
MAX_REGULAR_NUMBER = 69
MIN_POWERBALL_NUMBER = 1
MAX_POWERBALL_NUMBER = 26
N_OF_REGULAR_NUMBERS = 5

class PowerBallEngine():
    def __init__(self):
        pass

    def generate_numbers(self):
        regular_numbers = self.generate_regular_numbers()
        powerball_number = self.generate_power_ball_number()

        return regular_numbers, powerball_number

    def generate_regular_numbers(self):
        numbers = [self.generate_regular_number() for i in range(N_OF_REGULAR_NUMBERS)]
        return sorted(numbers)

    def generate_regular_number(self):
        return random.randint(MIN_REGULAR_NUMBER, MAX_REGULAR_NUMBER)

    def generate_power_ball_number(self):
        return random.randint(MIN_POWERBALL_NUMBER, MAX_POWERBALL_NUMBER)
