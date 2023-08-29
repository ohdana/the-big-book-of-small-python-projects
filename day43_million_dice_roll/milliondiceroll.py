import random

YES, NO = 'Y', 'N'
MIN_DIE_VALUE, MAX_DIE_VALUE = 1, 6
MIN_N_OF_DICE, MAX_N_OF_DICE = 1, 10
N_OF_ROLLS = 1000000

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        simulate()
        play_again = ask_if_play_again()

    say_bye()

def simulate():
    n_of_dice = get_n_of_dice()
    roll_results = get_roll_results(n_of_dice)
    show_roll_results(roll_results)

def show_roll_results(roll_results):
    print(STRINGS_DICTIONARY.results_headers)
    sorted_keys = sorted(roll_results.keys())
    for key in sorted_keys:
        print('{} - {} rolls - {}%'.format(key, roll_results[key], round(100 * roll_results[key] / N_OF_ROLLS, 1)))

def get_roll_results(n_of_dice):
    print(STRINGS_DICTIONARY.simulating_started.format(N_OF_ROLLS, n_of_dice))
    n_of_milestones = 15
    random_milestones = random.choices(range(N_OF_ROLLS), k=n_of_milestones)
    results = {}
    for i in range(N_OF_ROLLS):
        if i in random_milestones:
            print('{}% done...'.format(round(100 * i / N_OF_ROLLS, 1)))
        roll_result = roll_dice(n_of_dice)
        if not roll_result in results:
            results[roll_result] = 1
        else:
            results[roll_result] += 1
    return results

def roll_dice(n_of_dice):
    return sum([roll_die() for i in range(n_of_dice)])

def roll_die():
    return random.randint(MIN_DIE_VALUE, MAX_DIE_VALUE)

def get_n_of_dice():
    user_input = input(STRINGS_DICTIONARY.enter_n_of_dice)

    if not is_valid_n_of_dice(user_input):
        return get_n_of_dice()

    return int(user_input)

def is_valid_n_of_dice(user_input):
    if not user_input.isdigit():
        return False

    return MIN_N_OF_DICE <= int(user_input) <= MAX_N_OF_DICE

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
    Million Dice Roll Statistics Simulator

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A simulation of one million dice rolls.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.enter_n_of_dice = '''
    Enter how many six-sided dice you want to roll: '''
    STRINGS_DICTIONARY.simulating_started = '''
    Simulating {} rolls of {} dice...'''
    STRINGS_DICTIONARY.results_headers = '''
    TOTAL - ROLLS - PERCENTAGE'''

class StringsDictionary:
    pass

main()
