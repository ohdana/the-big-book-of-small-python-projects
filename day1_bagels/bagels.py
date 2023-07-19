import random

NUM_DIGITS = 3
MAX_GUESSES = 10
SECRET_NUMBER = ''

def main():
    init_strings_dictionary()
    show_intro_message()

    while True:
        show_start_game_message()
        generate_secret_number()
        play_game()

        play_again = ask_play_again()
        if not play_again:
            show_goodbye_message()
            break

def play_game():
    current_guess_number = 1
    ran_out_of_guesses = False

    while not ran_out_of_guesses:
        guess = take_guess(current_guess_number)

        if guess == SECRET_NUMBER:
            show_winning_message()
            break

        current_guess_number += 1
        show_clues(guess)

        ran_out_of_guesses = current_guess_number > MAX_GUESSES

    if ran_out_of_guesses:
        show_losing_message()

def show_clues(guess):
    clues = get_clues(guess)

    if not clues:
        print(STRINGS_DICTIONARY.bagels)
    else:
        print(' '.join(sorted(clues)))

def get_clues(guess):
    clues = []

    for i in range(len(SECRET_NUMBER)):
        if guess[i] == SECRET_NUMBER[i]:
            clues.append(STRINGS_DICTIONARY.fermi)
        elif guess[i] in SECRET_NUMBER:
            clues.append(STRINGS_DICTIONARY.pico)

    return clues

def ask_play_again():
    play_again = input(STRINGS_DICTIONARY.play_again_message)

    while play_again not in ['y', 'n']:
        play_again = input(STRINGS_DICTIONARY.invalid_play_again_input)

    return play_again == 'y'

def take_guess(guess_number):
    guess = input(STRINGS_DICTIONARY.guess_number.format(guess_number))

    while not is_valid_guess(guess):
        guess = input(STRINGS_DICTIONARY.invalid_guess)

    return guess

def is_valid_guess(guess):
    if len(guess) != NUM_DIGITS:
        return False

    if not guess.isdigit():
        return False

    return True

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_start_game_message():
    print(STRINGS_DICTIONARY.start_game_message)

def show_winning_message():
    print(STRINGS_DICTIONARY.winning_message)

def show_losing_message():
    print(STRINGS_DICTIONARY.losing_message)

def show_goodbye_message():
    print(STRINGS_DICTIONARY.goodbye_message)

def generate_secret_number():
    global SECRET_NUMBER
    digits = '0123456789'
    random_index = -1
    used_indices = [random_index]

    for i in range(NUM_DIGITS):
        while random_index in used_indices:
            random_index = random.randint(0, len(digits) - 1)

        SECRET_NUMBER += digits[random_index]
        used_indices.append(random_index)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Bagels, a deductive logic game.

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico
    '''.format(NUM_DIGITS)

    STRINGS_DICTIONARY.start_game_message = '''
    I have thought up a number.
    You have {} guesses to get it.'''.format(MAX_GUESSES)

    STRINGS_DICTIONARY.winning_message = '''
    You got it!'''
    STRINGS_DICTIONARY.losing_message = '''
    You ran out of guesses. The number was {}.'''.format(SECRET_NUMBER)
    STRINGS_DICTIONARY.goodbye_message = '''
    Thanks for playing!'''
    STRINGS_DICTIONARY.play_again_message = '''
    Do you want to play again? y/n: '''
    STRINGS_DICTIONARY.invalid_play_again_input = '''
    Please use \'y\' for \'Yes\' and \'n\' for \'No\': '''
    STRINGS_DICTIONARY.fermi = 'Fermi'
    STRINGS_DICTIONARY.pico = 'Pico'
    STRINGS_DICTIONARY.bagels = 'Bagels!'
    STRINGS_DICTIONARY.guess_number = '''
    Guess #{}: '''
    STRINGS_DICTIONARY.invalid_guess = '''
    That doesn\'t look like a valid {}-digit number!
    Please take another guess: '''.format(NUM_DIGITS)

class StringsDictionary:
    pass

main()

