GOAT_DOOR = ['+------+', '|  ((  |', '|  oo  |', '| /_/|_|', '|    | |', '|GOAT|||', '+------+']
CAR_DOOR = ['+------+', '| CAR! |', '|    __|', '|  _/  |', '| /_ __|', '|   O  |', '+------+']
CLOSED_DOOR = ['+------+', '|      |', '|   {}  |', '|      |', '|      |', '|      |', '+------+']
DOOR_HEIGHT = 7

class CanvasPrinter:
    def __init__(self, n_of_doors):
        self.n_of_doors = n_of_doors

    def show_canvas(self, opened_doors):
        canvas = self.get_canvas(opened_doors)
        print('\n'.join(canvas))

    def get_canvas(self, opened_doors):
        canvas = []
        for i in range(DOOR_HEIGHT):
            line = self.get_canvas_line(opened_doors, i)
            canvas.append(line)
        return canvas

    def get_canvas_line(self, opened_doors, i):
        door_lines = []
        for j in range(self.n_of_doors):
            door_number = j + 1
            line_pattern = self.get_door_line_pattern(opened_doors, door_number, i)
            door_lines.append(line_pattern)
        return '  '.join(door_lines)

    def get_door_line_pattern(self, opened_doors, door_number, i):
        if door_number in opened_doors.keys():
            door = opened_doors[door_number]
            return self.get_opened_door_line(door, i)
        else:
            return self.get_closed_door_line(i, door_number)

    def get_opened_door_line(self, door, i):
        if door.is_goat():
            return GOAT_DOOR[i]
        elif door.is_car():
            return CAR_DOOR[i]

    def get_closed_door_line(self, line_number, door_number):
        line_pattern = CLOSED_DOOR[line_number]
        if '{}' in line_pattern:
            line_pattern = line_pattern.format(door_number)

        return line_pattern
