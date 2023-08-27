from cup import Cup
from die import Die

import random

YES, NO = 'Y', 'N'
STAR_FACE = ['+-----------+',
            '|     .     |',
            '|    ,O,    |',
            '| \'ooOOOoo\' |',
            '|   `OOO`   |',
            '|   O' 'O   |',
            '+-----------+']
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
GOLD, SILVER, BRONZE = 'GOLD', 'SILVER', 'BRONZE'
STAR, SKULL, QUESTION = 'STAR', 'SKULL', 'QUESTION'
SIDE_TYPE_MAP = { STAR: STAR_FACE, SKULL: SKULL_FACE, QUESTION: QUESTION_FACE }
CUP_CONFIGURATION = { GOLD: 6, SILVER: 4, BRONZE: 3 }
GET_DIE_MAP = None
DIE_WIDTH = 13
DIE_HEIGHT = 7
GAME_OVER = None
MAX_PLAYERS = 6
MIN_PLAYERS = 2

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    cup = init_cup()
    reset_game()
    players = get_players()
    player_names = [name for name in players.keys()]
    start_game()
    turn = 0
    while not GAME_OVER:
        if is_last_round(players):
            do_last_round(players)
            break
        player = player_names[turn]
        take_turn(player)
        turn = (turn + 1) % len(player_names)
    calculate_final_results(player)

def calculate_final_results():
    pass

def is_last_round(players):
    pass

def get_score(player_dice):
    pass
    game_over()

def start_game():
    pass

def take_turn(player):
    pass

def do_last_round(players):
    for player in players:
        take_turn(player)

def get_players():
    n_of_players = get_n_of_players()
    players = {}
    for i in range(n_of_players):
        player_name = get_player_name(i + 1)
        players[player_name] = 0
    return players

def get_player_name(n):
    print(STRINGS_DICTIONARY.whats_players_name.format(n))
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_player_name(n)

def get_n_of_players():
    user_input = input(STRINGS_DICTIONARY.how_many_players)
    if not is_valid_n_of_players_input(user_input):
        return get_n_of_players()
    return int(user_input)

def is_valid_n_of_players_input(user_input):
    if not user_input:
        return False

    if not user_input.isdigit():
        return False

    return MIN_PLAYERS <= int(user_input) <= MAX_PLAYERS

def reset_game():
    set_game_over(False)

def game_over():
    set_game_over(True)

def set_game_over(value):
    global GAME_OVER
    GAME_OVER = value

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init_cup():
    dice = get_dice()
    return Cup(dice)

def get_dice():
    dice = []
    for die_type in CUP_CONFIGURATION:
        n_of_dice = CUP_CONFIGURATION[die_type]
        for i in range(n_of_dice):
            dice.append(GET_DIE_MAP[die_type]())
    return dice

def get_gold_die():
    die_sides = { STAR: 3, SKULL: 1, QUESTION: 2 }
    return Die(die_sides, SIDE_TYPE_MAP, GOLD)

def get_silver_die():
    die_sides = { STAR: 2, SKULL: 2, QUESTION: 2 }
    return Die(die_sides, SIDE_TYPE_MAP, SILVER)

def get_bronze_die():
    die_sides = { STAR: 1, SKULL: 3, QUESTION: 2 }
    return Die(die_sides, SIDE_TYPE_MAP, BRONZE)

def init_get_die_map():
    global GET_DIE_MAP
    GET_DIE_MAP = {}
    GET_DIE_MAP[GOLD] = get_gold_die
    GET_DIE_MAP[SILVER] = get_silver_die
    GET_DIE_MAP[BRONZE] = get_bronze_die

def init():
    init_strings_dictionary()
    init_get_die_map()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Lucky Start

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A "press your luck" game where you roll dice to gather as many stars
    as possible. You can roll as many times as you want, but if you roll
    three skulls you lose all your stars.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.roll_again = '''
    Do you want to roll again? y/n: '''
    STRINGS_DICTIONARY.stars_collected = 'Stars collected: '
    STRINGS_DICTIONARY.skulls_collected = 'Skulls collected: '
    STRINGS_DICTIONARY.turn_of: '''
    It is {}'s turn.'''
    STRINGS_DICTIONARY.scores = '''
    SCORES: {}'''
    STRINGS_DICTIONARY.input = '''
    >'''
    STRINGS_DICTIONARY.how_many_players = '''
    How many players are there? Please enter number more than 1: '''
    STRINGS_DICTIONARY.whats_players_name = '''
    What is player #{}'s name?'''
    STRINGS_DICTIONARY.not_enough_dice = '''
    There aren\'t enough dice left in the cup to continue {}'s turn.'''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to continue...'''
    STRINGS_DICTIONARY.lost_stars = '''
    3 or more skulls means you've lost your stars!'''
    STRINGS_DICTIONARY.reached_13 = '''
    has reached 13 points!!!'''
    STRINGS_DICTIONARY.one_more_turn = '''
    Everyone else will get one more turn!'''
    STRINGS_DICTIONARY.game_ended = '''
    The game has ended...'''
    STRINGS_DICTIONARY.winner = '''
    The winner is {}.'''
    STRINGS_DICTIONARY.winners = '''
    The winners are {}.'''

class StringsDictionary:
    pass

main()
