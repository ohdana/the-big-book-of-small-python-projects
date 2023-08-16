import random, time

TREE, FIRE, EMPTY = 'A', 'W', ' '
FIRE_PROBABILITY = 0.5
NEW_TREE_PROBABILITY = 0.15
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 30

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    canvas = init_forest()
    while True:
        show_canvas(canvas)
        canvas = tick(canvas)
        time.sleep(1)

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
        neighbours = get_neighbours(canvas, x, y)
        if any_neighbour_in_fire(neighbours):
            return FIRE

    return current_char

def decide_if_lightning_strikes():
    return random.randint(1, 100) < FIRE_PROBABILITY * 100

def get_neighbours(canvas, x, y):
    left = get_neighbour(canvas,x - 1, y)
    right = get_neighbour(canvas,x + 1, y)
    top = get_neighbour(canvas,x, y - 1)
    bottom = get_neighbour(canvas, x, y + 1)

    return left, top, right, bottom

def get_neighbour(canvas, x, y):
    if x < 0 or y < 0:
        return None

    if x >= CANVAS_WIDTH or y >= CANVAS_HEIGHT:
        return None

    return canvas[y][x]

def any_neighbour_in_fire(neighbours):
    return any([neighbour for neighbour in neighbours if neighbour == FIRE])

def init_forest():
    canvas = []
    for i in range(CANVAS_HEIGHT):
        new_line = []
        for j in range(CANVAS_WIDTH):
            new_line.append(generate_forest_char())
        canvas.append(new_line)

    return canvas

def generate_forest_char():
    if decide_if_grow_new_tree():
        return TREE
    return EMPTY

def show_canvas(canvas):
        lines = [''.join(line) for line in canvas]
        print('\n'.join(lines))

def decide_if_grow_new_tree():
    return random.randint(1, 100) < NEW_TREE_PROBABILITY * 100

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
