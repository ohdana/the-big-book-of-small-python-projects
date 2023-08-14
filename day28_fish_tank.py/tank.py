import random, time
from bubbler import Bubbler
from kelp import Kelp

FLOOR_CHAR = '^'
FLOOR_HEIGHT = 2

class Tank:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.floor = self.generate_floor()
        self.water = self.generate_water()
        self.bubblers = []
        self.kelps = []

    def generate_floor(self):
        floor = []
        for i in range(FLOOR_HEIGHT):
            floor.append([FLOOR_CHAR] * self.width)

        return floor

    def generate_water(self):
        water = []
        for i in range(self.height - FLOOR_HEIGHT):
            water.append([' '] * self.width)

        return water

    def show(self):
        water_lines = [''.join(line) for line in self.water]
        print('\n'.join(water_lines))
        floor_lines = [''.join(line) for line in self.floor]
        print('\n'.join(floor_lines))

    def get(self):
        return self.water + self.floor

    def reset(self):
        self.water = self.generate_water()
        self.floor = self.generate_floor()

    def get_dimensions(self):
        return self.width, self.height

    def add_kelp(self, kelp):
        if not kelp:
            return

        x = self.allocate_kelp(kelp.get_width())
        self.kelps.append((kelp, x))

    def allocate_kelp(self, kelp_width):
        left_bottom_x = random.randint(0, self.width - kelp_width - 1)

        return left_bottom_x

    def add_bubbler(self, bubbler):
        if not bubbler:
            return

        x = self.allocate_bubbler(bubbler.get_width())
        self.bubblers.append((bubbler, x))

    def allocate_bubbler(self, bubbler_width):
        left_bottom_x = random.randint(0, self.width - bubbler_width - 1)

        return left_bottom_x

    def draw_kelps(self, canvas):
        for kelp, kelp_x_coord in self.kelps:
            self.draw_kelp(canvas, kelp_x_coord, kelp)
            kelp.tick()

        return canvas

    def draw_kelp(self, canvas, kelp_x_coord, kelp):
        kelp_body = kelp.get_body()
        for i in range(len(kelp_body) - 1):
            kelp_char, kelp_char_x_coord = kelp_body[i]
            x = kelp_x_coord + kelp_char_x_coord
            y = self.height - 1 - i
            canvas[y][x] = kelp_char

        return canvas

    def draw_bubbles(self, canvas):
        for bubbler, bubbler_x_coord in self.bubblers:
            bubbles = bubbler.get_bubbles()
            for bubble in bubbles:
                self.draw_bubble(canvas, bubbler_x_coord, bubble)
            bubbler.tick()
        return canvas

    def draw_bubble(self, canvas, bubbler_x_coord, bubble):
        bubble_char, location = bubble
        bubble_x, bubble_y = location
        canvas[bubble_y][bubble_x + bubbler_x_coord] = bubble_char

    def tick(self):
        self.reset()
        canvas = self.get()
        canvas = self.draw_kelps(canvas)
        canvas = self.draw_bubbles(canvas)
        self.floor = canvas[-2:]
        self.water = canvas[:-2]

#height = 30
#tank = Tank(100, height)
#tank.add_bubbler(Bubbler(height))
#tank.add_bubbler(Bubbler(height))
#tank.add_kelp(Kelp(height))
#tank.add_kelp(Kelp(height))
#tank.add_kelp(Kelp(height))
#while True:
#    tank.tick()
#    tank.show()
#    time.sleep(0.5)

