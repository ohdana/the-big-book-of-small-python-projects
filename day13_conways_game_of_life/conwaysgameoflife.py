import random, time
WINDOW_WIDTH = 79
WINDOW_HEIGHT = 20
CELL_ALIVE = 'o'
CELL_DEAD = ' '

def main():
    init()
    show_intro_message()
    window = generate_new_window()

    while True:
        show_window(window)
        time.sleep(1)
        window = create_next_generation(window)

    say_bye()

def create_next_generation(old_generation):
    new_generation = []

    for line_number in range(WINDOW_HEIGHT):
        new_line = []
        for column_number in range(WINDOW_WIDTH):
            cell = old_generation[line_number][column_number]
            neighbours = get_cell_neighbours(old_generation, line_number, column_number)
            new_gen_cell = get_new_gen_cell(cell, neighbours)
            new_line.append(new_gen_cell)
        new_generation.append(new_line)

    return new_generation

def get_cell_neighbours(window, line_number, column_number):
    left = get_cell_by_coords(window, line_number, column_number-1)
    right = get_cell_by_coords(window, line_number, column_number+1)
    top = get_cell_by_coords(window, line_number-1, column_number)
    bottom = get_cell_by_coords(window, line_number+1, column_number)

    return [top, right, bottom, left]

def get_cell_by_coords(window, line_number, column_number):
    if 0 <= line_number < WINDOW_HEIGHT:
        if 0 <= column_number < WINDOW_WIDTH:
            return window[line_number][column_number]

    return None

def get_new_gen_cell(cell, neighbours):
    alive_neighbours = [x for x in neighbours if x == CELL_ALIVE]
    alive_neighbours_count = len(alive_neighbours)
    if cell == CELL_ALIVE:
        if alive_neighbours_count in [2, 3]:
            return CELL_ALIVE
        else:
            return CELL_DEAD
    else:
        if alive_neighbours_count == 3:
            return CELL_ALIVE
        else:
            return CELL_DEAD

def show_window(window):
    for i in range(WINDOW_HEIGHT):
        show_window_line(window[i])
    print('\n'*5)

def show_window_line(line):
    print(''.join(line))

def generate_new_window():
    window = []
    for i in range(WINDOW_HEIGHT):
        new_line = generate_new_line(WINDOW_WIDTH)
        window.append(new_line)

    return window

def generate_new_line(line_length):
    line = ''
    for i in range(line_length):
        line += generate_new_cell()

    return line

def generate_new_cell():
    is_alive_cell = random.randint(1,2) % 2 == 0
    if is_alive_cell:
        return CELL_ALIVE

    return CELL_DEAD

def prompt_try_again():
    try_again = input(STRINGS_DICTIONARY.try_again)

    while not is_valid_y_n(try_again):
        try_again = input(STRINGS_DICTIONARY.try_again)

    if try_again == 'n':
        return False

    return True

def is_valid_y_n(text):
    if not text:
        return False

    return text in ['y', 'n']

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Conway's Game Of Life

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The classic cellular automata simulation. Press Ctrl+C to stop.'''

    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.try_again = '''
    Try again? y/n: '''

class StringsDictionary:
    pass

main()

