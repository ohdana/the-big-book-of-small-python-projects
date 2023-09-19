import time
TICK_DURATION_SECONDS = 0.5
TICK_CHAR = '.'
GAP_CHAR = ' '
POLE_CHAR = '|'
NEW_LINE_CHAR = '\n'
SNAIL_IMG = '@v'
START, FINISH = 'START', 'FINISH'

class Race:
    def __init__(self, snails, distance):
        self.distance = distance
        self.init_snails(snails)

    def init_snails(self, snails):
        self.snails = {}
        self.snails_progress = {}
        for snail in snails:
            self.snails[snail.name] = snail
            self.snails_progress[snail.name] = 0.0

    def tick(self):
        for snail_name in self.snails.keys():
            self.tick_snail(snail_name)

    def tick_snail(self, snail_name):
        snail_progress_per_second = self.snails[snail_name].get_speed()
        self.snails_progress[snail_name] += snail_progress_per_second * TICK_DURATION_SECONDS

    def run(self):
        self.show()
        while not self.get_winners():
            time.sleep(TICK_DURATION_SECONDS)
            self.tick()
            self.show()

    def get_winners(self):
        return [snail_name for snail_name in self.snails.keys() if self.finished(snail_name)]

    def finished(self, snail_name):
        return self.snails_progress[snail_name] >= self.distance

    def clear_terminal(self):
        print(NEW_LINE_CHAR * 40)

    def show(self):
        self.clear_terminal()
        header = self.get_header()
        snails = self.get_snails_img()
        canvas = NEW_LINE_CHAR.join([header] + snails)
        print(canvas)

    def get_header(self):
        line_1 = START + GAP_CHAR * (self.distance - len(START)) + FINISH
        line_2 = POLE_CHAR + GAP_CHAR * self.distance + POLE_CHAR
        return line_1 + NEW_LINE_CHAR + line_2

    def get_snails_img(self):
        return [self.get_snail_img(snail_name) for snail_name in self.snails.keys()]

    def get_snail_img(self, snail_name):
        snail_progress = int(self.snails_progress[snail_name])
        line_1 = GAP_CHAR * snail_progress + snail_name
        line_2 = TICK_CHAR * snail_progress + SNAIL_IMG

        return line_1 + NEW_LINE_CHAR + line_2
