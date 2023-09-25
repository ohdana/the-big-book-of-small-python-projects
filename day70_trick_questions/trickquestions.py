def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    pass

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init():
    init_strings_dictionary()
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Trick Questions

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Can you figure out the answers to these trick questions?
    (Enter QUIT to quit at any time.)'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.press_enter_to_begin = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.press_enter_for_next_question = '''
    Press Enter for the next question...'''
    STRINGS_DICTIONARY.input = '''
        ANSWER: '''
    STRINGS_DICTIONARY.question = '''
    QUESTION: '''
    STRINGS_DICTIONARY.stats = '''
    Question: {}
    Score: {} / {}'''
    STRINGS_DICTIONARY.incorrect = '''
    {}. The answer is: {}.'''
    STRINGS_DICTIONARY.correct = '''
    {}'''


class StringsDictionary:
    pass

main()

