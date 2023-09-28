from game import Game

QUIT = 'q'
YES, NO = 'y', 'n'
W, A, S, D = 'w', 'a', 's', 'd'

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    play_again = True
    while play_again:
        start_new_game()
        play_again = ask_play_again()

def start_new_game():
    game = Game()
    game.show_board()
    while game.can_make_move():
        user_input = get_user_input()
        if user_input == QUIT:
            return
        game.make_move(user_input)
        game.show_board()
    show_loss_message()

def show_loss_message():
    print(STRINGS_DICTIONARY.you_lost)

def get_user_input():
    print(STRINGS_DICTIONARY.enter_move)
    user_input = input(STRINGS_DICTIONARY.input).lower()
    if not user_input in [W, A, S, D, QUIT]:
        return get_user_input()
    return user_input

def ask_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).lower()
    while not user_input in [YES, NO]:
        return ask_play_again()
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

    STRINGS_DICTIONARY.intro_message = """
    Twenty Forty-Eight

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A sliding tile game to combine exponentially-increasing numbers.
    Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
    1024, which in turn is a clone of the Threes! game.
    More info at https://en.wikipedia.org/wiki/2048_(video_game)

    Slide all the tiles on the board in one of four directions. Tiles with
    like numbers will combine into larger-numbered tiles. A new 2 or 4 tile is
    added to the board on each move. You win if you can create a 2048 tile.
    You lose if the board fills up the tiles before then."""

    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.enter_move = '''
    Enter move: (WASD or Q to quit)'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.score = '''
    Score: {}'''
    STRINGS_DICTIONARY.you_won = '''
    Congratulations! You reached 2048!'''
    STRINGS_DICTIONARY.you_lost = '''
    Game over. Thanks for playing!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''

class StringsDictionary:
    pass


main()
