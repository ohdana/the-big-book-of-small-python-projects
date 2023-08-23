import random, time

CANVAS_WIDTH = 100
CANVAS_HEIGHT = 50
SLEEP_DURATION = 0.5

def main():
    init()
    show_intro_message()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Hourglass

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    An animation of an hourglass with falling sand.'''

class StringsDictionary:
    pass

main()
