from bucket import Bucket

EIGHT, FIVE, THREE = '8', '5', '3'
BUCKETS = [EIGHT, FIVE, THREE]
QUIT = 'quit'
YES, NO = 'y', 'n'
FILL, EMPTY, POUR = 'f', 'e', 'p'
WINNING_WATER_LEVEL = 4

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    play_again = True
    while play_again:
        start_new_game()
        play_again = ask_play_again()

def start_new_game():
    is_game_over = False
    buckets = init_buckets()
    while not is_game_over:
        user_input = get_user_input(buckets)
        if user_input == QUIT:
            return
        make_move(buckets, user_input)
        is_game_over = calculate_is_game_over(buckets)
        if is_game_over:
            show_result(buckets)

def make_move(buckets, user_input):
    if user_input == FILL:
        bucket_number = get_bucket_number()
        buckets[bucket_number].fill()
    elif user_input == EMPTY:
        bucket_number = get_bucket_number()
        buckets[bucket_number].empty()
    elif user_input == POUR:
        bucket_from_number, bucket_to_number = get_bucket_numbers()
        pour(buckets, bucket_from_number, bucket_to_number)

def pour(buckets, bucket_from_number, bucket_to_number):
    bucket_from = buckets[bucket_from_number]
    bucket_to = buckets[bucket_to_number]
    bucket_from_capacity, bucket_from_water_level = bucket_from.get_stats()
    bucket_to_capacity, bucket_to_water_level = bucket_to.get_stats()
    bucket_to_available_capacity = bucket_to_capacity - bucket_to_water_level
    amount_to_pour = 0
    if bucket_to_available_capacity > bucket_from_water_level:
        amount_to_pour = bucket_from_water_level
    else:
        amount_to_pour = bucket_to_available_capacity
    bucket_from.remove(amount_to_pour)
    bucket_to.add(amount_to_pour)

def get_bucket_numbers():
    print(STRINGS_DICTIONARY.select_bucket_from)
    bucket_from_number = get_bucket_number()
    print(STRINGS_DICTIONARY.select_bucket_to)
    bucket_to_number = get_bucket_number()
    return bucket_from_number, bucket_to_number

def get_bucket_number():
    print(STRINGS_DICTIONARY.select_bucket)
    user_input = input(STRINGS_DICTIONARY.input)
    if user_input not in BUCKETS:
        return get_bucket_number()
    return user_input

def get_user_input(buckets):
    buckets_image = get_buckets_image(buckets)
    print(STRINGS_DICTIONARY.options.format(buckets_image))
    user_input = input(STRINGS_DICTIONARY.input).lower()
    if user_input not in [FILL, EMPTY, POUR, QUIT]:
        return get_user_input(buckets)

    return user_input

def init_buckets():
    buckets = {}
    for bucket_capacity in BUCKETS:
        buckets[bucket_capacity] = Bucket(bucket_capacity)
    return buckets

def show_buckets(buckets):
    buckets_image = get_buckets_image(buckets)
    print(buckets_image)

def get_buckets_image(buckets):
    bucket_images = [get_bucket_image(bucket) for bucket in buckets.values()]
    image_height = max([len(bucket) for bucket in bucket_images])
    lines = []
    for i in range(image_height):
        index = image_height - i - 1
        lines.append('  '.join([get_bucket_image_line(index, image) for image in bucket_images]))
    return '\n'.join(lines)

def get_bucket_image_line(i, image):
    if len(image) > i:
        return image[i]

    return len(image[0]) * ' '

def get_bucket_image(bucket):
    capacity, current_water_level = bucket.get_stats()
    bottom = ' +------+'
    bucket_width = bottom.count('-')
    label = '    {}L   '.format(capacity)
    image_lines = [label, bottom]
    for i in range(1, capacity + 1):
        content = bucket_width * ('W' if i <= current_water_level else ' ')
        line = '{}|{}|'.format(i, content)
        image_lines.append(line)
    return image_lines

def show_result(buckets):
    show_buckets(buckets)
    print(STRINGS_DICTIONARY.you_won)

def calculate_is_game_over(buckets):
    return any([bucket.get_current_water_level() == WINNING_WATER_LEVEL for bucket in buckets.values()])

def ask_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).lower()
    while not user_input in [YES, NO]:
        return ask_play_again()
    return user_input == YES

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)


def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)


def init():
    init_strings_dictionary()


##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = """
    Water Bucket Puzzle

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A water pouring puzzle.
    More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle"""
    STRINGS_DICTIONARY.options = """
    Try to get 4L of water into one of these
    buckets:

{}

    You can:
    (F)ill the bucket
    (E)mpty the bucket
    (P)our one bucket into another
    (Q)uit"""
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = """
    > """
    STRINGS_DICTIONARY.select_bucket = '''
    Select a bucket: 8, 5, 3:'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.you_won = '''
    Congratulations! You did it!'''
    STRINGS_DICTIONARY.select_bucket_from = '''
    Choosing bucket to pour FROM.'''
    STRINGS_DICTIONARY.select_bucket_to = '''
    Choosing bucket to pour INTO.'''


class StringsDictionary:
    pass


main()
