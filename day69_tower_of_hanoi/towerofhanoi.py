YES, NO = 'y', 'n'

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
    pass

def get_user_input(player):
    print(STRINGS_DICTIONARY.move)
    user_input = input(STRINGS_DICTIONARY.input)
    while not is_valid_user_input(user_input):
        return get_user_input(player)
    return user_input

def is_valid_user_input(user_input):
    pass

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).lower()
    if not user_input in [YES, NO]:
        return do_play_again()

    return user_input == YES

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

class StringsDictionary:
    pass

main()
