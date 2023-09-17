import time
from sinengine import SinEngine

PAUSE_BETWEEN_TICKS = 0.1
CANVAS_WIDTH = 100
MAX_MESSAGE_LENGTH = 39
ENGINE = None

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    try:
        message = get_message()
        init_engine(message)
        while True:
            show_sine_line()
            tick()
            time.sleep(PAUSE_BETWEEN_TICKS)
    except KeyboardInterrupt:
        show_bye_message()

def show_sine_line():
    line = ENGINE.get_line()
    print(line)

def tick():
    ENGINE.tick()

def get_message():
    print(STRINGS_DICTIONARY.enter_message)
    user_input = input(STRINGS_DICTIONARY.input)
    while not 0 < len(user_input) <= MAX_MESSAGE_LENGTH:
        return get_message()

    return user_input

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init_engine(message):
    global ENGINE
    ENGINE = SinEngine(CANVAS_WIDTH, message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Sine Message

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Create a sine-wavy message. Press Ctrl-C to stop.'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.enter_message = '''
    What message do you want to display? (Max {} chars.)'''.format(MAX_MESSAGE_LENGTH)

class StringsDictionary:
    pass

main()
