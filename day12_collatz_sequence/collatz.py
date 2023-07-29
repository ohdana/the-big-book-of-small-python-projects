MIN_START_NUMBER = 1
MAX_START_NUMBER = 9999

def main():
    init()
    show_intro_message()
    try_again = True

    while try_again:
        start_number = prompt_start_number()
        sequence = generate_collatz_sequence(start_number)
        show_numbers(sequence)
        try_again = prompt_try_again()

    say_bye()

def generate_collatz_sequence(start_number):
    sequence = [start_number]
    next_number = start_number

    while next_number != 1:
        next_number = get_next_collatz_number(next_number)
        sequence.append(next_number)

    return sequence

def get_next_collatz_number(number):
    if number % 2 == 0:
        return number // 2

    return 3 * number + 1

def show_numbers(numbers):
    print(', '.join([str(number) for number in numbers]))

def prompt_start_number():
    number = input(STRINGS_DICTIONARY.enter_start_number)

    while not is_valid_start_number(number):
        number = input(STRINGS_DICTIONARY.invalid_start_number)

    return int(number)

def prompt_try_again():
    try_again = input(STRINGS_DICTIONARY.try_again)

    while not is_valid_y_n(try_again):
        try_again = input(STRINGS_DICTIONARY.try_again)

    if try_again == 'n':
        return False

    return True

def is_valid_start_number(n):
    if not n:
        return False

    if not n.isdigit():
        return False

    return MIN_START_NUMBER <= int(n) <= MAX_START_NUMBER

def is_valid_y_n(text):
    if not text:
        return False

    return text in ['y', 'n']

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Collatz Sequence, or, the 3n + 1 Problem

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The Collatz Sequence is a sequence of numbers produced from a starting
    number n, following three rules:

    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.

    It is generally thought, but so far not mathematically  proven, that
    every starting number eventually terminates at 1.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.try_again = '''
    Try again? y/n: '''
    STRINGS_DICTIONARY.enter_start_number = '''
    Enter a starting number ({}-{}): '''.format(MIN_START_NUMBER, MAX_START_NUMBER)
    STRINGS_DICTIONARY.invalid_start_number = '''
    Please choose a number between {} and {}: '''.format(MIN_START_NUMBER, MAX_START_NUMBER)

class StringsDictionary:
    pass

main()
