import shutil
from datetime import datetime

W, A, S, D, H, C, F, QUIT = 'W', 'A', 'S', 'D', 'H', 'C', 'F', 'QUIT'
VALID_INPUTS = [W, A, S, D, H, C, F, QUIT]
COMMANDS_MAP = {}
CURSOR = (0, 0)
CHAR_UNDER_CURSOR = None
COMMANDS_LOG = []
GAME_OVER = False
CANVAS_WIDTH, CANVAS_HEIGHT = 0, 0
CANVAS = []

UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'

DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'

UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'

UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'

UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'

DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'

UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'

CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'


def main():
    init()
    show_intro_message()
    draw()

def draw():
    while not GAME_OVER:
        command = get_user_input()
        process_command(command)

def process_command(command):
    invoke_command(command)
    show_canvas()

def log_command(command):
    COMMANDS_LOG.append(command)

def show_canvas():
    drawing = get_drawing()
    print(drawing)

def get_drawing():
    lines = [''.join(line) for line in CANVAS]
    drawing = '\n'.join(lines)

    return drawing

def invoke_command(command):
    COMMANDS_MAP[command]()

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.directions).upper()

    while not is_valid_user_input(user_input):
        user_input = get_user_input()

    return user_input

def is_valid_user_input(user_input):
    if user_input not in VALID_INPUTS:
        return False

    return True

def update_cursor(x, y):
    global CURSOR, CHAR_UNDER_CURSOR
    old_x, old_y = CURSOR
    update_canvas(old_x, old_y, ' ')

    CURSOR = (x, y)
    CHAR_UNDER_CURSOR = CANVAS[y][x]
    update_canvas(x, y, STRINGS_DICTIONARY.cursor)

def update_canvas(x, y, char):
    CANVAS[y][x] = char

def is_free_cell(x, y):
    return CANVAS[y][x] == ' '

def move_up():
    x, y = CURSOR
    if y > 0:
        log_command(W)
        update_cursor(x, y - 1)

def move_down():
    x, y = CURSOR
    if y < CANVAS_HEIGHT:
        log_command(S)
        update_cursor(x, y + 1)

def move_right():
    x, y = CURSOR
    if x < CANVAS_WIDTH:
        log_command(D)
        update_cursor(x + 1, y)

def move_left():
    x, y = CURSOR
    if x > 0:
        log_command(A)
        update_cursor(x - 1, y)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def save():
    current_datetime = datetime.now()
    text_file = open('{}.txt'.format(datetime.now()), 'w')
    text_file.write(stringify_commands_log())
    text_file.write(get_drawing())
    text_file.close()

def show_help():
    print(STRINGS_DICTIONARY.help)

def clear():
    reset_commands_log()

def quit_game():
    global GAME_OVER
    GAME_OVER = True
    print(STRINGS_DICTIONARY.bye)

def reset_commands_log():
    global COMMANDS_LOG
    COMMANDS_LOG = []

def stringify_commands_log():
    return ''.join(COMMANDS_LOG)

def init():
    init_strings_dictionary()
    init_commands_map()
    init_canvas()

def init_commands_map():
    global COMMANDS_MAP
    COMMANDS_MAP[W] = move_up
    COMMANDS_MAP[S] = move_down
    COMMANDS_MAP[A] = move_left
    COMMANDS_MAP[D] = move_right
    COMMANDS_MAP[H] = show_help
    COMMANDS_MAP[F] = save
    COMMANDS_MAP[C] = clear
    COMMANDS_MAP[QUIT] = quit_game

def init_canvas():
    global CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS, CHAR_UNDER_CURSOR
    CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
    CANVAS_WIDTH -= 1
    CANVAS_HEIGHT -= 5
    CANVAS = []
    for i in range(CANVAS_HEIGHT):
        CANVAS.append([' '] * CANVAS_WIDTH)

    x, y = CURSOR
    CANVAS[y][x] = STRINGS_DICTIONARY.cursor
    CHAR_UNDER_CURSOR = ' '

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Etching Drawer

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    An art program that draws a continuous line around the screen using the
    WASD keys. Inspired by Etch the Sketch toy.'''

    STRINGS_DICTIONARY.directions = '''
    WASD keys to move, H for help, C to clear, F to Save, or QUIT.
    >'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.help = '''
    Enter W, A, S, and D characters to move the cursor and
    draw a line behind it as it moves. For example, ddd
    draws a line going right and sssdddwwwaaa draws a box.

    You can save your drawing to a text file by entering F.'''
    STRINGS_DICTIONARY.cursor = '#'

class StringsDictionary:
    pass

main()
