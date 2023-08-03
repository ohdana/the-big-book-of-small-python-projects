MIN_DIAMOND_SIZE = 2
MAX_DIAMOND_SIZE = 6

def main():
    init()
    show_intro_message()
    draw_diamonds()

def draw_diamonds():
    for i in range(MIN_DIAMOND_SIZE, MAX_DIAMOND_SIZE + 1):
        draw_empty_diamond(i)
        draw_filled_diamond(i)

def draw_empty_diamond(size):
    print(get_diamond(size, is_empty=True))

def draw_filled_diamond(size):
    print(get_diamond(size, is_empty=False))

def get_diamond(size, is_empty):
    top_half = get_top_half_lines(size, is_empty)
    bottom_half = flip_half_vertically(top_half)

    return '\n'.join(top_half + bottom_half)

def get_top_half_lines(size, is_empty):
    return [get_top_line(i, size - i, is_empty) for i in range(size)]

def get_top_line(size, margin, is_empty=True):
    result = ' ' * margin + '/'
    if is_empty:
        result += ' ' * size * 2
    else:
        result += '/' * size
        result += '\\' * size
    result += '\\' + ' ' * margin

    return result

def flip_half_vertically(half_lines):
    return [flip_line_vertically(line) for line in reversed(half_lines)]

def flip_line_vertically(line):
    return line.replace('/', '*').replace('\\', '/').replace('*', '\\')

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Diamonds

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Draws diamonds of various sizes.'''

class StringsDictionary:
    pass

main()
