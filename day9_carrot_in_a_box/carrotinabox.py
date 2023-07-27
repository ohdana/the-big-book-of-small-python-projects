import random

MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 5
BOX_COLOUR_1 = 'BLUE'
BOX_COLOUR_2 = 'GOLD'
IS_CARROT_IN_BOX_1 = False

def main():
    init()
    show_intro_message()
    play()

def play():
    play_again = True

    while play_again:
        player_names = [get_player_name(1), get_player_name(2)]
        show_closed_boxes(*player_names)
        peek_into_boxes(*player_names)
        clear_screen()
        say_truth_or_lie(*player_names)
        swap = offer_to_swap(*player_names)
        if swap:
            swap_boxes()
        reveal_boxes(*player_names)
        play_again = show_winner_and_play_again(*player_names)

    say_bye()

def show_winner_and_play_again(name1, name2):
    winner = name1
    if not IS_CARROT_IN_BOX_1:
        winner = name2

    play_again = input(STRINGS_DICTIONARY.winner.format(winner))

    while not is_valid_y_n(play_again):
        play_again = input(STRINGS_DICTIONARY.invalid_y_n)

    return play_again == 'y'

def say_truth_or_lie(name1, name2):
    print(STRINGS_DICTIONARY.say_sentence.format(name1, name2))
    input(STRINGS_DICTIONARY.press_enter)

def offer_to_swap(name1, name2):
    swap = input(STRINGS_DICTIONARY.swap_boxes.format(name2, name1))

    while not is_valid_y_n(swap):
        swap = input(STRINGS_DICTIONARY.invalid_y_n)

    return swap == 'y'

def show_closed_boxes(name1, name2):
    format_boxes_data = [BOX_COLOUR_1, BOX_COLOUR_2, name1, name2]
    print(STRINGS_DICTIONARY.closed_boxes.format(*format_boxes_data))
    print(STRINGS_DICTIONARY.you_have_box.format(name1, BOX_COLOUR_1))
    print(STRINGS_DICTIONARY.you_have_box.format(name2, BOX_COLOUR_2))
    input(STRINGS_DICTIONARY.press_enter)

def peek_into_boxes(name1, name2):
    print(STRINGS_DICTIONARY.you_get_to_look.format(name1))
    print(STRINGS_DICTIONARY.dont_look.format(name2))
    print(STRINGS_DICTIONARY.closed_eyes.format(name2))
    print(STRINGS_DICTIONARY.inside_of_box.format(name1))

    put_carrot_in_random_box()
    if IS_CARROT_IN_BOX_1:
        print(STRINGS_DICTIONARY.box1_carrot.format(BOX_COLOUR_1, BOX_COLOUR_2, name1, name2))
    else:
        print(STRINGS_DICTIONARY.box1_empty.format(BOX_COLOUR_1, BOX_COLOUR_2, name1, name2))
    input(STRINGS_DICTIONARY.press_enter)

def swap_boxes():
    global IS_CARROT_IN_BOX_1
    IS_CARROT_IN_BOX_1 = not IS_CARROT_IN_BOX_1

def reveal_boxes(name1, name2):
    print(STRINGS_DICTIONARY.opening_boxes)
    if IS_CARROT_IN_BOX_1:
        print(STRINGS_DICTIONARY.carrot_in_box1.format(BOX_COLOUR_1, BOX_COLOUR_2, name1, name2))
    else:
        print(STRINGS_DICTIONARY.carrot_in_box2.format(BOX_COLOUR_1, BOX_COLOUR_2, name1, name2))

def put_carrot_in_random_box():
    global IS_CARROT_IN_BOX_1
    IS_CARROT_IN_BOX_1 = random.randint(1, 2) == 1

def clear_screen():
    print('\n' * 100)

def get_player_name(n_of_player):
    name = input(STRINGS_DICTIONARY.player_enter_name.format(n_of_player))

    while not is_valid_name_input(name):
        name = input(STRINGS_DICTIONARY.invalid_name)

    return name

def is_valid_y_n(text):
    if not text:
        return False

    return text in ['y', 'n']

