YES, NO = 'y', 'n'
X, O = 'X', 'O'
PLAYERS = [X, O]
CELLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
HORIZONTAL_LINES = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
VERTICAL_LINES = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
DIAGONAL_LINES = [['1', '5', '9'], ['3', '5', '7']]
LINES = HORIZONTAL_LINES + VERTICAL_LINES + DIAGONAL_LINES

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
    turn = 0
    moves_log = {}
    show_canvas(moves_log)
    while not check_if_board_full(moves_log):
        player = PLAYERS[turn]
        make_move(moves_log, player)
        show_canvas(moves_log)
        is_winner = check_if_is_winner(moves_log, player)
        if is_winner:
            win(player)
            break
        turn = (turn + 1) % len(PLAYERS)
    tie()

def get_formatting_params(moves_log):
    return [get_cell_content(moves_log, cell) for cell in CELLS]

def get_cell_content(moves_log, cell):
    if cell in moves_log:
        return moves_log[cell]

    return ' '

def show_canvas(moves_log):
    formatting_params = get_formatting_params(moves_log)
    print(STRINGS_DICTIONARY.canvas.format(*formatting_params))

def make_move(moves_log, player):
    user_input = get_user_input(moves_log, player)
    moves_log[user_input] = player

def check_if_board_full(moves_log):
    return len(moves_log) == len(CELLS)

def check_if_is_winner(moves_log, player):
    for line in LINES:
        is_winning_line = all([get_cell_content(moves_log, cell) == player for cell in line])
        if is_winning_line:
            return True
    return False

def win(player):
    print(STRINGS_DICTIONARY.win.format(player))

def tie():
    print(STRINGS_DICTIONARY.tie)

def get_user_input(moves_log, player):
    print(STRINGS_DICTIONARY.move.format(player))
    user_input = input(STRINGS_DICTIONARY.input)
    while not is_valid_user_input(moves_log, user_input):
        return get_user_input(moves_log, player)
    return user_input

def is_valid_user_input(moves_log, user_input):
    if not user_input in CELLS:
        return False

    return user_input not in moves_log

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
    Welcome to Tic-Tac-Toe!

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The classic board game.'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.canvas = '''
    {}|{}|{}  1 2 3
    -+-+-
    {}|{}|{}  4 5 6
    -+-+-
    {}|{}|{}  7 8 9'''
    STRINGS_DICTIONARY.move = '''
    What is {}\'s move? (1-9)'''
    STRINGS_DICTIONARY.win = '''
    {} has won the game!'''
    STRINGS_DICTIONARY.tie = '''
    The game is a tie!'''

class StringsDictionary:
    pass

main()
