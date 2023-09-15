X_REPEAT = 10
Y_REPEAT = 10

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    for i in range(Y_REPEAT):
        print_horizontal_line()

def print_horizontal_line():
    for line in STRINGS_DICTIONARY.carpet_segment:
        print(line * X_REPEAT)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Shining Carpet

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Displays a tessellation of the carpet pattern from The Shining.'''
    STRINGS_DICTIONARY.carpet_segment = [
    '_ \ \ \_/ __',
    ' \ \ \___/ _',
    '\ \ \_____/ ',
    '/ / / ___ \_',
    '_/ / / _ \__',
    '__/ / / \___'
    ]

class StringsDictionary:
    pass

main()
