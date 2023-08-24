from canvas import Canvas

GAME_OVER = None
YES, NO = 'Y', 'N'
Q, W, E, D, C, X, A, Z = 'Q', 'W', 'E', 'D', 'C', 'X', 'A', 'Z'
DIRECTIONS = [Q, W, E, D, C, X, A, Z]
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
    reset_game()

def reset_game():
    canvas = Canvas(INITIAL_NUM_ALIVE_ROBOTS, INITIAL_NUM_DEAD_ROBOTS, INITIAL_NUM_TELEPORTS)
    while not GAME_OVER:
        pass

def player_wins():
    print(STRINGS_DICTIONARY.you_won)
    game_over()

def player_lost():
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
