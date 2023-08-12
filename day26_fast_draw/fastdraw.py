import random, time

MIN_SNOOZE_DURATION = 2
MAX_SNOOZE_DURATION = 7
MAX_TIME_TO_WIN_SECONDS = 0.3
FALSE_START_THRESHOLD_SECONDS = 0.01

def main():
    init()
    show_intro_message()
    play()

def play():
    input()
    while True:
        play_round()
        user_input = input(STRINGS_DICTIONARY.offer_play)
        if user_input.upper() == 'QUIT':
            say_bye()
            break

def play_round():
    snooze_duration = random.randint(MIN_SNOOZE_DURATION, MAX_SNOOZE_DURATION)
    print(STRINGS_DICTIONARY.its_high_noon)
    time.sleep(snooze_duration)
    print(STRINGS_DICTIONARY.draw)
    stopwatch_start = time.time()
    input()
    stopwatch_end = time.time()
    time_taken = stopwatch_end - stopwatch_start
    show_results(time_taken)

def show_results(time_taken):
    print(get_game_result(time_taken))

def get_game_result(time_taken):
    if time_taken <= FALSE_START_THRESHOLD_SECONDS:
        return STRINGS_DICTIONARY.false_start
    elif time_taken > MAX_TIME_TO_WIN_SECONDS:
        return STRINGS_DICTIONARY.your_result.format(time_taken) + ' ' + STRINGS_DICTIONARY.too_slow

    return STRINGS_DICTIONARY.your_result.format(time_taken) + ' ' +  STRINGS_DICTIONARY.perfect

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
    Fast Draw

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Time to test your reflexes and see if you are the fastest
    draw in the west!
    When you see DRAW, you have {} seconds to press Enter.
    But you lose if you press Enter before DRAW appears.

    Press Enter to begin...'''.format(MAX_TIME_TO_WIN_SECONDS)
    STRINGS_DICTIONARY.its_high_noon = '''
    It is high noon...'''
    STRINGS_DICTIONARY.draw = '''
    DRAW!'''
    STRINGS_DICTIONARY.your_result = '''
    You took {} to draw.'''
    STRINGS_DICTIONARY.too_slow = 'Too slow!'
    STRINGS_DICTIONARY.false_start = 'Oi oi. That was a false start! Naughty naughty.'
    STRINGS_DICTIONARY.perfect = 'Perfect!'
    STRINGS_DICTIONARY.offer_play = '''
    Enter QUIT to stop, or press Enter to play again: '''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''

class StringsDictionary:
    pass

main()
