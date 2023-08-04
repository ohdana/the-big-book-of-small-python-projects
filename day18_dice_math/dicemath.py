import random
from datetime import datetime, timedelta

CANVAS_WIDTH = 70
CANVAS_HEIGHT = 20
CANVAS = None
DIE_WIDTH = 0
DIE_HEIGHT = 0
MIN_DIE_VALUE = 1
MAX_DIE_VALUE = 6
MIN_N_OF_DICE = 2
MAX_N_OF_DICE = 6
DICE_MAP = {}
USER_CORRECT_ANSWERS = 0
USER_INCORRECT_ANSWERS = 0
POINTS_FOR_CORRECT_ANSWER = 4
POINTS_FOR_INCORRECT_ANSWER = -1
INITIAL_TIMER_SECONDS = 10

def main():
    init()
    show_intro_message()
    play_again = True

    while play_again:
        play()
        play_again = prompt_play_again()

def show_canvas():
    lines = [''.join(line) for line in CANVAS]
    print('\n'.join(lines))

def show_dice(dice):
    for die in dice:
        allocate_die(die)

    show_canvas()

def allocate_die(die):
    left_x, top_y = find_free_spot()
    die_img = get_die_img_lines(die)

    for i in range(DIE_HEIGHT):
        for j in range(DIE_WIDTH):
            CANVAS[top_y + i][left_x + j] = die_img[i][j]

    return left_x, top_y

def find_free_spot():
    min_x, min_y = 0, 0
    max_x = CANVAS_WIDTH - DIE_WIDTH - 1
    max_y = CANVAS_HEIGHT - DIE_HEIGHT - 1
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)

    if is_overlapping(x, y):
        return find_free_spot()

    return x, y

def is_overlapping(left_x, top_y):
    right_x = left_x + DIE_WIDTH
    bottom_y = top_y + DIE_HEIGHT

    for x in range(left_x, right_x):
        for y in range(top_y, bottom_y):
            if CANVAS[y][x] != ' ':
                return True

    return False

def play():
    reset_game()
    seconds_left = INITIAL_TIMER_SECONDS
    deadline = datetime.now() + timedelta(seconds=seconds_left)
    while datetime.now() <= deadline:
        dice = throw_dice()
        user_answer = get_user_answer()
        if is_correct_user_answer(user_answer, dice):
            user_gives_correct_answer()
        else:
            user_gives_incorrect_answer()
        reset_canvas()
    game_over()
    show_results()

def throw_dice():
    n_of_dice = get_n_of_dice()
    dice = [roll_die() for i in range(n_of_dice)]
    show_dice(dice)

    return dice

def get_n_of_dice():
    return random.randint(MIN_N_OF_DICE, MAX_N_OF_DICE)

def roll_die():
    return random.randint(MIN_DIE_VALUE, MAX_DIE_VALUE)

def user_gives_correct_answer():
    global USER_CORRECT_ANSWERS
    USER_CORRECT_ANSWERS += 1

def user_gives_incorrect_answer():
    global USER_INCORRECT_ANSWERS
    USER_INCORRECT_ANSWERS += 1

def game_over():
    print(STRINGS_DICTIONARY.time_up)

def show_results():
    total_answers = USER_CORRECT_ANSWERS + USER_INCORRECT_ANSWERS
    user_score = get_user_score()
    print(STRINGS_DICTIONARY.you_answered.format(USER_CORRECT_ANSWERS, total_answers))
    print(STRINGS_DICTIONARY.your_score.format(user_score))

def get_user_score():
    score_for_correct_answers = POINTS_FOR_CORRECT_ANSWER * USER_CORRECT_ANSWERS
    score_for_incorrect_answers = POINTS_FOR_INCORRECT_ANSWER * USER_INCORRECT_ANSWERS
    return score_for_correct_answers + score_for_incorrect_answers

def get_user_answer():
    answer = input(STRINGS_DICTIONARY.enter_the_sum)

    while not is_valid_user_answer(answer):
        answer = input(STRINGS_DICTIONARY.invalid_user_answer)

    return int(answer)

def calculate_dice_sum(dice):
    return sum(dice)

