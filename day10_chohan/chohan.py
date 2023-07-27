import random

MIN_BET = 1
MAX_BET = 1000
MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6
INITIAL_BALANCE = 1000
PLAYER_BALANCE = INITIAL_BALANCE
HOUSE_FEE_PERCENT = 0.05
BET = 0
DICE_IMG_MAP = {}

def main():
    init()
    show_intro_message()
    play_again = True

    while play_again:
        play()
        play_again = prompt_play_again()

def play():
    print(STRINGS_DICTIONARY.money.format(PLAYER_BALANCE))
    take_bet()
    player_move = get_player_move_input()
    dice = dealer_throws_dice()
    show_dice(dice)
    calculate_game_result(sum(dice), player_move)

def calculate_game_result(dice_sum, player_move):
    player_won = check_if_player_won(dice_sum, player_move)
    if player_won:
        win()
    else:
        loss()

def check_if_player_won(dices_sum, player_move):
    if dices_sum % 2 == 0:
        return player_move == 'cho'

    return player_move == 'han'

def win():
    print(STRINGS_DICTIONARY.you_won.format(BET))

    house_fee = calculate_house_fee()
    print(STRINGS_DICTIONARY.house_takes_fee.format(house_fee))
    payout(BET * 2 - house_fee)

def calculate_house_fee():
    return round(BET * HOUSE_FEE_PERCENT)

def loss():
    print(STRINGS_DICTIONARY.you_lost)

def take_bet():
    player_bet = get_bet()
    bet(int(player_bet))

def dealer_throws_dice():
    print(STRINGS_DICTIONARY.dealer_throws_dice)
    dice = [throw_die(), throw_die()]

    return dice

def throw_die():
    return random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE)

def quit():
    global PLAY_AGAIN
    PLAY_AGAIN = False
    print(STRINGS_DICTIONARY.your_final_total.format(PLAYER_BALANCE))
    print(STRINGS_DICTIONARY.goodbye_message)

def bet(amount):
    global BET, PLAYER_BALANCE
    BET += amount
    PLAYER_BALANCE -= amount

def payout(amount):
    global PLAYER_BALANCE
    PLAYER_BALANCE += amount

def get_bet():
    bet = input(STRINGS_DICTIONARY.how_much_bet)

    if bet == 'QUIT':
        stop_game()
        return

    while not is_valid_bet(bet):
        bet = input(STRINGS_DICTIONARY.invalid_bet_input)

    while int(bet) > PLAYER_BALANCE:
        bet = input(STRINGS_DICTIONARY.low_balance.format(PLAYER_BALANCE))

    return bet

def prompt_play_again():
    play_again = input(STRINGS_DICTIONARY.play_again)

    while not is_valid_play_again(play_again):
        play_again = input(STRINGS_DICTIONARY.play_again)

    if play_again == 'n':
        quit()

    return True

def get_player_move_input():
    move = input(STRINGS_DICTIONARY.cho_han_input).lower()

    while not is_valid_player_move(move):
        move = input(STRINGS_DICTIONARY.cho_han_input)

    return move

def show_dice(dice):
    print(STRINGS_DICTIONARY.dealer_reveals_dice)

    dice1_img_lines = DICE_IMG_MAP[dice[0]].split('\n')
    dice2_img_lines = DICE_IMG_MAP[dice[1]].split('\n')
    for i in range(len(dice1_img_lines)):
        print(dice1_img_lines[i] + '   ' + dice2_img_lines[i])

def is_valid_play_again(play_again):
    if not play_again.isalpha():
        return False

    if not play_again in ['y', 'n']:
        return False

    return True

def is_valid_bet(bet):
    if not bet.isdigit():
        return False

    if not MIN_BET <= int(bet) <= MAX_BET:
        return False

    return True

def is_valid_player_move(move):
    if not move:
        return False

    valid_inputs = ['cho', 'han']
    if move not in valid_inputs:
        return False

    return True

def init():
    init_strings_dictionary()
    init_dice_img_map()

def init_dice_img_map():
    DICE_IMG_MAP[1] = STRINGS_DICTIONARY.dice1
    DICE_IMG_MAP[2] = STRINGS_DICTIONARY.dice2
    DICE_IMG_MAP[3] = STRINGS_DICTIONARY.dice3
    DICE_IMG_MAP[4] = STRINGS_DICTIONARY.dice4
    DICE_IMG_MAP[5] = STRINGS_DICTIONARY.dice5
    DICE_IMG_MAP[6] = STRINGS_DICTIONARY.dice6

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.goodbye_message)
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Cho-Han

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    In this traditional Japanese dice game, two dice are rolled in a bamboo
    cup by the dealer sitting on the floor. The player must guess if the
    dice total to an even (cho) or odd (han) number.'''
    STRINGS_DICTIONARY.dealer_throws_dice = '''
    The dealer swirls the cup and you hear the rattle of dice.
    The dealer slams the cup on the floor, still covering the
    dice and asks for your bet.

        CHO (even) or HAN (odd)?'''
    STRINGS_DICTIONARY.dealer_reveals_dice = '''
    The dealer lifts the cup to reveal: '''
    STRINGS_DICTIONARY.cho_han_input = '''
    Please enter \'cho\' for even or \'han\' for odd: '''
    STRINGS_DICTIONARY.money = '''
    You have {} mon.'''
    STRINGS_DICTIONARY.low_balance = '''
    This amount is bigger than your balance. Your balance is {} mon.'''
    STRINGS_DICTIONARY.how_much_bet = '''
    How much do you bet? ({min_bet}-{max_bet}, or QUIT)
    '''.format(min_bet=MIN_BET, max_bet=MAX_BET)
    STRINGS_DICTIONARY.invalid_bet_input = '''
    Please enter amount between {min_bet} and {max_bet} or \'QUIT\' to end the game
    '''.format(min_bet=MIN_BET, max_bet=MAX_BET)
    STRINGS_DICTIONARY.you_won = '''
    You won {} mon!'''
    STRINGS_DICTIONARY.you_lost = '''
    You lost!'''
    STRINGS_DICTIONARY.house_takes_fee = '''
    The house takes {} mon fee.'''
    STRINGS_DICTIONARY.your_final_total = '''
    Your final balance is {} mon.'''
    STRINGS_DICTIONARY.goodbye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.separator = '''
    ==============================='''
    STRINGS_DICTIONARY.dice1 = '''
._______.
|       |
|   *   |
|       |
 ------- '''
    STRINGS_DICTIONARY.dice2 = '''
._______.
|       |
|  * *  |
|       |
 ------- '''
    STRINGS_DICTIONARY.dice3 = '''
._______.
|       |
| * * * |
|       |
 ------- '''
    STRINGS_DICTIONARY.dice4 = '''
._______.
| *   * |
|       |
| *   * |
 ------- '''
    STRINGS_DICTIONARY.dice5 = '''
._______.
| *   * |
|   *   |
| *   * |
 ------- '''
    STRINGS_DICTIONARY.dice6 = '''
._______.
| * * * |
|       |
| * * * |
 ------- '''
class StringsDictionary:
    pass

main()
