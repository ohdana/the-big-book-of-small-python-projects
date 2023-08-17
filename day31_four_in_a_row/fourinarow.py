PLAYER_1, PLAYER_2 = 'PLAYER_1', 'PLAYER_2'
PLAYER_CHARS = { PLAYER_1: 'X', PLAYER_2: 'O' }

def main():
    init()
    show_intro_message()
    build_frame(7, 6)

def show_frame(frame):
    lines = [''.join(line) for line in frame]
    print('\n'.join(lines))

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Four in a Row

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A tile-dropping game to get four in a row, similar to Connect Four.'''

class StringsDictionary:
    pass

main()