def is_correct_user_answer(user_answer, dice):
    correct_answer = calculate_dice_sum(dice)
    return user_answer == correct_answer

def prompt_play_again():
    answer = ''

    while not is_valid_y_n(answer):
        answer = input(STRINGS_DICTIONARY.play_again)

    return answer == 'y'

def is_valid_y_n(answer):
    if not answer:
        return False

    return answer in ['y', 'n']

def is_valid_user_answer(answer):
    if not answer:
        return False

    if not answer.isdigit():
        return False

    return True

def reset_canvas():
    global CANVAS
    CANVAS = []
    for i in range(CANVAS_HEIGHT):
        CANVAS.append([' '] * CANVAS_WIDTH)

def reset_game():
    global USER_CORRECT_ANSWERS, USER_INCORRECT_ANSWERS
    USER_CORRECT_ANSWERS = 0
    USER_INCORRECT_ANSWERS = 0

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init_dice_map():
    DICE_MAP[1] = [STRINGS_DICTIONARY.dice1]
    DICE_MAP[2] = [STRINGS_DICTIONARY.dice2a, STRINGS_DICTIONARY.dice2b]
    DICE_MAP[3] = [STRINGS_DICTIONARY.dice3a, STRINGS_DICTIONARY.dice3b]
    DICE_MAP[4] = [STRINGS_DICTIONARY.dice4]
    DICE_MAP[5] = [STRINGS_DICTIONARY.dice5]
    DICE_MAP[6] = [STRINGS_DICTIONARY.dice6a, STRINGS_DICTIONARY.dice6b]

def get_die_img_lines(n):
    return random.choice(DICE_MAP[n])

def init_die_dimensions():
    global DIE_HEIGHT, DIE_WIDTH
    any_die = DICE_MAP[1][0]
    DIE_HEIGHT = len(any_die)
    DIE_WIDTH = len(any_die[0])

def init():
    init_strings_dictionary()
    init_dice_map()
    init_die_dimensions()
    reset_canvas()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Dice Math

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Add up the sides of all the dice displayed on the screen. You have
    30 seconds to answer as many as possible. You get 4 points for each
    correct answer and lose 1 point for each incorrect answer.'''

    STRINGS_DICTIONARY.press_enter = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.enter_the_sum = '''
    Enter the sum: '''
    STRINGS_DICTIONARY.invalid_user_answer = '''
    Enter the sum (please use digits only): '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.timer = 'Time: {}'
    STRINGS_DICTIONARY.you_answered = '''
    You answered correctly {} out of {} times.'''
    STRINGS_DICTIONARY.your_score = '''
    Your score: {}'''
    STRINGS_DICTIONARY.time_up = '''
    Your time's up!'''
    STRINGS_DICTIONARY.dice1 = [
    '+-------+',
    '|       |',
    '|   o   |',
    '|       |',
    '+-------+']
    STRINGS_DICTIONARY.dice2a = [
    '+-------+',
    '|     o |',
    '|       |',
    '| o     |',
    '+-------+']
    STRINGS_DICTIONARY.dice2b = [
    '+-------+',
    '| o     |',
    '|       |',
    '|     o |',
    '+-------+']
    STRINGS_DICTIONARY.dice3a = [
    '+-------+',
    '|     o |',
    '|   o   |',
    '| o     |',
    '+-------+']
    STRINGS_DICTIONARY.dice3b = [
    '+-------+',
    '| o     |',
    '|   o   |',
    '|     o |',
    '+-------+']
    STRINGS_DICTIONARY.dice4 = [
    '+-------+',
    '| o   o |',
    '|       |',
    '| o   o |',
    '+-------+']
    STRINGS_DICTIONARY.dice5 = [
    '+-------+',
    '| o   o |',
    '|   o   |',
    '| o   o |',
    '+-------+']
    STRINGS_DICTIONARY.dice6a = [
    '+-------+',
    '| o   o |',
    '| o   o |',
    '| o   o |',
    '+-------+']
    STRINGS_DICTIONARY.dice6b = [
    '+-------+',
    '| o o o |',
    '|       |',
    '| o o o |',
    '+-------+']

class StringsDictionary:
    pass

main()
