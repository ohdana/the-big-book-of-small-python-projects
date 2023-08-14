import random, time

BUBBLE_TYPES = ['0', 'o', 'O', '.']
MIN_WIDTH, MAX_WIDTH = 3, 7
DENSITY_PERCENT = 75
DEFAULT_TICK_DURATION = 0.1
ON = False

class Bubbler:
    def __init__(self, screen_height, tick_duration=DEFAULT_TICK_DURATION):
        self.canvas_height = screen_height
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.tick_duration = tick_duration
        self.bubbles = []

    def tick(self):
        new_bubble_needed = self.decide_if_new_bubble_needed()
        if new_bubble_needed:
            bubble = self.generate_new_bubble()
            self.bubbles.append(bubble)

        self.tick_bubbles()

    def tick_bubbles(self):
        for i in range(len(self.bubbles)):
            bubble_char, location = self.bubbles[i]
            x, y = location
            self.bubbles[i] = bubble_char, (x, y - 1)

        self.bubbles = [bubble for bubble in self.bubbles if not self.out_of_scope(bubble)]

    def get_bubbles(self):
        return self.bubbles

    def out_of_scope(self, bubble):
        bubble_char, location = bubble
        x, y = location
        return y < 0

    def get_width(self):
        return self.width

    def generate_new_bubble(self):
        bubble_char = random.choice(BUBBLE_TYPES)
        x, y = random.randint(0, self.width - 1), self.canvas_height - 1
        location = (x, y)

        return bubble_char, location

    def decide_if_new_bubble_needed(self):
        return random.randint(1, 100) <= DENSITY_PERCENT

    #def show_canvas(self):
    #    canvas = self.build_canvas()
    #    lines = [''.join(line) for line in canvas]
    #    print('\n'.join(lines))

    #def build_canvas(self):
    #    canvas = []
    #    for i in range(self.canvas_height):
    #        canvas.append([' '] * self.width)

    #    for bubble_char, location in self.bubbles:
    #        x, y = location
    #        canvas[y][x] = bubble_char

    #    return canvas

    #def is_on(self):
    #    return ON

    #def switch_on(self):
    #    global ON
    #    ON = True
    #    while self.is_on():
    #        self.tick()
    #        self.show_canvas()
    #        time.sleep(self.tick_duration)

#bubbler = Bubbler(30)
#bubbler.switch_on()
#bubbler.show_canvas()
