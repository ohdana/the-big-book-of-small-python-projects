from frame import Frame

YES, NO = "Y", "N"
QUIT = 'QUIT'
PLAYER_1, PLAYER_2 = 'PLAYER_1', 'PLAYER_2'
PLAYERS = [PLAYER_1, PLAYER_2]
PLAYER_CHARS = { PLAYER_1: 'X', PLAYER_2: 'O' }

def main():
    init()
    show_intro_message()

    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()
    say_bye()

def play():
    frame = build_frame(PLAYER_CHARS.values())
    n_of_columns = frame.get_n_of_columns()
    turn = 0
    show_frame(frame)
    while True:
        if not frame.has_space():
            draw()
            break
        turn = (turn + 1) % len(PLAYERS)
        player = PLAYERS[turn]
        player_char = PLAYER_CHARS[player]
        user_input = get_user_input(player_char, n_of_columns)
        if user_input == QUIT:
            say_bye()
            break
        column_number = int(user_input)
        make_move(frame, player_char, column_number)
        show_frame(frame)
        winner = frame.get_winner()
        if winner:
            win(winner)
            break

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES


def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def make_move(frame, player_char, column_number):
    frame.throw_token(player_char, column_number)

def get_user_input(player_char, n_of_columns):
    user_input = input(STRINGS_DICTIONARY.enter_column.format(player_char)).upper()

    if not is_valid_user_input(user_input, n_of_columns):
        return get_user_input(player_char)

    return user_input

def is_valid_user_input(user_input, n_of_columns):
    if user_input == QUIT:
        return True

    if not user_input.isdigit():
        return False

    if 1 <= int(user_input) <= n_of_columns:
        return True

    return False

def draw():
    print('Draw!')

def win(winner):
    print('Player {} wins!'.format(winner))

def build_frame(chars):
    return Frame(chars)

def show_frame(frame):
    lines = [''.join(line) for line in frame.get()]
    print('\n'.join(lines))

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

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
    STRINGS_DICTIONARY.play_again = """
    Play again? y/n: """

class StringsDictionary:
    pass

main()
