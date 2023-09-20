import random

FLIP_CASE_PROBABILITY_PERCENT = 90
USE_UPPER_CASE = True

def main():
    init()
    show_intro_message()
    play()

def play():
    while True:
        user_input = get_user_input()
        spongified_user_input = spongify(user_input)
        show_message(spongified_user_input)

def show_message(message):
    print(message)

def flip_case():
    global USE_UPPER_CASE
    USE_UPPER_CASE = not USE_UPPER_CASE

def get_user_input():
    print(STRINGS_DICTIONARY.enter_message)
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_user_input()

    return user_input

def spongify(string):
    return ''.join([spongify_char(char) for char in string])

def spongify_char(char):
    do_flip_case = random.randint(0, 100) <= FLIP_CASE_PROBABILITY_PERCENT
    if do_flip_case:
        flip_case()
    if USE_UPPER_CASE:
        return char.upper()

    return char

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    sPoNgEcAsE

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Translates English messages into sPOnGEcAsE.'''
    STRINGS_DICTIONARY.enter_message = '''
    eNtEr YoUr MeSsAgE:'''
    STRINGS_DICTIONARY.input = '''
    > '''


class StringsDictionary:
    pass

main()
