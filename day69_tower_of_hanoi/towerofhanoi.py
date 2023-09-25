from gameengine import GameEngine

YES, NO = 'Y', 'N'
QUIT = 'QUIT'
A, B, C = 'A', 'B', 'C'
TOWERS = [A, B, C]
TOWER_SRC = A
TOWER_DEST = C
N_OF_DISCS = 5
GAME_ENGINE = None

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    play_again = True
    while play_again:
        start_new_game()
        play_again = do_play_again()

def start_new_game():
    GAME_ENGINE.start_new_game()
    GAME_ENGINE.show()
    while not GAME_ENGINE.is_game_over():
        user_input = get_user_input()
        if user_input == QUIT:
            return

        tower_src, tower_dest = parse_move(user_input)
        GAME_ENGINE.move(tower_src, tower_dest)
        GAME_ENGINE.show()
    show_congrats()

def get_user_input():
    print(STRINGS_DICTIONARY.move)
    user_input = input(STRINGS_DICTIONARY.input).upper()
    while not is_valid_user_input(user_input):
        return get_user_input()
    return user_input

def parse_move(user_input):
    if len(user_input) < 2:
        return None, None

    return user_input[0], user_input[1]

def is_valid_user_input(user_input):
    if user_input == QUIT:
        return True

    tower_src, tower_dest = parse_move(user_input)
    if tower_src not in TOWERS:
        return False

    if tower_dest not in TOWERS:
        return False

    return True

def show_congrats():
    print(STRINGS_DICTIONARY.win)

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).upper()
    if not user_input in [YES, NO]:
        return do_play_again()

    return user_input == YES

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init():
    init_strings_dictionary()
    init_game_engine()

def init_game_engine():
    global GAME_ENGINE
    GAME_ENGINE = GameEngine(TOWERS, TOWER_SRC, TOWER_DEST, N_OF_DISCS)
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    The Tower of Hanoi

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Move the tower of disks, one disk at a time, to another tower. Larger
    disks cannot rest on top of a smaller disk.

    More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.move = '''
    Enter the letters of "from" and "to" towers, or QUIT.
    (e.g. AB to moves a disk from tower A to tower B.)'''
    STRINGS_DICTIONARY.win = '''
    You have solved the puzzle! Well done!'''

class StringsDictionary:
    pass

main()
