import random, time

SLEEP_BETWEEN_LINES_SECONDS = 0.05
PAIRS = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]
CURR_LINE_INDEX = 0

def main():
    init()
    show_intro_message()
    generate_dna()

def generate_dna():
    while True:
        line = generate_line()
        show_line(line)
        update_line_counter()
        time.sleep(SLEEP_BETWEEN_LINES_SECONDS)

def generate_line():
    pair = generate_pair()
    pattern = STRINGS_DICTIONARY.dna_pattern[CURR_LINE_INDEX]
    if not '{}' in pattern:
        return pattern

    return pattern.format(*pair)

def update_line_counter():
    global CURR_LINE_INDEX
    pattern_length = len(STRINGS_DICTIONARY.dna_pattern)
    CURR_LINE_INDEX = (CURR_LINE_INDEX + 1) % pattern_length

def generate_pair():
    return random.choice(PAIRS)

def show_line(line):
    print(line)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    DNA Animation

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A simple animation of a DNA double-helix.'''

    STRINGS_DICTIONARY.dna_pattern = [
    '     ##',
    '    #{}-{}#',
    '   #{}---{}#',
    '  #{}-----{}#',
    ' #{}------{}#',
    '#{}------{}#',
    '#{}-----{}#',
    ' #{}---{}#',
    '  #{}-{}#',
    '   ##',
    '  #{}-{}#',
    '  #{}---{}#',
    ' #{}-----{}#',
    ' #{}------{}#',
    '  #{}------{}#',
    '   #{}-----{}#',
    '    #{}---{}#',
    '     #{}-{}#'
    ]

class StringsDictionary:
    pass

main()
