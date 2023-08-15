import random, time

LEFT, RIGHT = 'left', 'right'
DIRECTIONS = [ LEFT, RIGHT ]
FISH_TYPES = [{ RIGHT: ['><>'], LEFT: ['<><']},
    { RIGHT: ['>||>'], LEFT: ['<||<']},
    { RIGHT: ['>))>'], LEFT: ['<((<']},
    { RIGHT: ['>||o'], LEFT: ['o||<']},
    { RIGHT: ['>-==>'], LEFT: ['<==-<']},
    { RIGHT: ['><)))*>'], LEFT: ['<*(((><']},
    { RIGHT: ['}-[[[*>'], LEFT: ['<*]]]-{']},
    { RIGHT: ['><XXX*>'], LEFT: ['<*XXX><']},
    { RIGHT: ['}-[[[*>'], LEFT: ['<*]]]-{']},
    { RIGHT: ['_.-._.-^=>', '.-._.-.^=>', '-._.-._^=>', '._.-._.^=>'],
        LEFT: ['<=^-._.-._', '<=^.-._.-.', '<=^_.-._.-', '<=^._.-._.']}]
FISH_HEIGHT = 1

class Fish:
    def __init__(self):
        self.direction = random.choice(DIRECTIONS)
        self.type = random.choice(FISH_TYPES)
        self.movement_phase_index = 0

    def get(self):
        return self.type, self.direction

    def get_direction(self):
        return self.direction

    def get_image(self):
        return self.type[self.direction][self.movement_phase_index]

    def get_dimensions(self):
        return len(self.get_image()), FISH_HEIGHT

    def tick(self):
        n_of_movement_phases = len(self.type[self.direction])
        if n_of_movement_phases > 1:
            self.movement_phase_index = (self.movement_phase_index + 1) % n_of_movement_phases

    def mirror(self):
        if self.direction == LEFT:
            self.direction = RIGHT
        else:
            self.direction = LEFT

    def show(self):
        print(self.get_image())