def is_valid_name_input(name):
    if not name:
        return False

    if not (MIN_NAME_LENGTH <= len(name) <= MAX_NAME_LENGTH):
        return False

    return True

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
    Carrot in a Box

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    This is a bluffing game for two human players. Each player has a box.
    One box has a carrot in it. To win, you must have the box with
    the carrot in it.

    This is a very simple and silly game.

    The first player looks into their box (the second player must close
    their eyes during this). The first player then says 'There is a carrot
    in my box' or 'There is not a carrot in my box'. The second player then
    gets to decide if they want to swap boxes or not.'''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter when ready...'''
    STRINGS_DICTIONARY.player_enter_name = '''
    Player {}, enter your name: '''
    STRINGS_DICTIONARY.invalid_name = '''
    Please use the name that would be {}-{} characters long:
    '''.format(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
    STRINGS_DICTIONARY.here_are_boxes = '''
    HERE ARE TWO BOXES: '''
    STRINGS_DICTIONARY.you_have_box = '''
    {}, you have a {} box in front of you.'''
    STRINGS_DICTIONARY.you_get_to_look = '''
    {}, you will get to look into your box.'''
    STRINGS_DICTIONARY.dont_look = '''
    {}, close your eyes and don't look!!!'''
    STRINGS_DICTIONARY.closed_eyes = '''
    When {} has closed their eyes, press Enter...'''
    STRINGS_DICTIONARY.inside_of_box = '''
    {} here is the inside of your box: '''
    STRINGS_DICTIONARY.open_eyes = '''
    {}, tell {} to open their eyes.'''
    STRINGS_DICTIONARY.say_sentence = '''
    {}, say one of the following sentences to {}:
       1. There is a carrot in my box.
       2. There is no carrot in my box.'''
    STRINGS_DICTIONARY.swap_boxes = '''
    {}, do you want to swap boxes with {}? y/n: '''
    STRINGS_DICTIONARY.invalid_y_n = '''
    Please use \'y\' for \'yes\' and \'n\' for \'no\': '''
    STRINGS_DICTIONARY.opening_boxes = '''
    Opening the boxes...'''
    STRINGS_DICTIONARY.winner = '''
    {} wins! Play again? y/n: '''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.closed_boxes = '''
      _________    _________
     /        /|  /        /|
    +--------+ | +--------+ |
    |  {}  | | |  {}  | |
    |  BOX   | / |  BOX   | /
    +--------+   +--------+
       {}        {}       '''
    STRINGS_DICTIONARY.box1_empty = '''
       --------
      |        |
      |        |
      |________|    _________
     /        /|   /        /|
    +--------+ |  +--------+ |
    |  {}  | |  |  {}  | |
    |  BOX   | /  |  BOX   | /
    +--------+    +--------+'
       {}        {}       '''
    STRINGS_DICTIONARY.box1_carrot = '''
        V V V
       --V V---
      |   V    |
      |  VVV   |
      |__| |___|    _________
     /   | |  /|   /        /|
    +--------+ |  +--------+ |
    |  {}  | |  |  {}  | |
    |  BOX   | /  |  BOX   | /
    +--------+    +--------+'
       {}        {}       '''
    STRINGS_DICTIONARY.carrot_in_box1 = '''
        V V V
       --V-V---      --------
      |   V    |    |        |
      |  VVV   |    |        |
      |__| |___|    |________|
     /   | |  /|   /        /|
    +--------+ |  +--------+ |
    |  {}  | |  |  {}  | |
    |  BOX   | /  |  BOX   | /
    +--------+    +--------+
       {}        {}       '''
    STRINGS_DICTIONARY.carrot_in_box2 = '''
                      V V V
       --------      --V-V---
      |        |    |   V    |
      |        |    |  VVV   |
      |________|    |__| |___|
     /        /|   /   | |  /|
    +--------+ |  +--------+ |
    |  {}  | |  |  {}  | |
    |  BOX   | /  |  BOX   | /
    +--------+    +--------+
       {}        {}       '''
class StringsDictionary:
    pass

main()

