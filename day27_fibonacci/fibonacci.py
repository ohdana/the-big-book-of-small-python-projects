GAME_OVER = False
FIBONACCI_CACHE = [0, 1]

def main():
    init()
    show_intro_message()
    play()

def play():
    while True:
        n = get_user_input()
        if GAME_OVER:
            break

        calculate_fibonacci(n)
        show_result(n)

def calculate_fibonacci(n):
    cached_result = get_cached_result(n)

    if not cached_result:
        populate_cache(n)
        return calculate_fibonacci(n)

    return cached_result

def populate_cache(n):
    max_calculated_n = len(FIBONACCI_CACHE) - 1

    for i in range(n - max_calculated_n):
        FIBONACCI_CACHE.append(FIBONACCI_CACHE[-1] + FIBONACCI_CACHE[-2])

def get_cached_result(n):
    if n >= len(FIBONACCI_CACHE):
        return None

    return FIBONACCI_CACHE[n]

def get_user_input():
    global GAME_OVER
    user_input = input(STRINGS_DICTIONARY.user_input)

    if user_input.upper() == 'QUIT':
        GAME_OVER = True
        say_bye()
        return

    if not is_valid_number(user_input):
        return get_user_input()

    return int(user_input)

def is_valid_number(user_input):
    if not user_input:
        print('1')
        return False

    if not user_input.isdigit():
        print('2')
        return False

    if int(user_input) < 0:
        print('3')
        return False

    return True

def show_result(n):
    print(str(FIBONACCI_CACHE[n]))
    print(', '.join([str(i) for i in FIBONACCI_CACHE[:n+1]]))

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
    Fibonacci Sequence

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Calculates numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5... '''
    STRINGS_DICTIONARY.user_input = '''
    Enter the Nth Fibonacci number you wish to calculate (such as 1, 5, 50, 1000 or 9999), or QUIT to quit: '''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''

class StringsDictionary:
    pass

main()
