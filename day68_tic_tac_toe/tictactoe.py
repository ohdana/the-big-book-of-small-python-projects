YES, NO = 'y', 'n'
X, O = 'X', 'O'
PLAYERS = [X, O]
CELLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
HORIZONTAL_LINES = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
VERTICAL_LINES = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
DIAGONAL_LINES = [['1', '5', '9'], ['3', '5', '7']]
LINES = HORIZONTAL_LINES + VERTICAL_LINES + DIAGONAL_LINES
MOVES = None

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

def reset_moves_log():
    global MOVES
    MOVES = {}

def start_new_game():
    reset_moves_log()
    turn = 0
    show_canvas()
    while not check_if_board_full():
        player = PLAYERS[turn]
        make_move(player)
        show_canvas()
        if is_winner(player):
            announce_win(player)
            return
        turn = callculate_turn(turn)
    announce_tie()

def callculate_turn(curr_turn):
    return (curr_turn + 1) % len(PLAYERS)

def make_move(player):
    user_input = get_user_input(player)
    MOVES[user_input] = player

def check_if_board_full():
    return len(MOVES) == len(CELLS)

def is_winner(player):
    for line in LINES:
        is_winning_line = all([get_cell_content(cell) == player for cell in line])
        if is_winning_line:
            return True
    return False

def announce_win(player):
    print(STRINGS_DICTIONARY.win.format(player))

def announce_tie():
    print(STRINGS_DICTIONARY.tie)

def show_canvas():
    formatting_params = get_formatting_params()
    print(STRINGS_DICTIONARY.canvas.format(*formatting_params))

def get_formatting_params():
    return [get_cell_content(cell) for cell in CELLS]

def get_cell_content(cell):
    if cell in MOVES:
        return MOVES[cell]

    return ' '

def get_user_input(player):
    print(STRINGS_DICTIONARY.move.format(player))
    user_input = input(STRINGS_DICTIONARY.input)
    while not is_valid_user_input(user_input):
        return get_user_input(player)
    return user_input

def is_valid_user_input(user_input):
    if not user_input in CELLS:
        return False

    return user_input not in MOVES

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
