from game import Game

YES, NO = 'y', 'n'
QUIT = 'quit'

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    game = Game()
    show_board(game)
    while True:
        player_token_type = game.get_player_for_turn()
        announce_turn(player_token_type)
        coins_flip_result, points = game.flip_coins()
        if not points:
            announce_empty_move(coins_flip_result, player_token_type)
            game.pass_turn()
            continue
        tokens_to_move = game.get_tokens_to_move(player_token_type, points)
        user_input = get_user_input(tokens_to_move, coins_flip_result, points)
        if user_input is QUIT:
            break
        src_cell = user_input
        dest_cell = game.make_move(player_token_type, src_cell, points)
        show_board(game)
        if game.is_winner(player_token_type):
            announce_winner(player_token_type)
            break
        if game.got_extra_move(dest_cell):
            announce_extra_move(player_token_type)
        game.calculate_next_turn()

def announce_empty_move(coins_flip_result, token_type):
    formatted_flip_result = '-'.join(coins_flip_result)
    print(STRINGS_DICTIONARY.zero_points.format(formatted_flip_result, token_type))

def announce_extra_move(token_type):
    print(STRINGS_DICTIONARY.flower_cell.format(token_type))

def announce_turn(token_type):
    input(STRINGS_DICTIONARY.turn.format(token_type))

def get_user_input(tokens_to_move, coins_flip_result, points):
    formatted_flip_result = '-'.join(coins_flip_result)
    formatted_tokens_to_move = ', '.join(tokens_to_move)
    print(STRINGS_DICTIONARY.flip_result.format(formatted_flip_result, points, formatted_tokens_to_move))
    user_input = input(STRINGS_DICTIONARY.input).lower()

    if not is_valid_user_input(user_input, tokens_to_move):
        return get_user_input(tokens_to_move, coins_flip_result, points)

    return user_input

def is_valid_user_input(user_input, tokens_to_move):
    if user_input is QUIT:
        return True

    return user_input in tokens_to_move

def ask_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).lower()
    if not user_input in [YES, NO]:
        return ask_play_again()

    return user_input

def show_board(game):
    print(game.get_board_image())

def announce_winner(winner_token_type):
    print(STRINGS_DICTIONARY.winner.format(winner_token_type))

def init():
    init_strings_dictionary()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    The Royal Game of Ur

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    This is a 5,000 year old game. Two players must move their tokens
    from their home to their goal. On your turn you flip four coins and can
    move one token a number of spaces equal to the heads you got.

    Ur is a racing game; the first player to move all seven of their tokens
    to their goal wins. To do this, tokens must travel from their home to
    their goal:

              X Home      X Goal
                v           ^
  +---+---+---+-v-+       +-^-+---+
  |v<<<<<<<<<<<<< |       | ^<|<< |
  |v  |   |   |   |       |   | ^ |
  +v--+---+---+---+---+---+---+-^-+
  |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
  |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
  +^--+---+---+---+---+---+---+-v-+
  |^  |   |   |   |       |   | v |
  |^<<<<<<<<<<<<< |       | v<<<< |
  +---+---+---+-^-+       +-v-+---+
                ^           v
              O Home      O Goal

    If you land on an opponent's token in the middle track, it gets sent
    back home. The **flower** spaces let you take another turn. Tokens in
    the middle flower space are safe and cannot be landed on.

    More info https://en.wikipedia.org/wiki/Royal_Game_of_Ur'''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.turn = '''
    It is {}'s turn. Press Enter to flip...'''
    STRINGS_DICTIONARY.flip_result = '''
    Flips: {}  Select token to move {} spaces: {} or QUIT'''
    STRINGS_DICTIONARY.flower_cell = '''
    {} landed on a flower space and gets to go again.'''
    STRINGS_DICTIONARY.winner = '''
    {} wins!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.zero_points = '''
    Flips: {}. {} got 0 points...'''

class StringsDictionary:
    pass

main()

