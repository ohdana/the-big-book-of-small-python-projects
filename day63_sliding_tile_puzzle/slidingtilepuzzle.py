YES, NO = 'Y', 'N'
QUIT = 'QUIT'
EMPTY = ' '
W, A, S, D = 'W', 'A', 'S', 'D'
DIRECTIONS = [W, A, S, D]
ENGINE = None

import time
from gameengine import GameEngine

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    play_again = True
    while play_again:
        play_new_game()
        play_again = do_play_again()

def play_new_game():
    input(STRINGS_DICTIONARY.press_enter)
    ENGINE.start_game()
    while not ENGINE.is_win():
        ENGINE.show_canvas()
        user_input = get_user_input()
        if user_input == QUIT:
            break
        ENGINE.move(user_input)
    show_you_win()

def show_you_win():
    print(STRINGS_DICTIONARY.you_win)

def get_user_input():
    formatted_avaialble_moves = get_formatted_avaialble_moves()
    print(STRINGS_DICTIONARY.enter_wasd.format(*formatted_avaialble_moves))
    user_input = input(STRINGS_DICTIONARY.input).upper()
    if not user_input in (DIRECTIONS + [QUIT]):
        return get_user_input()

    return user_input

def get_formatted_avaialble_moves():
    available_moves = ENGINE.get_available_moves()
    params = []
    for direction in DIRECTIONS:
        if direction in available_moves:
            params.append(direction)
        else:
            params.append(EMPTY)

    return params

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).upper()
    if not user_input in [YES, NO]:
        return do_play_again()

    return user_input == YES

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init_game_engine():
    global ENGINE
    ENGINE = GameEngine()

def init():
    init_strings_dictionary()
    init_game_engine()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Sliding Tile Puzzle

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Use the WASD keys to move the tiles
    back into their original order:
           1  2  3  4
           5  6  7  8
           9 10 11 12
          13 14 15'''
    STRINGS_DICTIONARY.enter_wasd = '''
                              ({})
    Enter WASD (or QUIT): ({}) ({}) ({})
    '''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.you_win = '''
    You win!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''

class StringsDictionary:
    pass

main()
