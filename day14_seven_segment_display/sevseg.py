DIGITS_MAP = {}
DIGIT_LINES_MAP = {}
SEVSEG_HEIGHT = 0

def main():
    init()

def get_two_digit_number(number):
    number_str = str(number)
    if number_str in DIGITS_MAP:
        return DIGITS_MAP[number_str]

    result = ''
    for i in range(SEVSEG_HEIGHT):
        for digit in number_str:
            result += DIGIT_LINES_MAP[digit][i]
        result += '\n'

    return result

def get_digit(digit):
    if not is_valid_digit(digit):
        return ''

    return DIGITS_MAP[digit]

def is_valid_digit(digit):
    if not len(digit) == 1:
        return False

    if not digit.isdigit():
        return False

    return True

def populate_digit_lines_map():
    DIGIT_LINES_MAP['0'] = STRINGS_DICTIONARY.num0.split('\n')
    DIGIT_LINES_MAP['1'] = STRINGS_DICTIONARY.num1.split('\n')
    DIGIT_LINES_MAP['2'] = STRINGS_DICTIONARY.num2.split('\n')
    DIGIT_LINES_MAP['3'] = STRINGS_DICTIONARY.num3.split('\n')
    DIGIT_LINES_MAP['4'] = STRINGS_DICTIONARY.num4.split('\n')
    DIGIT_LINES_MAP['5'] = STRINGS_DICTIONARY.num5.split('\n')
    DIGIT_LINES_MAP['6'] = STRINGS_DICTIONARY.num6.split('\n')
    DIGIT_LINES_MAP['7'] = STRINGS_DICTIONARY.num7.split('\n')
    DIGIT_LINES_MAP['8'] = STRINGS_DICTIONARY.num8.split('\n')
    DIGIT_LINES_MAP['9'] = STRINGS_DICTIONARY.num9.split('\n')

def populate_digits_map():
    DIGITS_MAP['0'] = STRINGS_DICTIONARY.num0
    DIGITS_MAP['1'] = STRINGS_DICTIONARY.num1
    DIGITS_MAP['2'] = STRINGS_DICTIONARY.num2
    DIGITS_MAP['3'] = STRINGS_DICTIONARY.num3
    DIGITS_MAP['4'] = STRINGS_DICTIONARY.num4
    DIGITS_MAP['5'] = STRINGS_DICTIONARY.num5
    DIGITS_MAP['6'] = STRINGS_DICTIONARY.num6
    DIGITS_MAP['7'] = STRINGS_DICTIONARY.num7
    DIGITS_MAP['8'] = STRINGS_DICTIONARY.num8
    DIGITS_MAP['9'] = STRINGS_DICTIONARY.num9

    two_digit_numbers = generate_two_digit_numbers(0, 59)
    DIGITS_MAP.update(two_digit_numbers)

def generate_two_digit_numbers(start, end):
    result = {}
    for i in range(int(start), int(end) + 1):
        number_str = str(i)
        if 0 <= i <= 9:
            number_str = '0' + str(i)
        result[number_str] = get_two_digit_number(number_str)

    return result

def set_sevseg_height():
    global SEVSEG_HEIGHT
    num0_img_lines = STRINGS_DICTIONARY.num0.split('\n')
    SEVSEG_HEIGHT = len(num0_img_lines)

def init():
    init_strings_dictionary()
    set_sevseg_height()
    populate_digit_lines_map()
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
    It doesn't really do anything. Just to be used in other projects :)

     __A__
    |     |    Each digit in a seven-segment display:
    F     B     __       __   __          __    __  __    __   __
    |__G__|    |  |  |   __|  __|  |__|  |__   |__    |  |__| |__|
    |     |    |__|  |  |__   __|     |   __|  |__|   |  |__|  __|
    E     C
    |__D__|'''
    STRINGS_DICTIONARY.num0 = '''
    .__.
    |  |
    |__|'''
    STRINGS_DICTIONARY.num1 = '''
    .
    |
    |'''
    STRINGS_DICTIONARY.num2 = '''
    .__.
     __|
    |__.'''
    STRINGS_DICTIONARY.num3 = '''
    __.
    __|
    __|'''
    STRINGS_DICTIONARY.num4 = '''
    .  .
    |__|
       |'''
    STRINGS_DICTIONARY.num5 = '''
     __.
    |__.
    .__|'''
    STRINGS_DICTIONARY.num6 = '''
     __.
    |__.
    |__|'''
    STRINGS_DICTIONARY.num7 = '''
    __.
      |
      |'''
    STRINGS_DICTIONARY.num8 = '''
    .__.
    |__|
    |__|'''
    STRINGS_DICTIONARY.num9 = '''
    .__.
    |__|
    .__|'''

class StringsDictionary:
    pass

main()
