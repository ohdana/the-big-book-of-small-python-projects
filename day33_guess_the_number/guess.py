import random

YES, NO = "Y", "N"
MIN_NUMBER, MAX_NUMBER = 1, 100
INITIAL_N_OF_GUESSES = 10


def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()
    say_bye()


def play():
    secret_number = generate_secret_number()
    guesses_left = INITIAL_N_OF_GUESSES
    print(STRINGS_DICTIONARY.i_am_thinking_of_a_number)
    while guesses_left > 0:
        guess = get_user_input(guesses_left)
        if is_correct_guess(secret_number, guess):
            player_wins()
            break
        show_clue(secret_number, guess)
        guesses_left -= 1

    if guesses_left == 0:
        player_ran_out_of_moves(secret_number)


def show_clue(secret_number, guess):
    if secret_number > guess:
        print(STRINGS_DICTIONARY.too_low)
    else:
        print(STRINGS_DICTIONARY.too_high)


def player_wins():
    print(STRINGS_DICTIONARY.you_guessed)


def player_ran_out_of_moves(secret_number):
    print(STRINGS_DICTIONARY.ran_out_of_moves.format(secret_number))


def get_user_input(guesses_left):
    user_input = input(STRINGS_DICTIONARY.take_a_guess.format(guesses_left))

    if not is_valid_user_input(user_input):
        return get_user_input(guesses_left)

    return int(user_input)


def is_valid_user_input(user_input):
    if not user_input.isdigit():
        return False

    if MIN_NUMBER <= int(user_input) <= MAX_NUMBER:
        return True

    return False


def is_correct_guess(secret_number, guess):
    return secret_number == guess


def generate_secret_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES


def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]


def say_bye():
    print(STRINGS_DICTIONARY.bye)


def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)


def init():
    init_strings_dictionary()


##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = """
    Guess the Number

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Try to guess the secret number based on hints."""
    STRINGS_DICTIONARY.i_am_thinking_of_a_number = """
    I am thinking of a number between {} and {}.""".format(
        MIN_NUMBER, MAX_NUMBER
    )
    STRINGS_DICTIONARY.take_a_guess = """
    You have {} guesses left. Take a guess: """
    STRINGS_DICTIONARY.too_high = """
    Your guess is too high."""
    STRINGS_DICTIONARY.too_low = """
    Your guess is too low."""
    STRINGS_DICTIONARY.you_guessed = """
    Yay! You guessed my number!"""
    STRINGS_DICTIONARY.ran_out_of_moves = """
    You ran out of moves. My number was {}."""
    STRINGS_DICTIONARY.play_again = """
    Play again? y/n: """
    STRINGS_DICTIONARY.bye = """
    Bye!"""


class StringsDictionary:
    pass


main()
