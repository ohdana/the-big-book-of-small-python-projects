from canvas import Canvas

GAME_OVER = None
YES, NO = 'Y', 'N'
Q, W, E, D, C, X, A, Z, TELEPORT = 'Q', 'W', 'E', 'D', 'C', 'X', 'A', 'Z', 'T'
DIRECTIONS = [Q, W, E, A, D, Z, X, C]
QUIT = 'QUIT'
INITIAL_NUM_ALIVE_ROBOTS = 10
INITIAL_NUM_DEAD_ROBOTS = 2
INITIAL_NUM_TELEPORTS = 2

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    canvas = Canvas(INITIAL_NUM_ALIVE_ROBOTS, INITIAL_NUM_DEAD_ROBOTS, INITIAL_NUM_TELEPORTS)
    while not GAME_OVER:
        canvas.show_canvas()
        make_player_move(canvas)
        make_robots_move(canvas)

        if GAME_OVER:
            break

def make_player_move(canvas):
    user_input = get_user_input(canvas)
    if user_input == QUIT:
        game_over()
    elif user_input == TELEPORT:
        teleport(canvas)
    else:
        canvas.move_player(user_input)

def make_robots_move(canvas):
    canvas.move_robots()
    if canvas.is_player_eaten():
        player_lost()
    elif canvas.are_all_robots_dead():
        player_wins()

def teleport(canvas):
    canvas.teleport()

def get_user_input(canvas):
    available_directions = get_player_available_directions(canvas)
    print(STRINGS_DICTIONARY.enter_move.format(*available_directions))
    print(STRINGS_DICTIONARY.teleports_remaining.format(canvas.get_n_of_teleport()))
    user_input = input(STRINGS_DICTIONARY.input)
    if not is_valid_user_input(user_input, available_directions):
        return get_user_input(canvas)

    return user_input.upper()

def get_player_available_directions(canvas):
    available_directions = canvas.get_player_available_directions()
    ordered_directions = []
    for direction in DIRECTIONS:
        if direction in available_directions:
            ordered_directions.append(direction)
        else:
            ordered_directions.append(' ')

    return ordered_directions

def is_valid_user_input(user_input, available_directions):
    valid_inputs = DIRECTIONS + [QUIT] + [TELEPORT]
    return user_input.upper() in valid_inputs

def player_wins():
    canvas.show_canvas()
    print(STRINGS_DICTIONARY.you_won)
    game_over()

def player_lost():
    canvas.show_canvas()
    print(STRINGS_DICTIONARY.you_lost)
    game_over()

def game_over():
    set_game_over(True)

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def set_game_over(value):
    global GAME_OVER
    GAME_OVER = value

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
    Hungry Robots

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    You are trapped in a maze with hungry robots! You don't know why robots
    need to eat, but you don't want to find out. The robots are badly
    programmed and will move directly toward you, even if blocked by walls.
    You must trick the robots into crashing into each other (or dead robots)
    without being caught. You have a personal teleporter device, but it only
    has enough battery for {} trips. Keep in mind, you and robots can slip
    through the corners of two diagonal walls!'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.enter_move = '''
                        ({}) ({}) ({})
                        ({}) (S) ({})
    Enter move or QUIT: ({}) ({}) ({})'''
    STRINGS_DICTIONARY.teleports_remaining = '''
    (T)eleports remaining: {}'''
    STRINGS_DICTIONARY.input = '''
    >'''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.you_won = '''
    All the robots have crashed into each other and you
    lived to tell the tale! Good job!'''
    STRINGS_DICTIONARY.you_lost = '''
    You have been caught by a robot!'''

class StringsDictionary:
    pass

main()
