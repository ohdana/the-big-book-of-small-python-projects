from random import choices

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
MIN_CARD_VALUE = 2
MAX_CARD_VALUE = 10
DECK = []
CARD_VALUE_MAP = {}

PLAY_AGAIN = True
INITIAL_PLAYER_BALANCE = 1000
PLAYER_BALANCE = INITIAL_PLAYER_BALANCE
MIN_BET = 1
MAX_BET = 5000
BET = 0
PLAYER_CARDS = []
DEALER_CARDS = []
PLAYER_STOPPED = False
DEALER_STOPPED = False

def main():
    init()
    while PLAY_AGAIN:
        play()

def play():
    init_new_game()
    show_current_results()
    while not (PLAYER_STOPPED and DEALER_STOPPED):
        player_move()
        dealer_move()

    calculate_results()
    prompt_play_again()

def prompt_play_again():
    play_again = input(STRINGS_DICTIONARY.play_again)

    while not is_valid_play_again(play_again):
        play_again = input(STRINGS_DICTIONARY.play_again)

    if play_again == 'n':
        quit()

def is_valid_play_again(play_again):
    if not play_again.isalpha():
        return False

    if not play_again in ['y', 'n']:
        return False

    return True

def init_new_game():
    reset_game()
    show_player_balance()
    take_player_bet()
    draw_initial_cards(PLAYER_CARDS)
    draw_initial_cards(DEALER_CARDS)

def take_player_bet():
    global BET, PLAYER_BALANCE
    bet = get_bet()
    print(STRINGS_DICTIONARY.bet.format(bet))
    BET += int(bet)
    PLAYER_BALANCE -= int(bet)

def player_move():
    move = get_player_move_input()

    if move == 'h':
        hit()
    elif move == 's':
        stand()
    elif move == 'd':
        double_down()

    sums = get_sums(PLAYER_CARDS)
    went_above_21 = all(sum > 21 for sum in sums)
    if went_above_21:
        player_lost()

def dealer_move():
    global DEALER_STOPPED
    if DEALER_STOPPED:
        return

    card = draw_card()
    dealer_draws(card)

    sums = get_sums(DEALER_CARDS)

    reached_soft_17 = any(sum >= 17 for sum in sums)
    if reached_soft_17:
        DEALER_STOPPED = True

    went_above_21 = all(sum > 21 for sum in sums)
    if went_above_21:
        player_won()

def calculate_results():
    dealer_sums = get_sums(DEALER_CARDS)
    player_sums = get_sums(PLAYER_CARDS)

    player_best = get_best_sum(player_sums)
    dealer_best = get_best_sum(dealer_sums)

    if not (PLAYER_STOPPED and DEALER_STOPPED):
        return

    if player_best == dealer_best:
        tie()
    elif player_best > dealer_best:
        player_won()
    else:
        player_lost()

def get_best_sum(sums):
    if len(sums) == 1:
        return sums[0]

    return max([sum for sum in sums if sum <= 21])

def draw_card():
    return choices(DECK, k=1)[0]

def player_draws(card):
    PLAYER_CARDS.append(card)
    print(STRINGS_DICTIONARY.you_drew.format(card))

def dealer_draws(card):
    DEALER_CARDS.append(card)

def get_player_move_input():
    move = input(STRINGS_DICTIONARY.hit_stand_double).lower()

    while not is_valid_player_move(move):
        move = input(STRINGS_DICTIONARY.hit_stand_double)

    return move

def stop_game():
    global PLAYER_STOPPED, DEALER_STOPPED
    PLAYER_STOPPED = True
    DEALER_STOPPED = True

def tie():
    stop_game()
    print('Tie.')

def player_won():
    stop_game()
    print('Player wins!')

def player_lost():
    stop_game()
    print('Player lost!')

def show_current_results():
    dealer_sum = get_sums(DEALER_CARDS)
    print(STRINGS_DICTIONARY.dealer.format(get_sums_string(dealer_sum)))
    show_hand(DEALER_CARDS)

    player_sum = get_sums(PLAYER_CARDS)
    print(STRINGS_DICTIONARY.player.format(get_sums_string(player_sum)))
    show_hand(PLAYER_CARDS)

def draw_initial_cards(hand):
    hand.append(draw_card())
    hand.append(draw_card())

def show_hand(cards):
    for card in cards:
        print(card)

def get_sums(cards):
    cards_without_aces = [card for card in cards if card[0] != 'A']
    sum_without_aces = sum([CARD_VALUE_MAP[card[0]] for card in cards_without_aces])

    n_of_aces = len(cards) - len(cards_without_aces)
    if n_of_aces == 0:
        return [sum_without_aces]

    possible_aces_sum = get_possible_aces_sums(n_of_aces)
    possible_sums = [(sum_without_aces + sum) for sum in possible_aces_sum]

    if len(possible_sums) == 1:
        return possible_sums

    if 21 in possible_sums:
        return [21]

    return [sum for sum in possible_sums if sum <= 21]

