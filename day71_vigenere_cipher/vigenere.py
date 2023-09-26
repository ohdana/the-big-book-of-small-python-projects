from engine import Engine

ENCRYPT, DECRYPT = 'e', 'd'
ENGINE = None

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    while True:
        user_request = get_user_request()
        if user_request == ENCRYPT:
            encrypt()
        else:
            decrypt()

def get_user_request():
    print(STRINGS_DICTIONARY.encrypt_or_decrypt)
    user_request = input(STRINGS_DICTIONARY.input).lower()
    while not user_request in [ENCRYPT, DECRYPT]:
        return get_user_request()
    return user_request

def encrypt():
    message = get_message_from_user(STRINGS_DICTIONARY.enter_message_encrypt)
    key = get_key_from_user()
    return ENGINE.encrypt(message, key)

def decrypt():
    message = get_message_from_user(STRINGS_DICTIONARY.enter_message_decrypt)
    key = get_key_from_user()
    return ENGINE.decrypt(message, key)

def get_key_from_user():
    print(STRINGS_DICTIONARY.specify_key)
    user_input = input(STRINGS_DICTIONARY.input).upper()
    while not is_valid_key(user_input):
        return get_key_from_user()
    return user_input

def is_valid_key(user_input):
    if not user_input:
        return False

    return all([char.isalpha() for char in user_input])

def get_message_from_user(text_to_display):
    print(text_to_display)
    user_input = input(STRINGS_DICTIONARY.input)
    while not user_input:
        return get_message_from_user(text_to_display)
    return user_input

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)


def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)


def init():
    init_strings_dictionary()
    init_engine()

def init_engine():
    global ENGINE
    ENGINE = Engine()


##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Vigenère Cipher

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The Vigenère cipher is a polyalphabetic substitution cipher that was
    powerful enough to remain unbroken for centuries.'''
    STRINGS_DICTIONARY.encrypt_or_decrypt = '''
    Do you want to (e)ncrypt or (d)ecrypt?'''
    STRINGS_DICTIONARY.specify_key = '''
    Please specify the key to use.
    It can be a word or any combination of letters:'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.enter_message_encrypt = '''
    Enter the message to encrypt.'''
    STRINGS_DICTIONARY.enter_message_decrypt = '''
    Enter the message to decrypt.'''
    STRINGS_DICTIONARY.encrypted_message = '''
    Encrypted message:
    {}'''
    STRINGS_DICTIONARY.encrypted_message = '''
    Decrypted message:
    {}'''

class StringsDictionary:
    pass

main()
