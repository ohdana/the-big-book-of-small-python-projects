import time
from rainbow import Rainbow
PAUSE_BETWEEN_TICKS = 0.1
RAINBOW = None
CANVAS_WIDTH = 30

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    try:
        while True:
            show_rainbow_line()
    except KeyboardInterrupt:
        show_bye_message()

def show_rainbow_line():
    print(RAINBOW.get_line())
    RAINBOW.tick()
    time.sleep(PAUSE_BETWEEN_TICKS)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init_rainbow():
    global RAINBOW
    RAINBOW = Rainbow(CANVAS_WIDTH)

def init():
    init_strings_dictionary()
    init_rainbow()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Rainbow

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Shows a simple rainbow animation. Press Ctrl-C to stop.'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''

class StringsDictionary:
    pass

main()
