import random

class Die:
    def __init__(self, sides, side_type_map, die_type):
        self.side_type_map = side_type_map
        self.sides = self.get_sides(sides)
        self.type = die_type

    def roll(self):
        return random.choice(self.sides), self.type

    def get_sides(self, sides):
        result = []
        for side_type in sides:
            n_of_sides = sides[side_type]
            for i in range(n_of_sides):
                result.append(side_type)

        return result

    def get_image(self, side_type):
        return self.side_type_map[side_type]
