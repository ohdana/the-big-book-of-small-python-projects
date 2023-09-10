BLACK = u'\u2588' # char █
DARK = u'\u2593' # char ▓
MEDIUM = u'\u2592' # char ▒
LIGHT = u'\u2591' # char ░
GAP = ' '
COLOURS = [ BLACK, DARK, MEDIUM, LIGHT ]
COLOUR_WIDTH = 2
RIGHT = 'RIGHT'
LEFT = 'LEFT'
DIRECTION_SHIFT = { LEFT: -1, RIGHT: 1 }

class Rainbow:
    def __init__(self, canvas_width):
        self.canvas_width = canvas_width
        self.pattern = self.get_pattern()
        self.width = self.get_width()
        self.x_position = 0
        self.direction = RIGHT

    def get_width(self):
        return len(self.pattern)

    def get_line(self):
        left_gap = GAP * self.x_position
        right_gap = GAP * (self.canvas_width - self.width - self.x_position)
        return left_gap + self.pattern + right_gap

    def tick(self):
        new_x_position = self.get_new_x_position()
        self.x_position = new_x_position

    def get_new_x_position(self):
        new_x_position = self.x_position + DIRECTION_SHIFT[self.direction]
        if self.is_out_of_bounds(new_x_position):
            self.change_direction()
            return self.get_new_x_position()

        return new_x_position

    def change_direction(self):
        if self.direction is RIGHT:
            self.direction = LEFT
        else:
            self.direction = RIGHT

    def is_out_of_bounds(self, x_position):
        if x_position < 0:
            return True

        if x_position >= (self.canvas_width - self.width):
            return True

        return False

    def get_pattern(self):
        return ''.join([colour * COLOUR_WIDTH for colour in COLOURS])
