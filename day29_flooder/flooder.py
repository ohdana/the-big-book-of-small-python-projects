YES, NO, QUIT = 'Y', 'N', 'QUIT'
HEART, TRIANGLE, DIAMOND, BALL, CLUB, SPADE = 'H', 'T', 'D', 'B', 'C', 'S'
GAME_OVER = False
CANVAS_WIDTH = 20
CANVAS_HEIGHT = 20
INITIAL_N_OF_MOVES = 13

def main():
    init()
    show_intro_message()
    play()

def play():
    user_input = get_user_input()
    while not GAME_OVER:
        pass

    say_bye()

def get_user_input():
    global GAME_OVER
    user_input = input(STRINGS_DICTIONARY.choose_one)
   if user_input.upper() == QUIT:
        GAME_OVER = True
        return

    if user_input.upper() not in [HEART, TRIANGLE, DIAMOND, BALL, CLUB, SPADE]:
        return get_user_input()

    return user_input

def prompt_play_again():
    answer = ''

    while not is_valid_y_n(answer):
        answer = input(STRINGS_DICTIONARY.play_again)

    return answer.upper() == YES

def is_valid_y_n(answer):
    if not answer:
        return False

    return answer in [YES, NO]

def reset_canvas():
    pass

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Flooder

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A colourful game where you try to fill the board with a single colour. Has
    a mode for colourblind players.
    Set the upper left colour/shape, which fills in all the adjacent squares of that colour/shape. Try to make the
    entire board the same colour/shape.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.colour_mode = '''
    Do you want to play in colourblind mode? y/n: '''
    STRINGS_DICTIONARY.moves_left = '''
    Moves left: '''
    STRINGS_DICTIONARY.you_won = '''
    You won!'''
    STRINGS_DICTIONARY.no_moves_left = '''
    You ran out of moves.'''
    STRINGS_DICTIONARY.choose_one = '''
    Choose one of (H)eart, (T)riangle, (D)iamond, (B)all, (C)lub, (S)pade or QUIT: '''

class StringsDictionary:
    pass

main()
