from gameengine import GameEngine

LEFT, MIDDLE, RIGHT = 'left', 'middle', 'right'
CARD_INDEX_MAP = { LEFT: 0, MIDDLE: 1, RIGHT: 2 }
CARD_POSITION_MAP = { 0: LEFT, 1: MIDDLE, 2: RIGHT }
YES, NO = 'y', 'n'

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    game_engine = GameEngine()
    play_again = True
    while play_again:
        start_new_game(game_engine)
        play_again = do_play_again()

def start_new_game(game_engine):
    show_cards(game_engine)
    input(STRINGS_DICTIONARY.press_enter)
    shuffle_log = game_engine.shuffle()
    show_shuffle_log(shuffle_log)
    user_answer = ask_where_is_queen()
    is_winning_answer = game_engine.is_winning_answer(CARD_INDEX_MAP[user_answer])
    show_cards(game_engine)
    if is_winning_answer:
        user_won()
    else:
        user_lost()

def show_shuffle_log(shuffle_log):
    for entry in shuffle_log:
        index_1, index_2 = entry
        position_1, position_2 = CARD_POSITION_MAP[index_1], CARD_POSITION_MAP[index_2]
        print(STRINGS_DICTIONARY.swapping.format(position_1, position_2))

def get_card_position(card_index):
    return list(CARD_INDEX_MAP.keys())[list(CARD_INDEX_MAP.values()).index(card_index)]

def user_won():
    print(STRINGS_DICTIONARY.you_won)

def user_lost():
    print(STRINGS_DICTIONARY.you_lost)

def show_cards(game_engine):
    cards_image = game_engine.get_cards_image()
    print(STRINGS_DICTIONARY.cards)
    print(cards_image)

def ask_where_is_queen():
    print(STRINGS_DICTIONARY.where_is_queen)
    user_input = input(STRINGS_DICTIONARY.input).lower()
    while not is_valid_user_input(user_input):
        return ask_where_is_queen()
    return user_input

def is_valid_user_input(user_input):
    return user_input in [LEFT, MIDDLE, RIGHT]

def do_play_again():
    user_input = input(STRINGS_DICTIONARY.play_again).lower()
    if not user_input in [YES, NO]:
        return do_play_again()

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

    STRINGS_DICTIONARY.intro_message = '''
    Three-Card Monte

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    TFind the red lady (the Queen of Hearts)!
    Keep an eye on how the cards move.'''
    STRINGS_DICTIONARY.cards = '''
    Here are the cards:'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.input = '''
    > '''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.press_enter = '''
    Press Enter when you are ready to begin...'''
    STRINGS_DICTIONARY.you_won = '''
    You won!
    Thanks for playing!'''
    STRINGS_DICTIONARY.you_lost = '''
    You lost!
    Thanks for playing, sucker!'''
    STRINGS_DICTIONARY.where_is_queen = '''
    Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)'''
    STRINGS_DICTIONARY.swapping = '''
    swapping {} and {}...'''

class StringsDictionary:
    pass

main()
