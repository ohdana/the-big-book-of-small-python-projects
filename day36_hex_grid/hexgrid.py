X_REPEAT = 10
Y_REPEAT = 10
GAP_CHAR = ' '
HORIZONTAL_CHAR = '_'
SLASH_CHAR = '/'
BACK_SLASH_CHAR = '\\'

def main():
    init()
    show_intro_message()
    show_grid(2)

def show_grid(scale=1):
    for y in range(Y_REPEAT):
        show_grid_line(scale)

def show_grid_line(scale):
    lines = get_hex_cell(scale)
    for line in lines:
        print(line * X_REPEAT)

def get_hex_cell(scale):
    top = []
    bottom = []
    horizontal_line = HORIZONTAL_CHAR * scale
    for i in range(scale):
        top_line = (scale - 1 - i) * GAP_CHAR + SLASH_CHAR + (scale + i * 2) * GAP_CHAR + BACK_SLASH_CHAR + (scale - 1 - i) * GAP_CHAR + scale * GAP_CHAR
        bottom_line = i * GAP_CHAR + BACK_SLASH_CHAR + (scale + (scale - i - 1) * 2) * GAP_CHAR + SLASH_CHAR + (scale + i) * GAP_CHAR
        if i == (scale - 1):
            top_line = SLASH_CHAR + GAP_CHAR * (scale + i * 2) + BACK_SLASH_CHAR + HORIZONTAL_CHAR * scale
            bottom_line = i * GAP_CHAR + BACK_SLASH_CHAR + horizontal_line + SLASH_CHAR + i * GAP_CHAR + scale * GAP_CHAR
        top.append(top_line)
        bottom.append(bottom_line)

    return top + bottom

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Hex Grid

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Displays a simple tessellation of a hexagon grid.'''

class StringsDictionary:
    pass

main()

