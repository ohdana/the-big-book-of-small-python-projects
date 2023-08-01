import sevseg, time

CLOCK_HEIGHT = 0
START_COUNTDOWN_SECONDS = 2
START_COUNTDOWN_MINUTES = 2

def main():
    init()
    show_intro_message()
    show_countdown(START_COUNTDOWN_MINUTES, START_COUNTDOWN_SECONDS)

def show_countdown(minutes, seconds):
    while minutes > 0 or seconds >= 0:
        print('\n'*20)
        show_clock(minutes, seconds)
        minutes, seconds = subtract_one_second(minutes, seconds)
        time.sleep(1)

def subtract_one_second(minutes, seconds):
    if seconds > 0:
        return (minutes, seconds - 1)

    if minutes > 0:
        return (minutes - 1, 59)

    return (0, -1)

def show_clock(minutes, seconds):
    min_str = str(minutes)
    sec_str = str(seconds)
    if 0 <= minutes <= 9:
        min_str = '0' + min_str
    if 0 <= seconds <= 9:
        sec_str = '0' + sec_str
    result = ''
    minutes_sevseg_lines = sevseg.get_two_digit_number(min_str).split('\n')
    seconds_sevseg_lines = sevseg.get_two_digit_number(sec_str).split('\n')
    separator_sevseg_lines = STRINGS_DICTIONARY.min_sec_separator.split('\n')
    for i in range(CLOCK_HEIGHT):
        result += minutes_sevseg_lines[i]
        result += separator_sevseg_lines[i]
        result += seconds_sevseg_lines[i]
        result += '\n'

    print(result)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def set_clock_height():
    global CLOCK_HEIGHT
    sevseg_number_lines = sevseg.get_digit('0').split('\n')
    CLOCK_HEIGHT = len(sevseg_number_lines)

def init():
    init_strings_dictionary()
    set_clock_height()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Countdown

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Show a countdown timer animation using a seven-segment display.'''

    STRINGS_DICTIONARY.min_sec_separator = '''
     .
     *
     *
    '''

class StringsDictionary:
    pass

main()
