import math

GAP = ' '
OFFSET_STEP = 0.25

class SinEngine:
    def __init__(self, width, message):
        self.width = width
        self.sin_multiplier = (self.width - len(message)) / 2
        self.message = message
        self.offset = 0.0

    def tick(self):
        self.tick_offset()

    def tick_offset(self):
        self.offset += OFFSET_STEP

    def get_line(self):
        sin_shifted = math.sin(self.offset) + 1
        gap = int(sin_shifted * self.sin_multiplier) * GAP

        return gap + self.message
