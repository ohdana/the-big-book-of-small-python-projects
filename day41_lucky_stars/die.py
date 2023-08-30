import random

STAR, SKULL, QUESTION = 'STAR', 'SKULL', 'QUESTION'
STAR_FACE = ['+-----------+',
            '|     .     |',
            '|    ,O,    |',
            '| \'ooOOOoo\' |',
            '|   `OOO`   |',
            '|   O\' \'O   |',
            '+-----------+']
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
SIDE_TYPE_MAP = { STAR: STAR_FACE, SKULL: SKULL_FACE, QUESTION: QUESTION_FACE }

class Die:
    def __init__(self, sides, die_type):
        self.sides = self.get_sides(sides)
        self.type = die_type

    def roll(self):
        return random.choice(self.sides)

    def get_type(self):
        return self.type

    def get_sides(self, sides):
        result = []
        for side_type in sides:
            n_of_sides = sides[side_type]
            for i in range(n_of_sides):
                result.append(side_type)

        return result

    def get_image(self, side_type):
        image_lines = SIDE_TYPE_MAP[side_type]
        image_lines.append('    {}    '.format(self.type))

        return image_lines
