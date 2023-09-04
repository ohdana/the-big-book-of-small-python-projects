DEC, HEX, BIN = 'DEC', 'HEX', 'BIN'
PREFIX_LENGTH = 2

def main():
    init()
    show_intro_message()
    while True:
        play()

def play():
    starting_number = get_starting_number()
    n_of_numbers = get_n_of_numbers()
    show_numbers(starting_number, n_of_numbers)

def get_natural_number_from_user(message):
    user_input = input(message)
    while not is_valid_natural_number(user_input):
        return get_natural_number_from_user()

    return int(user_input)

def is_valid_natural_number(user_input):
    if not user_input.isdigit():
        return False

    return int(user_input) > 0

def get_n_of_numbers():
    return get_natural_number_from_user(STRINGS_DICTIONARY.enter_n_of_numbers)

def get_starting_number():
    return get_natural_number_from_user(STRINGS_DICTIONARY.enter_starting_number)

def show_numbers(starting_number, n_of_numbers):
    for i in range (starting_number, starting_number + n_of_numbers):
        show_line(i)

def show_line(number):
    dec_pattern = STRINGS_DICTIONARY.display_number_pattern.format(DEC, number)
    hex_pattern = STRINGS_DICTIONARY.display_number_pattern.format(HEX, get_hex(number))
    bin_pattern = STRINGS_DICTIONARY.display_number_pattern.format(BIN, get_bin(number))
    print(STRINGS_DICTIONARY.gap.join([dec_pattern, hex_pattern, bin_pattern]))

def get_bin(number):
    return bin(number)[PREFIX_LENGTH:]

def get_hex(number):
    return hex(number)[PREFIX_LENGTH:].upper()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Numeral System Counters

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Shows equivalent numbers in decimal, hexadecimal, and binary.'''
    STRINGS_DICTIONARY.enter_starting_number = '''
    Enter the starting number (interger bigger than 0): '''
    STRINGS_DICTIONARY.enter_n_of_numbers = '''
    Enter how many numbers to display (interger bigger than 0): '''
    STRINGS_DICTIONARY.gap = '        '
    STRINGS_DICTIONARY.display_number_pattern = '{}: {}'
class StringsDictionary:
    pass

main()
