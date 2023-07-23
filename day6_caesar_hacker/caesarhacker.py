MIN_KEY = 0
MAX_KEY = 25
ABC='abcdefghijklmnopqrstuvwxyz'

def main():
    init()
    show_intro_message()
    message = get_message(STRINGS_DICTIONARY.enter_message)
    show_hacked_message_options(message.lower())

def show_hacked_message_options(message):
    for key in range(MIN_KEY, MAX_KEY + 1):
        option = decrypt(message, key)
        print(STRINGS_DICTIONARY.option.format(key, option))

def decrypt(message, key):
    return ''.join([get_shifted_char(char, -key) for char in message])

def get_shifted_char(char, key):
    if not char.isalpha():
        return char

    char_ord_in_abc = ABC.index(char)
    new_char_ord_in_abc = char_ord_in_abc + key

    if new_char_ord_in_abc < 0:
        new_char_ord_in_abc += len(ABC)
    elif new_char_ord_in_abc >= len(ABC):
        new_char_ord_in_abc -= len(ABC)

    return chr(new_char_ord_in_abc + ord('a'))

def get_message(prompt_text):
    message = input(prompt_text)

    while not message:
        message = input(STRINGS_DICTIONARY.invalid_message)

    return message

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Caesar Cipher Hacker

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana
    '''
    STRINGS_DICTIONARY.enter_message = '''
    Enter the encrypted Caesar cipher message to hack: '''
    STRINGS_DICTIONARY.invalid_message = '''
    Message cannot be empty. Please enter the message: '''
    STRINGS_DICTIONARY.option = '''
    Key #{}: {}'''

class StringsDictionary:
    pass

main()
