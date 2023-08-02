import random, time

WINDOW_WIDTH = 100
ACTIONS_DICE = {}
SLEEP_BETWEEN_LINES_SECONDS = 0.07
EARTH_CHAR = '#'
GAP_CHAR = ' '

def main():
    init()
    show_intro_message()

    left = 20
    gap = 15
    while True:
        left, gap = go_deep(left, gap)
        time.sleep(SLEEP_BETWEEN_LINES_SECONDS)

def go_deep(left, gap):
    new_line, left, gap = generate_new_line(left, gap)
    show_line(new_line)

    return left, gap

def show_line(line):
    print(line)

def generate_new_line(left, gap):
    right = get_right(left, gap)
    action = ACTIONS_DICE[random.randint(1, 6)]
    left, gap, right = action(left, gap, right)

    return build_line(left, gap, right), left, gap

def build_line(left, gap, right):
    return EARTH_CHAR*left + GAP_CHAR*gap + EARTH_CHAR*right

def get_right(left, gap):
    return WINDOW_WIDTH - gap - left

def increment_gap_left(left, gap, right):
    if left > 1:
        left -= 1
        gap += 1

    return (left, gap, right)

def increment_gap_right(left, gap, right):
    if right > 1:
        right -= 1
        gap += 1

    return (left, gap, right)

def decrement_gap_left(left, gap, right):
    if gap > 1:
        gap -= 1
        left += 1

    return (left, gap, right)

def decrement_gap_right(left, gap, right):
    if gap > 1:
        gap -= 1
        right += 1

    return (left, gap, right)

def increment_gap_both_sides(left, gap, right):
    left, gap, right = increment_gap_left(left, gap, right)
    left, gap, right = increment_gap_right(left, gap, right)

    return (left, gap, right)

def decrement_gap_both_sides(left, gap, right):
    left, gap, right = decrement_gap_left(left, gap, right)
    left, gap, right = decrement_gap_right(left, gap, right)

    return (left, gap, right)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def populate_actions_dice():
    ACTIONS_DICE[1] = increment_gap_left
    ACTIONS_DICE[2] = increment_gap_right
    ACTIONS_DICE[3] = decrement_gap_left
    ACTIONS_DICE[4] = decrement_gap_right
    ACTIONS_DICE[5] = increment_gap_both_sides
    ACTIONS_DICE[6] = decrement_gap_both_sides

def init():
    init_strings_dictionary()
    populate_actions_dice()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Deep Cave

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    An animation of a deep cave that goes forever into the earth.'''

class StringsDictionary:
    pass

main()