def get_possible_aces_sums(n_of_aces):
    possible_sums = []
    for n in range(n_of_aces + 1):
        low_ace_value = 1
        high_ace_value = 11

        possible_aces_sum = low_ace_value * n + high_ace_value * (n_of_aces - n)
        possible_sums.append(possible_aces_sum)
        n -= 1

    return possible_sums

def get_sums_string(potential_sums):
    return ' or '.join(str(sum) for sum in potential_sums)

def hit():
    card = draw_card()
    player_draws(card)

def stand():
    global PLAYER_STOPPED
    PLAYER_STOPPED = True

def double_down():
    global PLAYER_STOPPED
    card = draw_card()
    player_draws(card)
    PLAYER_STOPPED = True

def payout(amount):
    PLAYER_BALANCE += amount

def quit():
    global GAME_OVER, PLAY_AGAIN
    GAME_OVER = True
    PLAY_AGAIN = False
    print(STRINGS_DICTIONARY.goodbye_message)

def get_bet():
    bet = input(STRINGS_DICTIONARY.how_much_bet)

    if bet == 'QUIT':
        stop_game()
        return

    while not is_valid_bet(bet):
        bet = input(STRINGS_DICTIONARY.invalid_bet_input)

    while int(bet) > PLAYER_BALANCE:
        bet = input(STRINGS_DICTIONARY.low_balance)

    return bet

def is_valid_bet(bet):
    if not bet.isdigit():
        return False

    if not MIN_BET <= int(bet) <= MAX_BET:
        return False

    return True

def is_valid_player_move(move):
    valid_inputs = ['h', 's', 'd']
    if move not in valid_inputs:
        return False

    return True

def reset_game():
    global PLAYER_CARDS, PLAYER_STOPPED
    global DEALER_CARDS, DEALER_STOPPED
    global BET
    BET = 0
    PLAYER_STOPPED = False
    DEALER_STOPPED = False
    PLAYER_CARDS = []
    DEALER_CARDS = []

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_player_balance():
    print(STRINGS_DICTIONARY.money.format(PLAYER_BALANCE))

def get_card_front(value, suit):
    return CARDS_FRONT.format(value=value, suit=suit)

def init():
    init_strings_dictionary()
    init_deck()
    init_value_map()

def init_deck():
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
    face_cards = ['J', 'Q', 'K', 'A']
    numeric_cards = [str(value) for value in range(MIN_CARD_VALUE, MAX_CARD_VALUE + 1)]
    card_values = numeric_cards + face_cards
    for suit in suits:
        for value in card_values:
            card = (value, suit)
            DECK.append(card)

def init_value_map():
    for value in range(MIN_CARD_VALUE, MAX_CARD_VALUE + 1):
        CARD_VALUE_MAP[str(value)] = value

    for face in ['J', 'Q', 'K']:
        CARD_VALUE_MAP[face] = 10

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Blackjack

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly once more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.'''

    STRINGS_DICTIONARY.card_back = '''
     ---
    |###|
    |###|
    |###|
     ---
    '''
    STRINGS_DICTIONARY.card_front = '''
     ___
    |{value}  |
    | {suit} |
    |  {value}|
     ---
    '''
    STRINGS_DICTIONARY.money = '''
    Money: {}'''.format(PLAYER_BALANCE)
    STRINGS_DICTIONARY.bet = '''
    Bet: {}'''
    STRINGS_DICTIONARY.player = '''
    PLAYER: {}'''
    STRINGS_DICTIONARY.dealer = '''
    DEALER: {}'''
    STRINGS_DICTIONARY.how_much_bet = '''
    How much do you bet? ({min_bet}-{max_bet}, or QUIT)
    '''.format(min_bet=MIN_BET, max_bet=MAX_BET)
    STRINGS_DICTIONARY.invalid_bet_input = '''
    Please enter amount between {min_bet} and {max_bet} or \'QUIT\' to end the game
    '''.format(min_bet=MIN_BET, max_bet=MAX_BET)
    STRINGS_DICTIONARY.low_balance = '''
    This amount is bigger than your balance. Please enter amount that doesn\'t exceed {}:
    '''.format(PLAYER_BALANCE)
    STRINGS_DICTIONARY.money = '''
    Money: {}'''
    STRINGS_DICTIONARY.hit_stand_double = '''
    (H)it, (S)tand, (D)ouble down? '''
    STRINGS_DICTIONARY.you_drew = '''
    You drew a {}.'''
    STRINGS_DICTIONARY.you_won = '''
    You won ${}!'''

    STRINGS_DICTIONARY.goodbye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''


class StringsDictionary:
    pass

main()
