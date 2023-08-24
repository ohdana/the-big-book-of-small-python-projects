WIDTH = 30
HEIGHT = 20
GAP_CHAR = ' '
PLAYER_CHAR = '@'
ROBOT_CHAR = 'R'
DEAD_ROBOT_CHAR = 'X'
WALL_CHAR = chr(9617)  # Character 9617 is '░'

class Canvas:
    def __init__(self):
        self.canvas = self.generate_initial_canvas()
        self.allocate_walls()
        self.allocate_robots()
        self.allocate_player()

    def generate_initial_canvas(self):
        pass

    def allocate_walls(self):
        pass

    def allocate_robots(self):
        pass

    def allocate_player(self):
        pass
