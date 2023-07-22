MIN_KEY = 0
MAX_KEY = 25
ABC='abcdefghijklmnopqrstuvwxyz'

def main():
    init()
    show_intro_message()

    while True:
        play()

def play():
    action = input(STRINGS_DICTIONARY.encrypt_or_decrypt)

    while not is_valid_action(action):
        action = input(STRINGS_DICTIONARY.invalid_encrypt_or_decrypt)

    if action == 'e':
        trigger_action_encrypt()
    elif action == 'd':
        trigger_action_decrypt()

    print(STRINGS_DICTIONARY.separator)

def trigger_action_encrypt():
    user_message = input(STRINGS_DICTIONARY.enter_message_encrypt)

    key = input(STRINGS_DICTIONARY.enter_the_key)
    while not is_valid_key(key):
        key = input(STRINGS_DICTIONARY.enter_the_key)

    encrypted_message = encrypt(user_message.lower(), int(key))
    print(STRINGS_DICTIONARY.your_encrypted_message.format(encrypted_message))

def trigger_action_decrypt():
    user_message = input(STRINGS_DICTIONARY.enter_message_decrypt)

    key = input(STRINGS_DICTIONARY.enter_the_key)
    decrypted_message = decrypt(user_message.lower(), int(key))

    while not is_valid_key(key):
        key = input(STRINGS_DICTIONARY.enter_the_key)
    print(STRINGS_DICTIONARY.your_decrypted_message.format(decrypted_message))

def is_valid_key(key):
    if not key.isdigit():
        return False
    return MIN_KEY <= int(key) <= MAX_KEY

def is_valid_action(action):
    if not action in ['e', 'd']:
        return False

    return True

def encrypt(message, key):
    return ''.join([get_shifted_char(char, key) for char in message])

def decrypt(message, key):
    return ''.join([get_shifted_char(char, -key) for char in message])

def get_shifted_char(char, key):
    if not char.isalpha():
        return char

    char_ord_in_abc = ABC.index(char)
    new_char_ord_in_abc = char_ord_in_abc + key
    if new_char_ord_in_abc < 0:
        new_char_ord_in_abc = len(ABC) - new_char_ord_in_abc
    elif new_char_ord_in_abc > len(ABC):
        new_char_ord_in_abc -= len(ABC)

    return chr(new_char_ord_in_abc + ord('a'))

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Caesar Cipher

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana'''

    STRINGS_DICTIONARY.encrypt_or_decrypt = '''
    Do you want (e)ncrypt or (d)ecrypt? '''
    STRINGS_DICTIONARY.invalid_encrypt_or_decrypt = '''
    Please enter \'e\' to encrypt or \'d\' to decrypt: '''

    STRINGS_DICTIONARY.enter_the_key = '''
    Please enter the key ({min_key} to {max_key}) to use:
    '''.format(min_key=MIN_KEY, max_key=MAX_KEY)
    STRINGS_DICTIONARY.enter_message_decrypt = '''
    Please enter the message to decrypt: '''
    STRINGS_DICTIONARY.enter_message_encrypt = '''
    Please enter the message to encrypt: '''
    STRINGS_DICTIONARY.your_encrypted_message = '''
    Your encrypted message: {}'''
    STRINGS_DICTIONARY.your_decrypted_message = '''
    Your decrypted message: {}'''
    STRINGS_DICTIONARY.separator = '''
    ************************************************'''

class StringsDictionary:
    pass

main()
