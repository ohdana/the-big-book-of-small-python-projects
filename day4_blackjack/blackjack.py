from random import choices

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
MIN_VALUE = 2
MAX_VALUE = 10
VALUE_MAP = {}
WINNING_VALUE = 21
PLAY_AGAIN = True
GAME_OVER = False
INITIAL_PLAYER_BALANCE = 5000
PLAYER_BALANCE = INITIAL_PLAYER_BALANCE
MIN_BET = 1
MAX_BET = 5000
MAX_DEALER_TOTAL = 17
BET = 0
CARDS_BACK = '''
 ---
|###|
|###|
|###|
 ---
'''
CARDS_FRONT = '''
 ___
|{value}  |
| {suit} |
|  {value}|
 ---
'''
DECK = []
PLAYER_CARDS = []
DEALER_CARDS = []
PLAYER_STOPPED = False
DEALER_STOPPED = False

def get_card_front(value, suit):
    return CARDS_FRONT.format(value=value, suit=suit)

def main():
    init()
    #show_intro_message()

    play()

def player_move():
    move = input(STRINGS_DICTIONARY.hit_stand_double)
    return move.lower()

def is_valid_move(move):
    valid_inputs = ['h', 'hit', 's', 'stand', 'd', 'double down']
    if move not in valid_inputs:
        return False

    return True

def play():
    global GAME_OVER
    start_new_game()
    while not GAME_OVER:
        move = player_move()
        while not is_valid_move(move):
            move = player_move()

        if move == 'h':
            hit()
        elif move == 's':
            stand()
        elif move == 'd':
            double_down()
        calculate_results()

        if not DEALER_STOPPED:
            dealer_move()
            calculate_results()

        show_round_results()

def dealer_move():
    global DEALER_STOPPED, DEALER_CARDS
    if DEALER_STOPPED:
        return

    dealer_sums = get_sum(DEALER_CARDS)
    if MAX_DEALER_TOTAL in dealer_sums:
        DEALER_STOPPED = True

    card = draw_card()
    DEALER_CARDS.append(card)

def calculate_results():
    global DEALER_STOPPED
    dealer_sums = get_sum(DEALER_CARDS)
    player_sums = get_sum(PLAYER_CARDS)

    dealer_stops = max(dealer_sums) >= 17
    if dealer_stops:
        DEALER_STOPPED = True

    got_21_dealer = WINNING_VALUE in dealer_sums
    got_21_player = WINNING_VALUE in player_sums

    if PLAYER_STOPPED and DEALER_STOPPED:
        player_best = max([sum for sum in player_sums if sum <= 21])
        dealer_best = max([sum for sum in dealer_sums if sum <= 21])

        if player_best == dealer_best:
            tie()
        elif player_best > dealer_best:
            player_won()
        else:
            player_lost()
    elif got_21_dealer and got_21_player:
        tie()
    elif got_21_dealer:
        player_lost()
    elif got_21_player:
        player_won()

    went_above_dealer = all(sum > WINNING_VALUE for sum in dealer_sums)
    went_above_player = all(sum > WINNING_VALUE for sum in player_sums)
    if went_above_dealer:
        player_won()
    elif went_above_player:
        player_lost()
def stop_game():
    global GAME_OVER, PLAYER_STOPPED, DEALER_STOPPED
    GAME_OVER = True
    PLAYER_STOPPED = True
    DEALER_STOPPED = True

def tie():
    stop_game()
    print('Tie')
def player_won():
    stop_game()
    print('Player wins')
def player_lost():
    stop_game()
    print('Player lost')

def start_new_game():
    global BET, PLAYER_CARDS, DEALER_CARDS, PLAYER_BALANCE
    print(STRINGS_DICTIONARY.money.format(PLAYER_BALANCE))
    bet = get_bet()

    if not bet:
        return

    print(STRINGS_DICTIONARY.bet.format(bet))
    BET += int(bet)
    PLAYER_CARDS += [draw_card(), draw_card()]
    DEALER_CARDS += [draw_card(), draw_card()]
    calculate_results()
    show_round_results()

def get_sum_string(potential_sums):
    return ' or '.join(str(sum) for sum in potential_sums)

def show_round_results():
    dealer_sum = get_sum(DEALER_CARDS)
    print(STRINGS_DICTIONARY.dealer.format(get_sum_string(dealer_sum)))
    show_hand(DEALER_CARDS)

    player_sum = get_sum(PLAYER_CARDS)
    print(STRINGS_DICTIONARY.player.format(get_sum_string(player_sum)))
    show_hand(PLAYER_CARDS)

def show_hand(cards):
    for card in cards:
        print(card)

def draw_card():
    return choices(DECK, k=1)[0]

def get_sum(cards):
    cards_without_aces = [card for card in cards if card[0] != 'A']
    sum_without_aces = sum([VALUE_MAP[card[0]] for card in cards_without_aces])

    n_of_aces = len(cards) - len(cards_without_aces)
    if n_of_aces == 0:
        return [sum_without_aces]

    possible_sums = []
    for n in range(n_of_aces + 1):
        low_ace_value = 1
        high_ace_value = 11

        possible_aces_sum = low_ace_value * n + high_ace_value * (n_of_aces - n)
        possible_sums.append(sum_without_aces + possible_aces_sum)
        n -= 1

    if len(possible_sums) > 1:
        possible_sums = [x for x in possible_sums if x <= 21]
    return possible_sums

def quit():
    PLAY_AGAIN = False
    print(STRINGS_DICTIONARY.goodbye_message)

def hit():
    card = draw_card()
    PLAYER_CARDS.append(card)
    print(STRINGS_DICTIONARY.you_drew.format(card))

def stand():
    global PLAYER_STOPPED
    PLAYER_STOPPED = True

def double_down():
    global PLAYER_STOPPED
    card = draw_card()
    PLAYER_CARDS.append(card)
    print(STRINGS_DICTIONARY.you_drew.format(card))
    PLAYER_STOPPED = True

def payout(amount):
    PLAYER_BALANCE += amount

def is_valid_bet(bet):
    if not bet.isdigit():
        return False

    if not MIN_BET <= int(bet) <= MAX_BET:
        return False

    return True

def get_bet():
    bet = input(STRINGS_DICTIONARY.how_much_bet)

    if bet == 'QUIT':
        stop_game()
        quit()
        return

    while not is_valid_bet(bet):
        bet = input(STRINGS_DICTIONARY.invalid_bet_input)

    while int(bet) > PLAYER_BALANCE:
        bet = input(STRINGS_DICTIONARY.low_balance)

    return bet

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()
    init_deck()
    init_value_map()

def init_deck():
    global DECK
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
    values = [str(value) for value in range(MIN_VALUE, MAX_VALUE + 1)] + ['J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            card = (value, suit)
            DECK.append(card)

def init_value_map():
    for value in range(MIN_VALUE, MAX_VALUE + 1):
        VALUE_MAP[str(value)] = value

    for face in ['J', 'Q', 'K']:
        VALUE_MAP[face] = 10

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


class StringsDictionary:
    pass

main()
