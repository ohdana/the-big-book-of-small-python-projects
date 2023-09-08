import math

def main():
    init()
    show_intro_message()
    generate_prime_numbers()

def generate_prime_numbers():
    start_number = get_start_number()
    input(STRINGS_DICTIONARY.press_key_instructions)
    try:
        while True:
            next_prime_number = get_closest_prime_number(start_number)
            show_number(next_prime_number)
            start_number = next_prime_number + 1
    except KeyboardInterrupt:
        show_bye_message()

def get_start_number():
    user_input = input(STRINGS_DICTIONARY.enter_number)

    if not user_input.isdigit():
        return get_start_number()

    return int(user_input)

def get_closest_prime_number(number):
    while not is_prime(number):
        number += 1
    return number

def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def show_number(number):
    print(str(number) + ', ', end='', flush=True)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Prime Numbers

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Calculates prime numbers, which are numbers that are only evenly
    divisible by one and themselves. They are used in a variety of practical
    applications.'''
    STRINGS_DICTIONARY.enter_number = '''
    Enter a number to start searching for primes from: '''
    STRINGS_DICTIONARY.press_key_instructions = '''
    Press Ctrl-C at any time to quit. Press Enter to begin...'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''

class StringsDictionary:
    pass

main()
