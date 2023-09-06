from piglatinconverter import PigLatinConverter

CONVERTER = None

def main():
    init()
    show_intro_message()
    while True:
        play()

def play():
    user_input = get_user_input()
    converted_message = convert_message(user_input)
    show_message(converted_message)

def convert_message(message):
    return CONVERTER.convert(message)

def show_message(message):
    print(message)

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.enter_message)
    while not is_valid_user_input(user_input):
        return get_user_input()

    return user_input

def is_valid_user_input(user_input):
    if not user_input:
        return False

    return True

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init_converter():
    global CONVERTER
    CONVERTER = PigLatinConverter()

def init():
    init_strings_dictionary()
    init_converter()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Igpay Atinlay

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Translates English messages into Igpay Atinlay.'''
    STRINGS_DICTIONARY.enter_message = '''
    Enter your message: '''

class StringsDictionary:
    pass

main()
