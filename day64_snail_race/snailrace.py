import time
from snail import Snail
from race import Race

MIN_N_OF_SNAILS = 2
MAX_N_OF_SNAILS = 8
DISTANCE = 20

def main():
    init()
    show_intro_message()
    play()

def play():
    snails = get_snails()
    race(snails)

def race(snails):
    new_race = Race(snails, DISTANCE)
    new_race.run()
    winners = new_race.get_winners()
    show_results(winners)

def show_results(winners):
    if len(winners) == 1:
        print(STRINGS_DICTIONARY.winner.format(winners[0]))
    else:
        winners_str = ', '.join(winners)
        print(STRINGS_DICTIONARY.winners.format(winners_str))

def get_snails():
    n_of_snails = get_n_of_snails()
    return [get_snail(i) for i in range(1, n_of_snails + 1)]

def get_snail(n):
    name = get_snail_name(n)
    return Snail(name)

def get_snail_name(n):
    print(STRINGS_DICTIONARY.enter_snail_name.format(n))
    user_input = input(STRINGS_DICTIONARY.input)
    if not user_input:
        return get_snail_name(n)

    return user_input

def get_n_of_snails():
    print(STRINGS_DICTIONARY.enter_n_of_snails)
    user_input = input(STRINGS_DICTIONARY.input)
    while not is_valid_n_of_snails(user_input):
        return get_n_of_snails()

    return int(user_input)

def is_valid_n_of_snails(user_input):
    if not user_input.isdigit():
        return False

    return MIN_N_OF_SNAILS <= int(user_input) <= MAX_N_OF_SNAILS

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).upper()
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
    Snail Race

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    @v <-- snail'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.enter_n_of_snails = '''
    How many snails will race? Max: {}'''.format(MAX_N_OF_SNAILS)
    STRINGS_DICTIONARY.enter_snail_name = '''
    Enter snail #{}'s name:'''
    STRINGS_DICTIONARY.winner = '''
    {} wins the race! Congratulations!'''
    STRINGS_DICTIONARY.winners = '''
    {} win the race! Congratulations!'''


class StringsDictionary:
    pass

main()
