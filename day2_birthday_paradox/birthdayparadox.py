from datetime import date, timedelta
from random import choices

MAX_BDAYS = 100
N_OF_SIMULATIONS = 1000
N_OF_BIRTHDAYS = 0
N_OF_POSITIVE_CASES = 0
CALENDAR = []

def main():
    init()
    show_intro_message()
    set_n_of_bdays()
    show_example()
    show_simulation_progress()
    show_simulation_result()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def set_n_of_bdays():
    global N_OF_BIRTHDAYS
    N_OF_BIRTHDAYS = int(get_n_of_birthdays())

def show_example():
    birthdays = generate_birthdays(N_OF_BIRTHDAYS)
    print(STRINGS_DICTIONARY.show_bdays_message)
    print(birthdays)
    matches = get_bday_matches(birthdays)
    matches_string = ', '.join(matches)
    print(STRINGS_DICTIONARY.multiple_bdays_message.format(matches_string))

def show_simulation_progress():
    print(STRINGS_DICTIONARY.generate_bdays_message)
    input(STRINGS_DICTIONARY.press_enter)
    run_simulations()

def show_simulation_result():
    print(STRINGS_DICTIONARY.result_message)

def run_simulations():
    global N_OF_POSITIVE_CASES
    n_of_positive_cases = 0
    for i in range(N_OF_SIMULATIONS+1):
        print(STRINGS_DICTIONARY.n_simulations_run_message.format(i))
        birthdays = generate_birthdays(N_OF_BIRTHDAYS)
        matches = get_bday_matches(birthdays)
        if not matches:
            continue
        n_of_positive_cases += 1
    N_OF_POSITIVE_CASES = n_of_positive_cases

def get_bday_matches(birthdays):
    return set([x for x in birthdays if birthdays.count(x) > 1])

def is_valid_n_of_bdays(user_input):
    if not user_input.isdigit():
        return False

    return 1 <= int(user_input) <= MAX_BDAYS

def get_n_of_birthdays():
    n_of_birthdays = input(STRINGS_DICTIONARY.how_many_bdays_question)

    while not is_valid_n_of_bdays(n_of_birthdays):
        n_of_birthdays = input(STRINGS_DICTIONARY.invalid_n_of_bdays)

    return n_of_birthdays

def generate_birthdays(n):
    return choices(CALENDAR, k=n)

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
    Here are {} birthdays:'''.format(N_OF_BIRTHDAYS)
    STRINGS_DICTIONARY.invalid_n_of_bdays = '''
    Please enter a number between 1 and {}'''.format(MAX_BDAYS)

    STRINGS_DICTIONARY.multiple_bdays_message = '''
    In this simulation multiple people have their birthday on {}'''

    STRINGS_DICTIONARY.generate_bdays_message = '''
    Generating {} random birthdays {} times...
    '''.format(N_OF_BIRTHDAYS, N_OF_SIMULATIONS)

    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''

    STRINGS_DICTIONARY.n_simulations_run_message = '''
    {} simulations run...'''
    STRINGS_DICTIONARY.result_message = '''
    Out of {} simulations of {} people, there was a
    matching birthday in that group {} times. This means
    that {} people have a {}% chance of
    having a matching birthday in their group.
    That's probably more than you would think!
    '''.format(N_OF_SIMULATIONS, N_OF_BIRTHDAYS, N_OF_POSITIVE_CASES, N_OF_BIRTHDAYS, N_OF_POSITIVE_CASES * 100 / N_OF_SIMULATIONS)

class StringsDictionary:
    pass

main()
