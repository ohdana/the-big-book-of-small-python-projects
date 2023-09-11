import time, random

ROCK, PAPER, SCISSORS = 'ROCK', 'PAPER', 'SCISSORS'
QUIT = 'QUIT'
WIN, LOSS, TIE = 'WIN', 'LOSS', 'TIE'
STATS = None
USER_MOVES_MAP = None
COUNTDOWN_PAUSE = 0.5

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    while True:
        show_stats()
        user_input = get_user_input()
        if user_input is QUIT:
            break
        bot_move = get_bot_move()
        show_round_results(user_input, bot_move)

def show_round_results(user_move, bot_move):
    print(STRINGS_DICTIONARY.versus.format(user_move))
    for i in STRINGS_DICTIONARY.countdown:
        print(i)
        time.sleep(COUNTDOWN_PAUSE)
    print(STRINGS_DICTIONARY.bot_move.format(bot_move))
    round_result = get_round_result(user_move, bot_move)
    if round_result is WIN:
        print(STRINGS_DICTIONARY.you_won)
    elif round_result is LOSS:
        print(STRINGS_DICTIONARY.you_lost)
    else:
        print(STRINGS_DICTIONARY.tie)
    update_stats(round_result)

def get_round_result(user_move, bot_move):
    if user_move == bot_move:
        return TIE

    if user_move is ROCK and bot_move is SCISSORS:
        return WIN

    if user_move is PAPER and bot_move is ROCK:
        return WIN

    if user_move is SCISSORS and bot_move is PAPER:
        return WIN

    return LOSS

def update_stats(round_result):
    STATS[round_result] += 1

def show_stats():
    print(STRINGS_DICTIONARY.stats.format(STATS[WIN], STATS[LOSS], STATS[TIE]))

def get_user_input():
    print(STRINGS_DICTIONARY.enter_your_move)
    user_input = input(STRINGS_DICTIONARY.input).upper()
    if not is_valid_user_input(user_input):
        return get_user_input()

    return USER_MOVES_MAP[user_input]

def is_valid_user_input(user_input):
    return user_input in USER_MOVES_MAP.keys()

def get_bot_move():
    return random.choice([ROCK, PAPER, SCISSORS])

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init_stats():
    global STATS
    STATS = { WIN: 0, LOSS: 0, TIE: 0 }

def init_user_moves_map():
    global USER_MOVES_MAP
    USER_MOVES_MAP = { 'R': ROCK, 'P': PAPER, 'S': SCISSORS, 'Q': QUIT }

def init():
    init_strings_dictionary()
    init_stats()
    init_user_moves_map()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Rock, Paper, Scissors

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    - Rock beats scissors.
    - Paper beats rocks.
    - Scissors beats paper.'''
    STRINGS_DICTIONARY.versus = '''
    {} versus...'''
    STRINGS_DICTIONARY.bot_move = '''
    {}'''
    STRINGS_DICTIONARY.countdown = ['''
    1...''', '''
    2...''', '''
    3...''']
    STRINGS_DICTIONARY.you_won = '''
    You won!'''
    STRINGS_DICTIONARY.you_lost = '''
    You lost!'''
    STRINGS_DICTIONARY.tie = '''
    Tie!'''
    STRINGS_DICTIONARY.stats = '''
    {} Wins, {} Losses, {} Ties'''
    STRINGS_DICTIONARY.enter_your_move = '''
    Enter your move: (R)ock (P)aper (S)cissors or (Q)uit'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''

class StringsDictionary:
    pass

main()
