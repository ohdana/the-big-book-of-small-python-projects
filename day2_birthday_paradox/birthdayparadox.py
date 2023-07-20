from datetime import date, timedelta
from random import choices

MAX_BDAYS = 100
N_OF_SIMULATIONS = 1000
CALENDAR = []

def main():
    init()
    show_intro_message()
    n_of_bdays = get_n_of_bdays()
    show_simulation_example(n_of_bdays)
    run_all_simulations(n_of_bdays)

def show_simulation_example(n_of_bdays):
    matches = []

    while not matches:
        random_bdays = generate_bdays(n_of_bdays)
        matches = get_bday_matches(random_bdays)

    print(STRINGS_DICTIONARY.show_bdays_message.format(n_of_bdays))
    print(random_bdays)

    matches_string = ', '.join(matches)
    print(STRINGS_DICTIONARY.multiple_bdays_message.format(matches_string))

def run_all_simulations(n_of_bdays):
    show_simulation_progress(n_of_bdays)

    n_of_positive_outcomes = 0
    for i in range(N_OF_SIMULATIONS + 1):
        print(STRINGS_DICTIONARY.n_simulations_run_message.format(i))
        random_bdays = generate_bdays(n_of_bdays)
        matches = get_bday_matches(random_bdays)
        if not matches:
            continue
        n_of_positive_outcomes += 1

    show_simulation_result(n_of_bdays, n_of_positive_outcomes)

def show_simulation_progress(n_of_bdays):
    print(STRINGS_DICTIONARY.generate_bdays_message.format(n_of_bdays, N_OF_SIMULATIONS))
    input(STRINGS_DICTIONARY.press_enter)

def show_simulation_result(n_of_bdays, n_of_positive_outcomes):
    percent_of_positive_outcomes = n_of_positive_outcomes * 100 / N_OF_SIMULATIONS
    print(STRINGS_DICTIONARY.result_message.format(a=N_OF_SIMULATIONS, b=n_of_bdays, c=n_of_positive_outcomes, d=percent_of_positive_outcomes))

def get_n_of_bdays():
    n_of_bdays = input(STRINGS_DICTIONARY.how_many_bdays_question)

    while not is_valid_n_of_bdays(n_of_bdays):
        n_of_bdays = input(STRINGS_DICTIONARY.invalid_n_of_bdays)

    return int(n_of_bdays)

def get_bday_matches(bdays):
    return set([day for day in bdays if bdays.count(day) > 1])

def generate_bdays(n):
    return choices(CALENDAR, k=n)

def is_valid_n_of_bdays(user_input):
    if not user_input.isdigit():
        return False

    return 1 <= int(user_input) <= MAX_BDAYS

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
    init_calendar()

def init_calendar():
    global CALENDAR
    start_date, end_date = date(2023, 1, 1), date(2024, 1, 1)
    pointer = start_date

    while pointer != end_date:
        month_day = pointer.strftime("%b %d")
        CALENDAR.append(month_day)

        pointer += timedelta(days=1)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Birthday Paradox

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.

    (It's not actually a paradox, it's just a surprising result.)'''

    STRINGS_DICTIONARY.how_many_bdays_question = '''
    How many birthdays shall I generate? (Max {}): '''.format(MAX_BDAYS)
    STRINGS_DICTIONARY.show_bdays_message = '''
    Here are {} birthdays:'''
    STRINGS_DICTIONARY.invalid_n_of_bdays = '''
    Please enter a number between 1 and {}'''.format(MAX_BDAYS)

    STRINGS_DICTIONARY.multiple_bdays_message = '''
    In this simulation multiple people have their birthday on {}'''

    STRINGS_DICTIONARY.generate_bdays_message = '''
    Generating {} random birthdays {} times...'''

    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''

    STRINGS_DICTIONARY.n_simulations_run_message = '''
    {} simulations run...'''
    STRINGS_DICTIONARY.result_message = '''
    Out of {a} simulations of {b} people, there was a
    matching birthday in that group {c} times. This means
    that {b} people have a {d}% chance of
    having a matching birthday in their group.
    That's probably more than you would think!'''

class StringsDictionary:
    pass

main()
