from gameengine import GameEngine
import random

YES, NO = 'Y', 'N'
MIN_PLAYERS = 2
MAX_PLAYERS = 6

def main():
    init()
    show_intro_message()
    play_again = True
    game_engine = GameEngine()
    while play_again:
        play(game_engine)
        play_again = ask_if_play_again()

    say_bye()

def play(game):
    players = get_players()
    game.start_new_game(players)
    game.play()
    show_final_results(game)

def show_final_results(game):
    print(STRINGS_DICTIONARY.game_ended)
    show_scores(game)
    winners = game.get_winners()
    if len(winners) > 1:
        winners_str = ', '.join(winners)
        print(STRINGS_DICTIONARY.winners.format(winners_str))
    else:
        print(STRINGS_DICTIONARY.winner.format(winners[0]))

def show_scores(game):
    scores = game.get_scores()
    scores_str = ''
    for player in scores.keys():
        scores_str += '{}: {}'.format(player, scores[player])
    print(STRINGS_DICTIONARY.scores.format(scores_str))

def get_players():
    n_of_players = get_n_of_players()
    return [get_player_name(i + 1) for i in range(n_of_players)]

def get_player_name(n):
    print(STRINGS_DICTIONARY.whats_players_name.format(n))
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_player_name(n)

    return user_input

def get_n_of_players():
    user_input = input(STRINGS_DICTIONARY.how_many_players)
    if not is_valid_n_of_players_input(user_input):
        return get_n_of_players()

    return int(user_input)

def is_valid_n_of_players_input(user_input):
    if not user_input.isdigit():
        return False

    return MIN_PLAYERS <= int(user_input) <= MAX_PLAYERS

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

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Lucky Stars

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A "press your luck" game where you roll dice with Stars, Skulls, and
    Question Marks.

    On your turn, you pull three random dice from the dice cup and roll
    them. You can roll Stars, Skulls, and Question Marks. You can end your
    turn and get one point per Star. If you choose to roll again, you keep
    the Question Marks and pull new dice to replace the Stars and Skulls.
    If you collect three Skulls, you lose all your Stars and end your turn.

    When a player gets 13 points, everyone else gets one more turn before
    the game ends. Whoever has the most points wins.

    There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
    Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
    even.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.roll_again = '''
    Do you want to roll again? y/n: '''
    STRINGS_DICTIONARY.stars_collected = 'Stars collected: '
    STRINGS_DICTIONARY.skulls_collected = 'Skulls collected: '
    STRINGS_DICTIONARY.scores = '''
    SCORES:
    {}'''
    STRINGS_DICTIONARY.input = '''
    >'''
    STRINGS_DICTIONARY.how_many_players = '''
    How many players are there? Please enter number more than 1: '''
    STRINGS_DICTIONARY.whats_players_name = '''
    What is player #{}'s name?'''
    STRINGS_DICTIONARY.game_ended = '''
    The game has ended...'''
    STRINGS_DICTIONARY.winner = '''
    The winner is {}.'''
    STRINGS_DICTIONARY.winners = '''
    The winners are {}.'''

class StringsDictionary:
    pass

main()
