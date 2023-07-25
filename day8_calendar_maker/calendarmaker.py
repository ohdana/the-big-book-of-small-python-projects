from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

MIN_YEAR = 1
MAX_YEAR = 9999
MIN_MONTH = 1
MAX_MONTH = 12
FIRST_DAY_OF_WEEK = 0
LAST_DAY_OF_WEEK = 6

def main():
    init()
    year = get_year_input()
    month = get_month_input()
    file_name = STRINGS_DICTIONARY.file_name.format(year, month)
    generate_calendar(year, month)

def save_calendar_to_file(file_name):
    print(STRINGS_DICTIONARY.saved_to.format(filename))

def generate_calendar(year, month):
    first_day_of_month = date(year, month, 1)
    last_day_of_month = first_day_of_month + relativedelta(months=+1) - timedelta(days=1)

    first_day_of_calendar = first_day_of_month
    while first_day_of_calendar.weekday() != FIRST_DAY_OF_WEEK:
        first_day_of_calendar -= timedelta(days=1)

    last_day_of_calendar = last_day_of_month
    while last_day_of_calendar.weekday() != LAST_DAY_OF_WEEK:
        last_day_of_calendar += timedelta(days=1)
    cursor = first_day_of_calendar

    data_to_format_calendar = [first_day_of_month.strftime("%B"), year]
    while cursor <= last_day_of_calendar:
        day_str = str(cursor.day)
        if len(day_str) == 1:
            day_str = '0' + day_str
        data_to_format_calendar.append(day_str)
        cursor += timedelta(days=1)
    print(STRINGS_DICTIONARY.calendar_pattern.format(*data_to_format_calendar))

def get_year_input():
    year = input(STRINGS_DICTIONARY.enter_the_year)

    while not is_valid_year_input(year):
        year = input(STRINGS_DICTIONARY.invalid_year)

    return int(year)

def get_month_input():
    month = input(STRINGS_DICTIONARY.enter_the_month)

    while not is_valid_month_input(month):
        month = input(STRINGS_DICTIONARY.invalid_month)

    return int(month)

def is_valid_year_input(year):
    if not year.isdigit():
        return False

    return MIN_YEAR <= int(year) <= MAX_YEAR

def is_valid_month_input(month):
    if not month.isdigit():
        return False

    return MIN_MONTH <= int(month) <= MAX_MONTH

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Calendar Maker

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana
    Create monthly calendars, saved to a text file and fit for printing.'''
    STRINGS_DICTIONARY.enter_the_year = '''
    Enter the year for the calendar: '''
    STRINGS_DICTIONARY.invalid_year = '''
    Invalid input. Please use only digits: '''
    STRINGS_DICTIONARY.enter_the_month = '''
    Enter the month for the calendar, 1-12: '''
    STRINGS_DICTIONARY.invalid_month = '''
    Invalid input. Please use only numbers from 1 to 12: '''
    STRINGS_DICTIONARY.saved_to = '''
    Saved to {} '''
    STRINGS_DICTIONARY.file_name = 'calendar_{}_{}.txt'
    STRINGS_DICTIONARY.calendar_pattern = '''
                                         {} {}
    ...Monday....Tuesday...Wednesday...Thursday....Friday....Saturday....Sunday...
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    |{}        |{}        |{}        |{}        |{}        |{}        |{}        |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    |          |          |          |          |          |          |          |
    +----------+----------+----------+----------+----------+----------+----------+
    '''

class StringsDictionary:
    pass

main()
