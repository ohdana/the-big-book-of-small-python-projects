import re, random

INPUT_REGEX = '^(([1-9][0-9]*)d([1-9][0-9]*)([\+,\-][1-9][0-9]*)*)$'

def main():
    init()
    show_intro_message()
    while True:
        user_input = get_user_input()
        n_of_dice, n_of_sides, extra = parse_user_input(user_input)
        dice = roll_dice(n_of_dice, n_of_sides)
        show_result(dice, extra)

def show_result(dice, extra):
    total = calculate_sum(dice, extra)
    expanded_result = [str(die) for die in dice]
    if extra:
        expanded_result.append(f'{extra:+}')
    expanded_result_str = '(' + ', '.join(expanded_result) + ')'

    print(total, expanded_result_str)

def calculate_sum(dice, extra=0):
    return sum(dice) + extra

def roll_dice(n_of_dice, n_of_sides):
    return [roll_die(n_of_sides) for die in range(n_of_dice)]

def roll_die(n_of_sides):
    return random.randint(1, n_of_sides)

def parse_user_input(user_input):
    regex_match = re.search(INPUT_REGEX, user_input)
    n_of_dice = regex_match.group(2)
    n_of_sides = regex_match.group(3)
    extra = regex_match.group(4)
    if not extra:
        extra = 0

    return int(n_of_dice), int(n_of_sides), int(extra)

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.your_input)
    if user_input == 'QUIT':
        say_bye()

    if not is_valid_user_input(user_input):
        return get_user_input()

    return user_input

def is_valid_user_input(user_input):
    if not user_input:
        return False

    if not re.search(INPUT_REGEX, user_input):
        return False

    return True

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
    Dice Roller

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Simulates dice rolls using the Dungeons & Dragons dice roll notation.
    Enter what kind and how many dice to roll. The format is the number of
    dice, followed by 'd', followed by the number of sides the dice have.
    You can also add a plus or minus adjustments.

    Examples:
        3d6 rolls three 6-sided dice
        1d10+2 rolls one 10-sided die, and adds 2
        2d38-1 rolls two 38-sided dice, and subtracts 1
        QUIT quits the program'''
    STRINGS_DICTIONARY.your_input = '''
    >>>'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''

class StringsDictionary:
    pass

main()
