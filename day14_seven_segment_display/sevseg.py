DIGITS_MAP = {}

def main():
    init()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def get_digit(digit):
    if not is_valid_digit(digit):
        return ''

    return DIGITS_MAP[int(digit)]

def is_valid_digit(digit):
    if not len(digit) == 1:
        return False

    if not digit.isdigit():
        return False

    return True

def populate_digits_map():
    DIGITS_MAP[0] = STRINGS_DICTIONARY.num0
    DIGITS_MAP[1] = STRINGS_DICTIONARY.num1
    DIGITS_MAP[2] = STRINGS_DICTIONARY.num2
    DIGITS_MAP[3] = STRINGS_DICTIONARY.num3
    DIGITS_MAP[4] = STRINGS_DICTIONARY.num4
    DIGITS_MAP[5] = STRINGS_DICTIONARY.num5
    DIGITS_MAP[6] = STRINGS_DICTIONARY.num6
    DIGITS_MAP[7] = STRINGS_DICTIONARY.num7
    DIGITS_MAP[8] = STRINGS_DICTIONARY.num8
    DIGITS_MAP[9] = STRINGS_DICTIONARY.num9

def init():
    init_strings_dictionary()
    populate_digits_map()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Sevseg

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A seven segment number display module.

     __A__
    |     |    Each digit in a seven-segment display:
    F     B     __       __   __          __    __  __    __   __
    |__G__|    |  |  |   __|  __|  |__|  |__   |__    |  |__| |__|
    |     |    |__|  |  |__   __|     |   __|  |__|   |  |__|  __|
    E     C
    |__D__|'''
    STRINGS_DICTIONARY.num0 = '''
     __
    |  |
    |__|
    '''
    STRINGS_DICTIONARY.num1 = '''
    |
    |
    '''
    STRINGS_DICTIONARY.num2 = '''
     __
     __|
    |__
    '''
    STRINGS_DICTIONARY.num3 = '''
    __
    __|
    __|
    '''
    STRINGS_DICTIONARY.num4 = '''
    |__|
       |
    '''
    STRINGS_DICTIONARY.num5 = '''
     __
    |__
     __|
    '''
    STRINGS_DICTIONARY.num6 = '''
     __
    |__
    |__|
    '''
    STRINGS_DICTIONARY.num7 = '''
    __
      |
      |
    '''
    STRINGS_DICTIONARY.num8 = '''
     __
    |__|
    |__|
    '''
    STRINGS_DICTIONARY.num9 = '''
     __
    |__|
     __|
    '''

class StringsDictionary:
    pass

main()
