import random, time

CANVAS_WIDTH = 100
SLEEP_BETWEEN_LINES_SECONDS = 0.1
MIN_STREAM_LENGTH = 5
MAX_STREAM_LENGTH = 15
STREAM_CHARS = ['0', '1']
STREAM_DENSITY_PERCENT = 2
STREAM_MAP = []

def main():
    init()
    show_intro_message()
    run_stream()

def run_stream():
    while True:
        line = generate_next_line()
        show_line(line)
        time.sleep(SLEEP_BETWEEN_LINES_SECONDS)

def show_line(line):
    print(line)

def generate_next_line():
    line = ''
    for i in range(CANVAS_WIDTH):
        if STREAM_MAP[i] > 0:
            line += get_char()
            STREAM_MAP[i] -= 1
        else:
            line += ' '
            STREAM_MAP[i] = get_new_stream_length()

    return line

def get_new_stream_length():
    start_new_stream = decide_if_start_new_stream()
    if not start_new_stream:
        return 0

    stream_length = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
    return stream_length

def decide_if_start_new_stream():
    return random.randint(1, 100) <= STREAM_DENSITY_PERCENT

def get_char():
    return random.choice(STREAM_CHARS)

def init_map():
    global STREAM_MAP
    STREAM_MAP = [0] * CANVAS_WIDTH

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
    init_map()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Digital Stream Screensaver

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A screensaver in the style of The Matrix movie's visuals.'''

class StringsDictionary:
    pass

main()
