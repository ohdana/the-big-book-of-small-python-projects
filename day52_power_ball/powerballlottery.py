from powerballengine import PowerBallEngine
from powerballplayer import PowerBallPlayer

MAX_N_OF_ITERATIONS = 1000000
MIN_POWERBALL_N = 1
MAX_POWERBALL_N = 26
MIN_BALL_N = 1
MAX_BALL_N = 69
N_OF_REGULAR_BALLS = 5
LOTTERY_TICKET_PRICE = 2

def main():
    init()
    show_intro_message()
    simulate()
    show_bye_message()

def simulate():
    engine = get_powerball_engine()
    player, players_numbers = get_player()
    n_of_iterations = get_n_of_iterations()
    start_game(n_of_iterations)
    is_win = False
    while not is_simulation_over(n_of_iterations, player.get_tickets_used(), is_win):
        player.buy_ticket()
        winning_numbers = engine.generate_numbers()
        is_win = is_exact_match(winning_numbers, players_numbers)
        show_results(is_win, winning_numbers)

    if not is_win:
        show_wasted_total(player.get_tickets_used())

def is_simulation_over(n_of_iterations, current_iteration, is_win):
    return is_win or current_iteration == n_of_iterations

def show_wasted_total(n_of_tickets):
    total_money_spent = n_of_tickets * LOTTERY_TICKET_PRICE
    print(STRINGS_DICTIONARY.you_wasted.format(total_money_spent))

def start_game(n_of_iterations):
    show_total_estimated_price(n_of_iterations)
    input(STRINGS_DICTIONARY.press_enter)

def show_total_estimated_price(n_of_iterations):
    total_price = n_of_iterations * LOTTERY_TICKET_PRICE
    print(STRINGS_DICTIONARY.cost_of_play.format(total_price, n_of_iterations))

def show_results(is_win, winning_numbers):
    winning_numbers_str = get_formatted_winning_numbers(winning_numbers)
    if is_win:
        print(STRINGS_DICTIONARY.winning_numbers.format(winning_numbers_str))
        print(STRINGS_DICTIONARY.you_won)
    else:
        print(STRINGS_DICTIONARY.winning_numbers.format(winning_numbers_str) + '. ' + STRINGS_DICTIONARY.you_lost)

def get_formatted_winning_numbers(numbers):
    regular_numbers, powerball_number = numbers
    regular_numbers_str = ' '.join([str(number) for number in regular_numbers])
    return regular_numbers_str + ' and ' + str(powerball_number)

def is_exact_match(winning_numbers, players_numbers):
    return winning_numbers == players_numbers

def get_player_numbers():
    regular_numbers = get_player_regular_numbers()
    powerball_number = get_player_powerball_number()

    return regular_numbers, powerball_number

def get_player_powerball_number():
    input_message = STRINGS_DICTIONARY.enter_powerball
    min_bound, max_bound = MIN_POWERBALL_N, MAX_POWERBALL_N

    return get_number_user_input(input_message, min_bound, max_bound)

def get_player_regular_numbers():
    input_message = STRINGS_DICTIONARY.enter_numbers
    n_of_numbers, min_bound, max_bound = N_OF_REGULAR_BALLS, MIN_BALL_N, MAX_BALL_N
    numbers = get_numbers_user_input(input_message, n_of_numbers, min_bound, max_bound)

    return numbers

def get_n_of_iterations():
    input_message = STRINGS_DICTIONARY.enter_n_of_iterations
    min_bound, max_bound = 1, MAX_N_OF_ITERATIONS

    return get_number_user_input(input_message, min_bound, max_bound)

def get_number_user_input(input_message, min_bound, max_bound):
    return get_numbers_user_input(input_message, 1, min_bound, max_bound)[0]

def get_numbers_user_input(input_message, n_of_numbers, min_bound, max_bound):
    print(input_message)
    user_input = input(STRINGS_DICTIONARY.input)
    is_valid_input, parsed_numbers = try_parse_numbers(user_input, n_of_numbers, min_bound, max_bound)

    if not is_valid_input:
        return get_numbers_user_input(input_message, n_of_numbers, min_bound, max_bound)

    return sorted(parsed_numbers)

def try_parse_numbers(string, n_of_numbers, min_bound, max_bound):
    string = string.strip()
    if not string:
        return False, None

    strings = string.split(' ')
    if len(strings) != n_of_numbers:
        return False, None

    all_are_numbers = lambda raw_list: all([element.isdigit() for element in raw_list])
    if not all_are_numbers(strings):
        return False, None

    numbers = [int(x)for x in strings]
    all_are_within_bounds = lambda numbers: all([min_bound <= number <= max_bound for number in numbers])
    if not all_are_within_bounds(numbers):
        return False, None

    return True, numbers

def get_player():
    player_numbers = get_player_numbers()
    return PowerBallPlayer(*player_numbers), player_numbers

def get_powerball_engine():
    return PowerBallEngine()

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Powerball Lottery

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Each powerball lottery ticket costs $2. The jackpot for this game
    is $1.586 billion! It doesn't matter what the jackpot is, though,
    because the odds are 1 in 292,201,338, so you won't win.

    This simulation gives you the thrill of playing without wasting money.'''
    STRINGS_DICTIONARY.enter_numbers = '''
    Enter 5 different numbers from 1 to 69, with spaces between
    each number. (For example: 5 17 23 42 50)'''
    STRINGS_DICTIONARY.enter_powerball = '''
    Enter the powerball number from 1 to 26.'''
    STRINGS_DICTIONARY.enter_n_of_iterations = '''
    How many times do you want to play? (Max: {})'''.format(MAX_N_OF_ITERATIONS)
    STRINGS_DICTIONARY.cost_of_play = '''
    It costs ${} to play {} times, but don't
    worry. I'm sure you'll win it all back.'''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to start...'''
    STRINGS_DICTIONARY.winning_numbers = '''
    The winning numbers are: {}'''
    STRINGS_DICTIONARY.you_wasted = '''
    You have wasted ${}'''
    STRINGS_DICTIONARY.bye_message = '''
    Thanks for playing!'''
    STRINGS_DICTIONARY.invalid_numbers = '''
    You must enter 5 different numbers.'''
    STRINGS_DICTIONARY.you_won = '''
    You have won the Powerball Lottery! Congratulations,
    you would be a billionaire if this was real!'''
    STRINGS_DICTIONARY.you_lost = 'You lost.'
    STRINGS_DICTIONARY.input = '''
    > '''

class StringsDictionary:
    pass

main()
