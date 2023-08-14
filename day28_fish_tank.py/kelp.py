import random, math
KELP_CHARS = [')', '(', '|']
KELP_TOP_CHAR = '|'
MAX_WIDTH = 3
MIN_WIDTH = 1

class Kelp:
    def __init__(self, canvas_height):
        min_length = math.floor(canvas_height * 0.3)
        max_length = math.floor(canvas_height * 0.8)
        self.length = random.randint(min_length, max_length)
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.body = []
        self.build_kelp()

    def build_kelp(self):
        for i in range(self.length - 1):
            x_pos = random.randint(0, self.width - 1)
            self.body.append((random.choice(KELP_CHARS), x_pos))

        x_pos = random.randint(0, self.width)
        self.body.append((KELP_TOP_CHAR, x_pos))

    def build_canvas(self):
        canvas = []
        for i in range(self.length):
            canvas.append([' '] * self.width)
        for y in range(self.length):
            for segment in self.body:
                char, x_pos = segment
                canvas[y][x_pos] = char

        return canvas

    def show_canvas(self):
        canvas = self.build_canvas()
        lines = [''.join(line) for line in canvas]
        print('\n'.join(lines))

kelp = Kelp(30)
kelp.show_canvas()
