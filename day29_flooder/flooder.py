from frame import Frame

HEART, TRIANGLE, DIAMOND, BALL, CLUB, SPADE, CROSS = 'H', 'T', 'D', 'B', 'C', 'S', 'R'
CANVAS_WIDTH, CANVAS_HEIGHT = 10, 10
CURSOR_X, CURSOR_Y = 1, 1
INITIAL_N_OF_MOVES = 13

HEART_CHAR      = chr(9829)  # Character 9829 is '♥'
DIAMOND_CHAR    = chr(9830)  # Character 9830 is '♦'
SPADE_CHAR      = chr(9824)  # Character 9824 is '♠'
CLUB_CHAR       = chr(9827)  # Character 9827 is '♣'
BALL_CHAR       = chr(9679)  # Character 9679 is '●'
TRIANGLE_CHAR   = chr(9650)  # Character 9650 is '▲'
CROSS_CHAR   = '+'

YES, NO, QUIT = 'Y', 'N', 'QUIT'
EASY, MEDIUM, HARD = 'E', 'M', 'H'
DIFFICULTY_TYPES = {
    EASY: [HEART_CHAR, BALL_CHAR, CROSS_CHAR],
    MEDIUM: [HEART_CHAR, BALL_CHAR, TRIANGLE_CHAR, BALL_CHAR, CROSS_CHAR],
    HARD: [HEART_CHAR, DIAMOND_CHAR, SPADE_CHAR, CLUB_CHAR, BALL_CHAR, TRIANGLE_CHAR, CROSS_CHAR] }
DIFFICULTY_NAMES_MAP = {}
CHARS_MAP = { HEART: HEART_CHAR, DIAMOND: DIAMOND_CHAR, SPADE: SPADE_CHAR, CLUB: CLUB_CHAR,
    BALL: BALL_CHAR, TRIANGLE: TRIANGLE_CHAR, CROSS: CROSS_CHAR}

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = prompt_play_again()
    say_bye()

def play():
    moves_left = INITIAL_N_OF_MOVES
    difficulty = get_difficulty_level()
    available_chars = DIFFICULTY_TYPES[difficulty]
    frame = Frame(CANVAS_WIDTH, CANVAS_HEIGHT, available_chars)
    while True:
        print(STRINGS_DICTIONARY.moves_left.format(moves_left))
        frame.show_canvas()
        user_input = get_user_input()
        moves_left = make_move(frame, user_input, moves_left)
        if moves_left == 0 or frame.is_filled_up_with_one_char():
            break

    frame.show_canvas()
    show_results(frame, difficulty, INITIAL_N_OF_MOVES - moves_left)

def make_move(frame, user_input, moves_left):
    new_char = CHARS_MAP[user_input]
    old_char = frame.get()[CURSOR_Y][CURSOR_X]
    cells_to_update = frame.get_matching_neighbours(old_char, CURSOR_X, CURSOR_Y)
    cells_to_update.append((CURSOR_X, CURSOR_Y))
    update_cells(new_char, frame, cells_to_update)

    return moves_left - 1

def update_cells(char, frame, cells):
    for cell in cells:
        x, y = cell
        frame.update_cell(x, y, char)

def show_results(frame, difficulty, moves_used):
    print(STRINGS_DICTIONARY.difficulty.format(DIFFICULTY_NAMES_MAP[difficulty]))
    print(STRINGS_DICTIONARY.moves_used.format(moves_used, INITIAL_N_OF_MOVES))
    if player_won(frame):
        print(STRINGS_DICTIONARY.you_won)
    else:
        print(STRINGS_DICTIONARY.you_lost)

def player_won(frame):
    return frame.is_filled_up_with_one_char()

def get_difficulty_level():
    user_input = input(STRINGS_DICTIONARY.choose_difficulty_level)
    if user_input.upper() not in [EASY, MEDIUM, HARD]:
        return get_difficulty_level()

    return user_input.upper()

def get_user_input():
    global GAME_OVER
    user_input = input(STRINGS_DICTIONARY.choose_one)
    if user_input.upper() == QUIT:
        GAME_OVER = True
        return

    if user_input.upper() not in [HEART, TRIANGLE, DIAMOND, BALL, CLUB, SPADE, CROSS]:
        return get_user_input()

    return user_input.upper()

def prompt_play_again():
    answer = ''

    while not is_valid_y_n(answer):
        answer = input(STRINGS_DICTIONARY.play_again)

    return answer.upper() == YES

def is_valid_y_n(answer):
    if not answer:
        return False

    return answer.upper() in [YES, NO]

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init_difficulty_names_map():
    DIFFICULTY_NAMES_MAP[EASY] = STRINGS_DICTIONARY.easy
    DIFFICULTY_NAMES_MAP[MEDIUM] = STRINGS_DICTIONARY.medium
    DIFFICULTY_NAMES_MAP[HARD] = STRINGS_DICTIONARY.hard

def init():
    init_strings_dictionary()
    init_difficulty_names_map()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Flooder

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A colourful game where you try to fill the board with a single shape.
    Set the upper left colour/shape, which fills in all the adjacent squares of that shape. Try to make the
    entire board the same shape.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.colour_mode = '''
    Do you want to play in colourblind mode? y/n: '''
    STRINGS_DICTIONARY.moves_left = '''
    Moves left: {}'''
    STRINGS_DICTIONARY.you_won = '''
    You won!'''
    STRINGS_DICTIONARY.you_lost = '''
    You lost.'''
    STRINGS_DICTIONARY.choose_one = '''
    Choose one of (H)eart, (T)riangle, (D)iamond, (B)all, (C)lub, (S)pade, c(R)oss or QUIT: '''
    STRINGS_DICTIONARY.choose_difficulty_level = '''
    Choose the difficulty -- (E)asy, (M)edium, (H)ard: '''
    STRINGS_DICTIONARY.difficulty = '''
    Difficulty level: {}'''
    STRINGS_DICTIONARY.moves_used = '''
    Moves used: {} out of {}'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.easy = 'EASY'
    STRINGS_DICTIONARY.medium = 'MEDIUM'
    STRINGS_DICTIONARY.hard = 'HARD'

class StringsDictionary:
    pass

main()
