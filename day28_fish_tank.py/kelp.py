import random, math, time
KELP_CHARS = [')', '(']
MAX_WIDTH = 3
MIN_WIDTH = 2
MIN_SEGMENT_LENGTH = 2
MAX_SEGMENT_LENGTH = 4

class Kelp:
    def __init__(self, canvas_height):
        min_length = math.floor(canvas_height * 0.3)
        max_length = math.floor(canvas_height * 0.8)
        self.canvas_height = canvas_height
        self.length = random.randint(min_length, max_length)
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.body = []
        self.build_kelp()

    def build_kelp(self):
        for i in range(self.length):
            if len(self.body) > i:
                continue
            segment_length = random.randint(MIN_SEGMENT_LENGTH, MAX_SEGMENT_LENGTH)
            x_pos = random.randint(0, self.width - 1)
            char = random.choice(KELP_CHARS)
            self.body += [(char, x_pos)] * segment_length

    def get_width(self):
        return self.width

    def get_body(self):
        return self.body

    def tick(self):
        new_body = []
        for segment in self.body:
            new_segment = self.mirror_segment(segment)
            new_body.append(new_segment)

        self.body = new_body

    def mirror_segment(self, segment):
        char, x_pos = segment
        new_char = self.mirror_char(char)
        new_x_pos = self.width - x_pos - 1

        return (new_char, new_x_pos)

    def mirror_char(self, char):
        if char == ')':
            return '('
        elif char == '(':
            return ')'

        return char

    #def build_canvas(self):
    #    canvas = []
    #    for i in range(self.length):
    #        canvas.append([' '] * self.width)

    #    for i in range(self.length):
    #        char, x_pos = self.body[i]
    #        y_pos = self.length - i - 1
    #        canvas[y_pos][x_pos] = char

    #    return canvas

    #def show_canvas(self):
    #    canvas = self.build_canvas()
    #    lines = [''.join(line) for line in canvas]
    #    print('\n'.join(lines))

#kelp = Kelp(30)
#while True:
#    kelp.tick()
#    kelp.show_canvas()
#    time.sleep(1)
