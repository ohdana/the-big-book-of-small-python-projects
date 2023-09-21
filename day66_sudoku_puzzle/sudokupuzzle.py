import time, re
from sudokugrid import SudokuGrid

RESET, NEW, UNDO, ORIGINAL, QUIT = 'RESET', 'NEW', 'UNDO', 'ORIGINAL', 'QUIT'
MOVE_REGEX = '^[ABCDEFGHI][123456789] [123456789]$'
YES, NO = 'Y', 'N'

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
    grid = SudokuGrid()
    while not grid.is_solved():
        grid.show_canvas()
        if grid.is_full():
            grid_full()
        user_input = get_user_input()
        if user_input == QUIT:
            break
        elif user_input == RESET:
            grid.reset()
        elif user_input == NEW:
            grid = SudokuGrid()
        elif user_input == ORIGINAL:
            show_original(grid)
        elif user_input == UNDO:
            grid.undo()
        else:
            make_move(user_input, grid)
    grid.show_canvas()
    grid_solved()

def grid_full():
    print(STRINGS_DICTIONARY.grid_full)

def grid_solved():
    print(STRINGS_DICTIONARY.grid_solved)

def get_user_input():
    print(STRINGS_DICTIONARY.user_input)
    user_input = input(STRINGS_DICTIONARY.input).upper()
    while not is_valid_user_input(user_input):
        return get_user_input()
    return user_input

def is_valid_user_input(user_input):
    if user_input in [RESET, NEW, UNDO, ORIGINAL, QUIT]:
        return True

    regex_match = re.search(MOVE_REGEX, user_input)
    if regex_match:
       return True

    return False

def make_move(move, grid):
    cell_id, cell_new_value = parse_move(move)
    print(cell_id, cell_new_value)
    grid.make_move(cell_id, cell_new_value)

def parse_move(move):
    parsed_move = move.split(' ')

    return parsed_move[0], parsed_move[1]

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).upper()
    if not user_input in [YES, NO]:
        return do_play_again()

    return user_input == YES

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)
    input(STRINGS_DICTIONARY.press_enter)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init():
    init_strings_dictionary()
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Sudoku Puzzle

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The classic 9x9 number placement puzzle.
    More info at https://en.wikipedia.org/wiki/Sudoku'''
    STRINGS_DICTIONARY.user_input = '''
    Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:
    (For example, a move looks like "B4 9".)'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.grid_full = '''
    Ooops.
    The grid is full but it's not solved (yet!).
    Seems like there's a mistake somewhere...'''
    STRINGS_DICTIONARY.grid_solved = '''
    Congratulations! You solved the puzzle!'''

class StringsDictionary:
    pass

main()
