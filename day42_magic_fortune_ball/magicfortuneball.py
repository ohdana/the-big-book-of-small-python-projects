from magicball import MagicBall

YES, NO = 'Y', 'N'

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    ball = MagicBall()
    question = get_question()
    ball.get_answer()

def get_question():
    question = input(STRINGS_DICTIONARY.input)
    if not question:
        return get_question()

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

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Lucky Start

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana
    Ask a yes/no question about your future. Inspired by the Magic 8 Ball.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.input = '''
    >'''

class StringsDictionary:
    pass

main()
