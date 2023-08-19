from canvas import Canvas

HEART_CHAR      = chr(9829)  # Character 9829 is '♥'
SPADE_CHAR      = chr(9824)  # Character 9824 is '♠'

YES, NO, QUIT = 'Y', 'N', 'QUIT'
PLAYER_1, PLAYER_2 = 'PLAYER_1', 'PLAYER_2'
PLAYERS = [PLAYER_1, PLAYER_2]
PLAYER_CHARS = { PLAYER_1: HEART_CHAR, PLAYER_2: SPADE_CHAR }

GAME_OVER = False

def main():
    init()
    show_intro_message()

    play_again = True
    while play_again:
        reset_game()
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    canvas = get_canvas(PLAYER_CHARS.values())
    turn = 0
    show_canvas(canvas)
    while not GAME_OVER:
        player_char = PLAYER_CHARS[PLAYERS[turn]]
        take_turn(canvas, player_char)
        show_canvas(canvas)
        turn = calculate_turn(turn)
        calculate_turn_results(canvas)

def calculate_turn_results(canvas):
    winner = get_winner(canvas)
    if winner:
        win(winner)
        game_over()
    elif not canvas.has_space():
        draw()
        game_over()

def take_turn(canvas, player_char):
    column_numbers = canvas.get_column_numbers()
    user_input = get_user_input(player_char, column_numbers)
    if user_input == QUIT:
        game_over()
    else:
        column_number = int(user_input)
        make_move(canvas, player_char, column_number)

def game_over():
    set_game_over(True)

def reset_game():
    set_game_over(False)

def calculate_turn(turn):
    return (turn + 1) % len(PLAYERS)

def get_winner(canvas):
    return canvas.get_winning_token()

def make_move(canvas, player_char, column_number):
    canvas.throw_token(player_char, column_number)

def get_user_input(player_char, column_numbers):
    user_input = input(STRINGS_DICTIONARY.enter_column.format(player_char)).upper()

    if not is_valid_user_input(user_input, column_numbers):
        return get_user_input(player_char, column_numbers)

    return user_input

def is_valid_user_input(user_input, column_numbers):
    if user_input == QUIT:
        return True

    if not user_input.isdigit():
        return False

    min_column_number = min(column_numbers)
    max_column_number = max(column_numbers)
    if min_column_number <= int(user_input) <= max_column_number:
        return True

    return False

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def draw():
    print(STRINGS_DICTIONARY.draw)

def win(winner):
    print(STRINGS_DICTIONARY.player_wins.format(winner))

def get_canvas(chars):
    return Canvas(chars)

def show_canvas(canvas):
    lines = [''.join(line) for line in canvas.get()]
    print('\n'.join(lines))

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()

def set_game_over(value):
    global GAME_OVER
    GAME_OVER = value

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Four in a Row

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A tile-dropping game to get four in a row, similar to Connect Four.'''
    STRINGS_DICTIONARY.enter_column = '''
    Player {}, enter a column or QUIT: '''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.player_wins = '''
    Player {} wins!'''
    STRINGS_DICTIONARY.draw = '''
    It's a draw ._. '''

class StringsDictionary:
    pass

main()
