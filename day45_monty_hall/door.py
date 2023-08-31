GOAT, CAR = 'GOAT', 'CAR'

class Door:
    def __init__(self, number, content):
        self.number = number
        self.content = content

    def get_number(self):
        return self.number

    def is_goat(self):
        return self.content == GOAT

    def is_car(self):
        return self.content == CAR
