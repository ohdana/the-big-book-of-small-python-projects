import math
GAME_OVER = False

def main():
    init()
    show_intro_message()
    find_factors()

def find_factors():
    user_input = get_user_input()
    while not GAME_OVER:
        factors = get_factors(user_input)
        show_factors(factors)
        user_input = get_user_input()

    say_bye()

def get_factors(number):
    result = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            result.append(i)
            result.append(number // i)

    return sorted(result)

def show_factors(factors):
    print(', '.join([str(factor) for factor in factors]))

def get_user_input():
    global GAME_OVER
    user_input = input(STRINGS_DICTIONARY.enter_number)

    if user_input.upper() == 'QUIT':
        GAME_OVER = True
        return

    if not is_valid_user_input(user_input):
        return get_user_input()

    return int(user_input)

def is_valid_user_input(user_input):
    if not user_input:
        return False

    if not user_input.isdigit():
        return False

    if int(user_input) < 0:
        return False

    return True

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
    Factor Finder

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Finds all the factors of a number.
    A number's factors are two numbers that, when multiplied with each
    other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
    factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
    say that 26 has four factors: 1, 2, 13 and 26.

    If a number only has two factors (1 and itself), we call that a prime
    number. Otherwise, we call it a composite number.

    Can you discover some prime numbers?'''
    STRINGS_DICTIONARY.enter_number = '''
    Enter a positive whole number to factor (or QUIT): '''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''

class StringsDictionary:
    pass

main()

