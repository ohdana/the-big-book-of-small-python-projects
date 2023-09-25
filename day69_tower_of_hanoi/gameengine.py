TOWER_CHAR = '||'
DISC_CHAR = '@'

class GameEngine:
    def __init__(self, tower_ids, tower_src_id, tower_dest_id, n_of_discs):
        self.n_of_discs = n_of_discs
        self.tower_ids = tower_ids
        self.tower_src_id = tower_src_id
        self.tower_dest_id = tower_dest_id

    def start_new_game(self):
        self.init_towers()

    def is_game_over(self):
        return self.is_full_tower_dest()

    def is_full_tower_dest(self):
        return len(self.towers[self.tower_dest_id]) == self.n_of_discs

    def get_tower_height(self):
        return self.n_of_discs + 1

    def is_valid_move(self, tower_src, tower_dest):
        tower_src_top_disc = self.peek(tower_src)
        if not tower_src_top_disc:
            return False
        tower_dest_top_disc = self.peek(tower_dest)
        return self.is_bigger(tower_dest_top_disc, tower_src_top_disc)

    def move(self, tower_src, tower_dest):
        if self.is_valid_move(tower_src, tower_dest):
            tower_src_top_disc = self.pop(tower_src)
            self.push(tower_src_top_disc, tower_dest)

    def is_bigger(self, disc_1, disc_2):
        if not disc_1:
            return True

        return disc_1 > disc_2

    def peek(self, tower_id):
        if not self.towers[tower_id]:
            return None
        return self.towers[tower_id][0]

    def push(self, disc_id, tower_id):
        self.towers[tower_id].insert(0, disc_id)

    def pop(self, tower_id):
        return self.towers[tower_id].pop(0)

    def init_towers(self):
        self.towers = {}
        for tower_id in self.tower_ids:
            self.towers[tower_id] = []
            if tower_id == self.tower_src_id:
                self.init_discs(tower_id)

    def init_discs(self, tower_id):
        self.towers[tower_id] = [(i + 1) for i in range(self.n_of_discs)]

    def get_disc_image(self, disc_id):
        gap = (self.n_of_discs - disc_id) * ' '
        head = disc_id * DISC_CHAR
        middle = '_{}'.format(disc_id)
        pole_width = 2
        tail = (disc_id - len(middle) + pole_width) * DISC_CHAR
        return gap + head + middle + tail + gap

    def show(self):
        tower_images = self.get_tower_images()
        for i in range(self.get_tower_height() + 1):
            line = '  '.join([image[i] for image in tower_images])
            print(line)

    def get_tower_images(self):
        return [self.get_tower_image(tower_id) for tower_id in self.towers]

    def get_tower_image(self, tower_id):
        discs = self.towers[tower_id]
        tower = [self.get_disc_image(disc_id) for disc_id in discs]
        gap = self.n_of_discs * ' '
        while len(tower) < self.get_tower_height():
            tower.insert(0, gap + TOWER_CHAR + gap)

        tower.append(self.get_tower_label(tower_id))

        return tower

    def get_tower_label(self, tower_id):
        tower_name = str(tower_id)
        gap = self.n_of_discs * ' '
        middle = ' {}'.format(tower_name)

        return gap + middle + gap
