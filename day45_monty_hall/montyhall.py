from gameengine import GameEngine
from canvasprinter import CanvasPrinter

YES, NO = 'Y', 'N'
QUIT = 'QUIT'
N_OF_DOORS = 3
ONE, TWO, THREE = '1', '2', '3'
SWAP, NO_SWAP = 'SWAP', 'NO_SWAP'
WIN, LOSS = 'WIN', 'LOSS'
GAME_ENGINE = None
CANVAS_PRINTER = None

def main():
    init()
    show_intro_message()
    play()

    say_bye()

def play():
    while True:
        start_game()
        user_input = get_user_input()
        if is_quit_requested(user_input):
            break
        offer_to_choose_a_door(user_input)
        open_all_but_two_doors()
        offer_to_swap_the_door()
        end_game()
        show_stats()
        offer_to_play_again()

def start_game():
    GAME_ENGINE.start_game()
    show_doors()

def end_game():
    GAME_ENGINE.end_game()
    show_doors()

def is_quit_requested(user_input):
    return user_input == QUIT

def offer_to_play_again():
    input(STRINGS_DICTIONARY.play_again)

def calculate_results():
    if GAME_ENGINE.is_win():
        print(STRINGS_DICTIONARY.you_won)
    else:
        print(STRINGS_DICTIONARY.you_lost)

def offer_to_swap_the_door():
    show_doors()
    swap = offer_to_swap()
    if swap:
        GAME_ENGINE.swap_doors()
    else:
        GAME_ENGINE.confirm_initial_choice()

def open_all_but_two_doors():
    GAME_ENGINE.open_all_but_one_goat_doors()

def offer_to_choose_a_door(user_input):
    player_chosen_door = int(user_input)
    GAME_ENGINE.set_player_initial_choice(player_chosen_door)

def show_stats():
    stats = GAME_ENGINE.get_stats()
    swap_wins, swap_losses = stats[SWAP][WIN], stats[SWAP][LOSS]
    swap_rate = calculate_rate(swap_wins, swap_losses)

    no_swap_wins, no_swap_losses = stats[NO_SWAP][WIN], stats[NO_SWAP][LOSS]
    no_swap_rate = calculate_rate(no_swap_wins, no_swap_losses)

    format_params = [swap_wins, swap_losses, swap_rate, no_swap_wins, no_swap_losses, no_swap_rate]
    print(STRINGS_DICTIONARY.stats.format(*format_params))

def show_doors():
    opened_doors = GAME_ENGINE.get_opened_doors()
    CANVAS_PRINTER.show_canvas(opened_doors)

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.pick_door)
    if not is_valid_user_input(user_input):
        return get_user_input()

    return user_input.upper()

def offer_to_swap():
    user_input = input(STRINGS_DICTIONARY.ask_swap_doors)
    while not is_valid_y_n(user_input):
        return offer_to_swap()

    return user_input.upper() == YES

def is_valid_user_input(user_input):
    if user_input.upper() == QUIT:
        return True

    if not user_input.isdigit():
        return False

    return user_input in [ONE, TWO, THREE, QUIT]

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def calculate_rate(wins, losses):
    if not wins:
        return 0.0

    return round(wins * 100 / (wins + losses), 1)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()
    init_game_engine()
    init_canvas_printer()

def init_game_engine():
    global GAME_ENGINE
    GAME_ENGINE = GameEngine(N_OF_DOORS)

def init_canvas_printer():
    global CANVAS_PRINTER
    CANVAS_PRINTER = CanvasPrinter(N_OF_DOORS)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    The Monty Hall Problem

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A simulation of the Monty Hall game show problem.
    https://en.wikipedia.org/wiki/Monty_Hall_problem'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Press Enter to repeat the experiment...'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.pick_door = '''
    Pick a door 1, 2, or 3 (or QUIT to stop): '''
    STRINGS_DICTIONARY.door_goat = '''
    Door {} contains a goat!'''
    STRINGS_DICTIONARY.ask_swap_doors = '''
    Do you want to swap doors? y/n: '''
    STRINGS_DICTIONARY.door_car = '''
    Door {} has a car!'''
    STRINGS_DICTIONARY.you_won = '''
    You won!'''
    STRINGS_DICTIONARY.you_lost = '''
    Better luck next time!'''
    STRINGS_DICTIONARY.stats = '''
    Swapping: {} wins, {} losses, success rate {}%
    Not swapping: {} wins, {} losses, success rate {}%'''
    STRINGS_DICTIONARY.goat_door = ['+------+', '|  ((  |', '|  oo  |', '| /_/|_|', '|    | |', '|GOAT|||', '+------+']
    STRINGS_DICTIONARY.car_door = ['+------+', '| CAR! |', '|    __|', '|  _/  |', '| /_ __|', '|   O  |', '+------+']
    STRINGS_DICTIONARY.closed_door = ['+------+', '|      |', '|   {}  |', '|      |', '|      |', '|      |', '+------+']

class StringsDictionary:
    pass

main()
