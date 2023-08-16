import random, time
from bubbler import Bubbler
from kelp import Kelp
from fish import Fish

FLOOR_CHAR = '^'
FLOOR_HEIGHT = 2
LEFT, RIGHT = 'left', 'right'

class Tank:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.floor = self.generate_floor()
        self.water = self.generate_water()
        self.bubblers = []
        self.kelps = []
        self.fishes = []

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

    def allocate_object_x(self, object_width):
        left_x = random.randint(0, self.width - object_width - 1)

        return left_x

    def allocate_fish(self, fish_width, fish_height):
        left_x = self.allocate_object_x(fish_width)
        top_y = random.randint(0, self.height - fish_height - 1)

        return left_x, top_y

    def allocate_kelp(self, kelp_width):
        return self.allocate_object_x(kelp_width)

    def allocate_bubbler(self, bubbler_width):
        return self.allocate_object_x(bubbler_width)

    def get_new_x_for_fish(self, fish, x):
        fish_width, fish_height = fish.get_dimensions()
        fish_direction = fish.get_direction()
        if x <= 0 and fish_direction == LEFT:
            fish.mirror()
            return x + 1
        elif x > self.width - fish_width - 1 and fish_direction == RIGHT:
            fish.mirror()
            return x - 1

        if fish.get_direction() == LEFT:
            return x - 1

        return x + 1

    def get_new_y_for_fish(self, fish, y):
        fish_width, fish_height = fish.get_dimensions()
        if y <= 0:
            return y + 1
        elif y >= self.height - fish_height - 1:
            return y - 1

        return y + random.randint(-1, 1)

    def add_fish(self, fish):
        if not fish:
            return

        x, y = self.allocate_fish(*fish.get_dimensions())
        self.fishes.append((fish, (x, y)))

    def add_kelp(self, kelp):
        if not kelp:
            return

        x = self.allocate_kelp(kelp.get_width())
        self.kelps.append((kelp, x))

    def add_bubbler(self, bubbler):
        if not bubbler:
            return

        x = self.allocate_bubbler(bubbler.get_width())
        self.bubblers.append((bubbler, x))

    def draw_kelps(self, canvas):
        for kelp, kelp_x_coord in self.kelps:
            self.draw_kelp(canvas, kelp_x_coord, kelp)
            kelp.tick()

        return canvas

    def draw_kelp(self, canvas, kelp_x_coord, kelp):
        root = random.randint(0, FLOOR_HEIGHT)
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

    def draw_fishes(self, canvas):
        for i in range(len(self.fishes)):
            fish, (x, y) = self.fishes[i]
            self.draw_fish(canvas, fish, x, y)
            self.fishes[i] = self.tick_fish(fish, x, y)

        return canvas

    def draw_fish(self, canvas, fish, x, y):
        fish_image = fish.get_image()
        for i in range(len(fish_image)):
            canvas[y][x + i] = fish_image[i]

        return canvas

    def tick_fish(self, fish, x, y):
        fish.tick()
        new_x = self.get_new_x_for_fish(fish, x)
        new_y = self.get_new_y_for_fish(fish, y)

        return fish, (new_x, new_y)

    def tick(self):
        self.reset()
        canvas = self.get()
        canvas = self.draw_kelps(canvas)
        canvas = self.draw_bubbles(canvas)
        canvas = self.draw_fishes(canvas)
        self.floor = canvas[-2:]
        self.water = canvas[:-2]

#height = 20
#tank = Tank(20, height)
#tank.add_bubbler(Bubbler(height))
#tank.add_bubbler(Bubbler(height))
#tank.add_kelp(Kelp(height))
#tank.add_kelp(Kelp(height))
#tank.add_kelp(Kelp(height))
#tank.add_fish(Fish())
#while True:
#    tank.tick()
#    tank.show()
#    time.sleep(0.1)

