import random

YES, NO = 'Y', 'N'
LEETSPEAK_MAP = None

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    user_input = get_user_input()
    leetspeak_text = convert_to_leetspeak(user_input)
    show(leetspeak_text)

def show(text):
    print(text)

def convert_to_leetspeak(text):
    result = ''
    for char in text:
        result += get_leetspeak_char(char)

    return result

def get_leetspeak_char(char):
    if char in LEETSPEAK_MAP.keys():
        return random.choice(LEETSPEAK_MAP[char])

    return char

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.enter_message)
    if not user_input:
        return get_user_input()
    return user_input

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()
    init_leetspeak_map()

def init_leetspeak_map():
    global LEETSPEAK_MAP
    LEETSPEAK_MAP = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Leetspeak

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Translates English messages into l33t5p34]<.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.enter_message = '''
    Enter your leet message: '''

class StringsDictionary:
    pass

main()

