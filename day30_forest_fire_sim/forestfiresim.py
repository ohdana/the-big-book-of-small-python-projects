import random, time

TREE, FIRE, EMPTY = 'A', 'W', ' '
FIRE_PROBABILITY_PERCENT = 20
NEW_TREE_PROBABILITY_PERCENT = 10
MIN_PERCENT, MAX_PERCENT = 1, 100
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 30

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    canvas = get_clean_canvas()
    while True:
        canvas = tick(canvas)
        show_canvas(canvas)
        time.sleep(1)

def get_clean_canvas():
    canvas = []
    for i in range(CANVAS_HEIGHT):
        canvas.append([EMPTY] * CANVAS_WIDTH)
    return canvas

def tick(current_canvas):
    canvas = []
    for i in range(CANVAS_HEIGHT):
        new_line = []
        for j in range(CANVAS_WIDTH):
            new_line.append(get_new_char(current_canvas, j, i))
        canvas.append(new_line)
    return canvas

def get_new_char(canvas, x, y):
    current_char = canvas[y][x]
    if current_char == FIRE:
        return EMPTY
    elif current_char == EMPTY:
        if decide_if_grow_new_tree():
            return TREE
    elif current_char == TREE:
        if decide_if_lightning_strikes():
            return FIRE
        if any_neighbour_in_fire(canvas, x, y):
            return FIRE

    return current_char

def get_neighbours(canvas, x, y):
    left = get_neighbour(canvas,x - 1, y)
    right = get_neighbour(canvas,x + 1, y)
    top = get_neighbour(canvas,x, y - 1)
    bottom = get_neighbour(canvas, x, y + 1)

    return left, top, right, bottom

def get_neighbour(canvas, x, y):
    out_of_range = lambda x, min_value, max_value: x < min_value or x > max_value
    if out_of_range(x, 0, CANVAS_WIDTH - 1):
        return None
    if out_of_range(y, 0, CANVAS_HEIGHT - 1):
        return None

    return canvas[y][x]

def any_neighbour_in_fire(canvas, x, y):
    neighbours = get_neighbours(canvas, x, y)
    return any([neighbour for neighbour in neighbours if neighbour == FIRE])

def show_canvas(canvas):
    lines = [''.join(line) for line in canvas]
    print('\n'.join(lines))

def decide_if_grow_new_tree():
    return random.randint(MIN_PERCENT, MAX_PERCENT) <= NEW_TREE_PROBABILITY_PERCENT

def decide_if_lightning_strikes():
    return random.randint(MIN_PERCENT, MAX_PERCENT) <= FIRE_PROBABILITY_PERCENT

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Forest Fire Sim

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A simulation of wildfires spreading in a forest.'''

class StringsDictionary:
    pass

main()
