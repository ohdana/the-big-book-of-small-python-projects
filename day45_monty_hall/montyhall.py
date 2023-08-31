from gameengine import GameEngine

YES, NO = 'Y', 'N'
QUIT = 'QUIT'
N_OF_DOORS = 3
ONE, TWO, THREE = '1', '2', '3'
SWAP, NO_SWAP = 'SWAP', 'NO_SWAP'
WIN, LOSS = 'WIN', 'LOSS'
DOOR_HEIGHT = 7

def main():
    init()
    show_intro_message()
    play()

    say_bye()

def play():
    game_engine = GameEngine(N_OF_DOORS)
    while True:
        game_engine.start_game()
        show_doors(game_engine)
        user_input = get_user_input()
        if user_input == QUIT:
            break
        player_chosen_door = int(user_input)
        game_engine.set_player_initial_choice(player_chosen_door)
        game_engine.open_all_but_one_goat_doors()
        show_doors(game_engine)
        swap = offer_to_swap()
        if swap:
            game_engine.swap_doors()
        game_engine.end_game()
        show_doors(game_engine)
        if game_engine.is_win():
            print(STRINGS_DICTIONARY.you_won)
        else:
            print(STRINGS_DICTIONARY.you_lost)
        stats = game_engine.get_stats()
        show_stats(stats)
        input(STRINGS_DICTIONARY.play_again)

def calculate_rate(wins, losses):
    if not wins:
        return 0.0

    return round(wins * 100 / (wins + losses), 1)

def show_stats(stats):
    swap_wins, swap_losses = stats[SWAP][WIN], stats[SWAP][LOSS]
    swap_rate = calculate_rate(swap_wins, swap_losses)
    no_swap_wins, no_swap_losses = stats[NO_SWAP][WIN], stats[NO_SWAP][LOSS]
    no_swap_rate = calculate_rate(no_swap_wins, no_swap_losses)
    format_params = [swap_wins, swap_losses, swap_rate, no_swap_wins, no_swap_losses, no_swap_rate]
    print(STRINGS_DICTIONARY.stats.format(*format_params))

def show_initial_doors():
    canvas = []
    for i in range(DOOR_HEIGHT):
        lines = []
        for j in range(N_OF_DOORS):
            door_number = j + 1
            line_pattern = get_closed_door_line(i, door_number)
            lines.append(line_pattern)
        canvas.append('  '.join(lines))
    show_canvas(canvas)

def get_closed_door_line(line_number, door_number):
    line_pattern = STRINGS_DICTIONARY.closed_door[line_number]
    if '{}' in line_pattern:
        line_pattern = line_pattern.format(door_number)

    return line_pattern

def show_doors(game_engine):
    canvas = []
    opened_doors = game_engine.get_opened_doors()
    for i in range(DOOR_HEIGHT):
        lines = []
        for j in range(N_OF_DOORS):
            door_number = j + 1
            if door_number in opened_doors.keys():
                door = opened_doors[door_number]
                if door.is_goat():
                    line_pattern = STRINGS_DICTIONARY.goat_door[i]
                elif door.is_car():
                    line_pattern = STRINGS_DICTIONARY.car_door[i]
            else:
                line_pattern = get_closed_door_line(i, door_number)
            lines.append(line_pattern)
        canvas.append('  '.join(lines))
    show_canvas(canvas)

def show_canvas(canvas):
    print('\n'.join(canvas))

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
