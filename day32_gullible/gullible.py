YES, NO = 'Y', 'N'

def main():
    init()
    show_intro_message()
    play()

def play():
    valid_answers = [YES, NO]
    while True:
        user_input = input(STRINGS_DICTIONARY.question)
        if user_input.upper() not in valid_answers:
            print(STRINGS_DICTIONARY.invalid_response.format(user_input))
        if user_input.upper() == NO:
            print(STRINGS_DICTIONARY.bye)
            break

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Gullible

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    How to keep a gullible person busy for hours. (This is a joke program.)'''
    STRINGS_DICTIONARY.question = '''
    Do you want to know how to keep a gullible person busy for hours? y/n: '''
    STRINGS_DICTIONARY.invalid_response = '''
    "{}" is not a valid yes/no response.'''
    STRINGS_DICTIONARY.bye = '''
    Thank you. Have a nice day!'''
class StringsDictionary:
    pass

main()
