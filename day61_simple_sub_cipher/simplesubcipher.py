from subcipherengine import SubCipherEngine

ENCRYPT, DECRYPT = 'e', 'd'
RANDOM = 'RANDOM'
ENGINE = None

def main():
    init()
    show_intro_message()
    play()

def play():
    while True:
        user_request = get_user_request()
        if user_request == ENCRYPT:
            encrypt()
        else:
            decrypt()

def encrypt():
    print(STRINGS_DICTIONARY.provide_key)
    print(STRINGS_DICTIONARY.enter_random)
    key = get_key()
    message = get_message_to_encrypt()
    encrypted_message = ENGINE.encrypt(key, message)
    show_encrypted_message(encrypted_message)

def decrypt():
    print(STRINGS_DICTIONARY.provide_key)
    key = get_key()
    message = get_message_to_decrypt()
    decrypted_message = ENGINE.decrypt(key, message)
    show_decrypted_message(decrypted_message)

def show_encrypted_message(message):
    print(STRINGS_DICTIONARY.encrypted_message.format(message))

def show_decrypted_message(message):
    print(STRINGS_DICTIONARY.decrypted_message.format(message))

def get_message_to_encrypt():
    print(STRINGS_DICTIONARY.enter_message_encrypt)
    user_input = input(STRINGS_DICTIONARY.input)
    while not user_input:
        return get_message_to_encrypt()
    return user_input

def get_message_to_decrypt():
    print(STRINGS_DICTIONARY.enter_message_decrypt)
    user_input = input(STRINGS_DICTIONARY.input)
    while not user_input:
        return get_message_to_decrypt()
    return user_input

def get_key():
    user_input = input(STRINGS_DICTIONARY.input)
    key = user_input.upper()
    if user_input.upper() == RANDOM:
        key = ENGINE.generate_key()
        print(STRINGS_DICTIONARY.key.format(key))

    while not ENGINE.is_valid_key(key):
        return get_key()

    return key

def get_user_request():
    print(STRINGS_DICTIONARY.encrypt_or_decrypt)
    user_input = input(STRINGS_DICTIONARY.input).lower()
    if user_input not in [ENCRYPT, DECRYPT]:
        return get_user_request()

    return user_input

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init_engine():
    global ENGINE
    ENGINE = SubCipherEngine()

def init():
    init_strings_dictionary()
    init_engine()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Simple Substitution Cipher

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A simple substitution cipher has a one-to-one translation for each
    symbol in the plaintext and each symbol in the ciphertext.'''
    STRINGS_DICTIONARY.encrypt_or_decrypt = '''
    Do you want to (e)ncrypt or (d)ecrypt?'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.enter_random = '''
    Or enter RANDOM to have one generated for you.'''
    STRINGS_DICTIONARY.key = '''
    The key is {}. KEEP THIS SECRET!'''
    STRINGS_DICTIONARY.enter_message_encrypt = '''
    Enter the message to encrypt.'''
    STRINGS_DICTIONARY.enter_message_decrypt = '''
    Enter the message to decrypt.'''
    STRINGS_DICTIONARY.encrypted_message = '''
    The encrypted message is:
    {}'''
    STRINGS_DICTIONARY.decrypted_message = '''
    The decrypted message is:
    {}'''
    STRINGS_DICTIONARY.provide_key = '''
    Please specify the key to use.'''

class StringsDictionary:
    pass

main()
