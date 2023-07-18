import random

NUM_DIGITS = 3
MAX_GUESSES = 10
SECRET_NUMBER = ''
STRING_FERMI = 'Fermi'
STRING_PICO = 'Pico'
STRING_BAGELS = 'Bagels!'

def main():
    show_intro_message()

    while True:
        set_secret_number()
        show_start_game_message()
        current_guess_number = 1

        while current_guess_number <= MAX_GUESSES:
            guess = take_guess(current_guess_number)

            if guess == SECRET_NUMBER:
                show_winning_message()
                break

            current_guess_number += 1
            show_clues(guess)

        if current_guess_number > MAX_GUESSES:
            print(current_guess_number)
            show_losing_message()

        play_again = ask_play_again()
        if not play_again:
            show_goodbye_message()
            break

def ask_play_again():
    play_again = input('Do you want to play again? y/n: ')

    while play_again not in ['y', 'n']:
        play_again = input('Please use \'y\' for \'Yes\' and \'n\' for \'No\': ')

    return play_again == 'y'

def show_clues(guess):
    clues = []

    for i in range(len(SECRET_NUMBER)):
        if guess[i] == SECRET_NUMBER[i]:
            clues.append(STRING_FERMI)
        elif guess[i] in SECRET_NUMBER:
            clues.append(STRING_PICO)

    if not clues:
        print(STRING_BAGELS)
    else:
        print(' '.join(sorted(clues)))

def show_goodbye_message():
    print('Thanks for playing!')

def show_losing_message():
    print('You ran out of guesses. The number was {}.'.format(SECRET_NUMBER))

def show_winning_message():
    print('You got it!')

def show_intro_message():
    print('''

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
    '''.format(NUM_DIGITS))

def show_start_game_message():
    print('''
    I have thought up a number.
    You have {} guesses to get it.'''.format(MAX_GUESSES))

def take_guess(guess_number):
    guess = input('''
    Guess #{}: '''.format(guess_number))

    while not is_valid_guess(guess):
        guess = input('''
    That doesn\'t look like a valid {}-digit number!
    Please take another guess: '''.format(NUM_DIGITS))

    return guess

def is_valid_guess(guess):
    if len(guess) != NUM_DIGITS:
        return False

    if not guess.isdigit():
        return False

    return True

def set_secret_number():
    secret_number = ''
    digits = '0123456789'
    used_indices = []
    for i in range(NUM_DIGITS):
        index = random.randint(0, len(digits) - 1)

        while index in used_indices:
            index = random.randint(0, len(digits) - 1)

        secret_number += digits[index]
        used_indices.append(index)

    global SECRET_NUMBER
    SECRET_NUMBER = secret_number

main()

