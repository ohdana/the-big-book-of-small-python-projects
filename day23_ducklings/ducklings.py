import random, time

CANVAS_WIDTH = 70
CANVAS_HEIGHT = 10
DENSITY_PERCENT = 80
SLEEP_BETWEEN_LINES_SECONDS = 0.1
DUCKLING_HEIGHT = 3
LEFT, RIGHT, COMMON = 'left', 'right', 'common'
NORMAL, CHUBBY, VERY_CHUBBY = 'normal', 'chubby', 'very chubby'
DUCKLING_DIRECTIONS = [LEFT, RIGHT]
DUCKLING_BODY_TYPE = [NORMAL, CHUBBY, VERY_CHUBBY]
DUCKLING_WINGS = { COMMON: ['^', 'V'], RIGHT: ['<'], LEFT: ['>']}
DUCKLING_BEAKS = { COMMON: ['='], RIGHT: ['<'], LEFT: ['>']}
DUCKLING_EYES = { COMMON: ['\'\'', '\' \'', '^^', '``'], RIGHT: [' "'], LEFT: ['" ']}
DUCKLING_FEET = { COMMON: ['^^']}

def main():
    init()
    show_intro_message()
    generate_ducks()

def generate_ducks():
    canvas = init_canvas()
    while True:
        add_new_duck = decide_if_add_new_duck()
        if add_new_duck:
            add_duck_to_canvas(canvas)
        canvas = update_canvas(canvas)
        time.sleep(SLEEP_BETWEEN_LINES_SECONDS)

def decide_if_add_new_duck():
    return random.randint(1, 100) <= DENSITY_PERCENT

def add_duck_to_canvas(canvas):
    duck_img = generate_duck()
    duck_width = max([len(line) for line in duck_img])
    left_x, top_y = find_free_spot(duck_width, DUCKLING_HEIGHT, canvas)

    for i in range(DUCKLING_HEIGHT):
        for j in range(duck_width):
            char = ' '
            if j < len(duck_img[i]):
                char = duck_img[i][j]

            canvas[top_y + i][left_x + j] = char

def find_free_spot(duck_width, duck_height, canvas):
    min_x, min_y = 0, 0
    max_x = CANVAS_WIDTH - duck_width - 1
    max_y = CANVAS_HEIGHT - duck_height - 1
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)

    if is_overlapping(x, y, duck_width, duck_height, canvas):
        return find_free_spot(duck_width, duck_height, canvas)

    return x, y

def is_overlapping(left_x, top_y, duck_width, duck_height, canvas):
    right_x = left_x + duck_width
    bottom_y = top_y + duck_height

    for x in range(left_x, right_x):
        for y in range(top_y, bottom_y):
            if canvas[y][x] != ' ':
                return True

    return False

def generate_duck():
    direction = random.choice(DUCKLING_DIRECTIONS)
    body_type = random.choice(DUCKLING_BODY_TYPE)
    head = generate_head(direction, body_type)
    body = generate_body(direction, body_type)
    feet = generate_feet(body_type)

    return [head, body, feet]

def generate_head(direction, body_type):
    gap = get_gap(body_type)
    result = ''
    if direction == RIGHT:
        beak = random.choice(DUCKLING_BEAKS[COMMON] + DUCKLING_BEAKS[RIGHT])
        eyes = random.choice(DUCKLING_EYES[COMMON] + DUCKLING_EYES[RIGHT])
        result += '(' + gap + eyes + beak
    else:
        beak = random.choice(DUCKLING_BEAKS[COMMON] + DUCKLING_BEAKS[LEFT])
        eyes = random.choice(DUCKLING_EYES[COMMON] + DUCKLING_EYES[LEFT])
        result += beak + eyes + gap + ')'

    return result

def generate_body(direction, body_type):
    gap = ' ' + get_gap(body_type)
    result = '('
    if direction == RIGHT:
        wing = random.choice(DUCKLING_WINGS[COMMON] + DUCKLING_WINGS[RIGHT])
        result += wing + gap
    else:
        wing = random.choice(DUCKLING_WINGS[COMMON] + DUCKLING_WINGS[LEFT])
        result += gap + wing
    result += ')'

    return result

def generate_feet(body_type):
    feet = random.choice(DUCKLING_FEET[COMMON])
    gap = get_gap(body_type)

    return ' ' + feet[:1] + gap + feet[-1:] + ' '

def get_gap(body_type):
    if body_type == VERY_CHUBBY:
        return '  '
    elif body_type == CHUBBY:
        return ' '
    else:
        return ''

def update_canvas(canvas):
    print(''.join(canvas[0]))

    return canvas[1:] + [([' '] * CANVAS_WIDTH)]

def init_canvas():
    canvas = []
    for i in range(CANVAS_HEIGHT):
        canvas.append([' '] * CANVAS_WIDTH)

    return canvas

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
    init_canvas()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Ducklings Screensaver

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A screensaver of many many ducklings.'''

class StringsDictionary:
    pass

main()
