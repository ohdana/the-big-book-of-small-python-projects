CURSOR_CHAR = '>'
FRAME_TOP_LEFT_CHAR = chr(9484)  # Character 9484 is '┌'
FRAME_BOTTOM_LEFT_CHAR = chr(9492)  # Character 9492 is '└'
FRAME_TOP_RIGHT_CHAR = chr(9488)  # Character 9488 is '┐'
FRAME_BOTTOM_RIGHT_CHAR = chr(9496)  # Character 9496 is '┘'
FRAME_HORIZONTAL_CHAR = chr(9472)  # Character 9472 is '─'
FRAME_VARTICAL_CHAR = chr(9474)  # Character 9474 is '│'

class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = self.get_canvas()

    def get_canvas(self):
        frame = self.build_frame()
        canvas = self.add_cursor(frame)

        return canvas

    def build_frame(self):
        canvas = []
        canvas.append([FRAME_HORIZONTAL_CHAR] * (self.width + 2))
        for i in range(self.height):
            new_line = [FRAME_VARTICAL_CHAR] + [' '] * self.width + [FRAME_VARTICAL_CHAR]
            canvas.append(new_line)
        canvas.append([FRAME_HORIZONTAL_CHAR] * (self.width + 2))

        top_left_x, top_left_y = 0, 0
        bottom_right_x, bottom_right_y = self.width + 1, self.height + 1
        top_right_x, top_right_y = self.width + 1, 0
        bottom_left_x, bottom_left_y = 0, self.height + 1

        canvas[top_left_y][top_left_x] = FRAME_TOP_LEFT_CHAR
        canvas[bottom_left_y][bottom_left_x] = FRAME_BOTTOM_LEFT_CHAR
        canvas[top_right_y][top_right_x] = FRAME_TOP_RIGHT_CHAR
        canvas[bottom_right_y][bottom_right_x] = FRAME_BOTTOM_RIGHT_CHAR

        return canvas

    def add_cursor(self, canvas):
        cursor_x, cursor_y = 0, 1
        canvas[cursor_y][cursor_x] = CURSOR_CHAR

        return canvas

    def show_canvas(self):
        lines = [''.join(line) for line in self.canvas]
        print('\n'.join(lines))

frame = Frame(10, 10)
frame.show_canvas()
