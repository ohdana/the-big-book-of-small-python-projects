QUIT = 'QUIT'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
SHIFT = 13

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    while True:
        user_input = get_user_input()
        if user_input.upper() == QUIT:
            break
        rotated_message = rotate_message(user_input)
        show_message(rotated_message)

def get_user_input():
    print(STRINGS_DICTIONARY.enter_message)
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_user_input()

    return user_input

def rotate_message(message):
    return ''.join([rotate_char(char) for char in message])

def rotate_char(char):
    if char in UPPER_LETTERS:
        return UPPER_LETTERS[(UPPER_LETTERS.find(char) + SHIFT) % len(UPPER_LETTERS)]

    if char in LOWER_LETTERS:
        return LOWER_LETTERS[(LOWER_LETTERS.find(char) + SHIFT) % len(LOWER_LETTERS)]

    return char

def show_message(message):
    print(STRINGS_DICTIONARY.translated_message.format(message))

def init():
    init_strings_dictionary()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    ROT13 Cipher

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The simplest shift cipher for encrypting and decrypting text.'''
    STRINGS_DICTIONARY.enter_message = '''
    Enter a message to encrypt/decrypt (or QUIT):'''
    STRINGS_DICTIONARY.translated_message = '''
    The translated message is:
    {}'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''

class StringsDictionary:
    pass

main()
