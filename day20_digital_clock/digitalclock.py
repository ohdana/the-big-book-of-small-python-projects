import time
import sevseg
from datetime import datetime
CLOCK_HEIGHT = 0

def main():
    init()
    show_intro_message()
    while True:
        clear_screen()
        show_time(datetime.now())
        time.sleep(1)

def show_time(time):
    hours, minutes, seconds = get_h_m_s_clock_digits(time)
    clock = get_clock(hours, minutes, seconds)
    print(clock)

def get_h_m_s_clock_digits(time):
    hours = get_clock_digit(time.hour)
    minutes = get_clock_digit(time.minute)
    seconds = get_clock_digit(time.second)

    return hours, minutes, seconds

def get_clock_digit(digit):
    if 0 <= digit <= 9:
        return '0{}'.format(digit)

    return str(digit)

def get_clock(hours, minutes, seconds):
    result = ''
    hours_sevseg_lines = sevseg.get_two_digit_number(hours).split('\n')
    minutes_sevseg_lines = sevseg.get_two_digit_number(minutes).split('\n')
    seconds_sevseg_lines = sevseg.get_two_digit_number(seconds).split('\n')
    separator_sevseg_lines = STRINGS_DICTIONARY.hour_min_sec_separator.split('\n')

    for i in range(CLOCK_HEIGHT):
        result += hours_sevseg_lines[i]
        result += separator_sevseg_lines[i]
        result += minutes_sevseg_lines[i]
        result += separator_sevseg_lines[i]
        result += seconds_sevseg_lines[i]
        result += '\n'

    return result

def clear_screen():
    print('\n' * 30)

def set_clock_height():
    global CLOCK_HEIGHT
    sevseg_number_lines = sevseg.get_digit('0').split('\n')
    CLOCK_HEIGHT = len(sevseg_number_lines)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
    set_clock_height()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Digital CLock

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Displays a digital clock of the current time with a seven-segment
    display.'''

    STRINGS_DICTIONARY.hour_min_sec_separator = '''
     .
     *
     *
    '''

class StringsDictionary:
    pass

main()
