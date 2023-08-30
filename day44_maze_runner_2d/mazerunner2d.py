import os
from maze import Maze

YES, NO = 'Y', 'N'
LIST = 'LIST'
W, A, S, D = 'W', 'A', 'S', 'D'

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    maze_filename = get_maze_filename()
    maze = Maze(maze_filename)
    maze.show_canvas()
    while not maze.is_completed():
        direction = get_direction(maze)
        maze.move(direction)
        maze.show_canvas()
    print(STRINGS_DICTIONARY.you_won)

def get_direction(maze):
    print(STRINGS_DICTIONARY.enter_direction)
    user_input = input(STRINGS_DICTIONARY.input)
    while not is_valid_direction(maze, user_input):
        return get_direction()

    return user_input.upper()

def is_valid_direction(maze, user_input):
    available_directions = maze.get_available_directions()
    if not user_input.upper() in available_directions:
        return False

    return True

def get_maze_filename():
    user_input = get_user_input()
    if not user_input:
        return get_maze_filename()
    if user_input == LIST:
        list_maze_files()
        return get_maze_filename()
    if file_exists(user_input):
        return user_input

    print(STRINGS_DICTIONARY.no_such_file.format(user_input))
    return get_maze_filename()

def list_maze_files():
    all_files = os.listdir()
    maze_files = [filename for filename in all_files if filename.endswith('.txt')]
    if not maze_files:
        print(STRINGS_DICTIONARY.no_maze_files)
    else:
        print('\n'.join(maze_files))

def get_user_input():
    print(STRINGS_DICTIONARY.enter_filename)
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_user_input()

    return user_input.upper()

def file_exists(user_input):
    return os.path.exists(user_input)

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
    Maze Runner 2D

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Move around a maze and try to escape.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.enter_filename = '''
    Enter the filename of the maze (or LIST): '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.files_found = '''
    Maze files found: '''
    STRINGS_DICTIONARY.no_such_file = '''
    There is no file named {}.'''
    STRINGS_DICTIONARY.no_maze_files = '''
    No maze files found.'''
    STRINGS_DICTIONARY.enter_direction = '''
                               W
    Enter direction, or QUIT: ASD'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.you_won = '''
    You have reached the exit! Good job!'''

class StringsDictionary:
    pass

main()
