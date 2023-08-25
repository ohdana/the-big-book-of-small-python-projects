import random
from words_loader import load_words

GAP_CHAR = ' '
YES, NO = 'Y', 'N'
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
INITIAL_N_OF_TRIES = 4
MIN_MEMORY_ADDRESS_DEC = 1
MAX_MEMORY_ADDRESS_DEC = 100
MAX_MEMORY_CELLS_TO_DISPLAY = 16
MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 9
GAME_OVER = None
TRIES_LEFT = None

def main():
    init()
    show_intro_message()
    play_again = True
    while play_again:
        play()
        play_again = ask_if_play_again()

    say_bye()

def play():
    reset_game()
    password, password_options = get_password_and_options()
    show_computer_memory(password_options)
    while not GAME_OVER:
        try_guess_password(password)
        if not GAME_OVER and ran_out_of_tries():
            out_of_tries(password)
            break

def try_guess_password(password):
    user_input = get_user_input()
    set_tries(TRIES_LEFT - 1)
    if guessed_password(user_input, password):
        access_granted()
    else:
        n_of_correct_chars = get_n_of_correct_chars(password, user_input)
        access_denied(n_of_correct_chars, len(password))

def ran_out_of_tries():
    return TRIES_LEFT <= 0

def game_over():
    set_game_over(True)

def reset_game():
    set_game_over(False)
    set_tries(INITIAL_N_OF_TRIES)

def guessed_password(guess, password):
    return guess.upper() == password.upper()

def get_user_input():
    print(STRINGS_DICTIONARY.enter_password.format(TRIES_LEFT))
    user_input = input(STRINGS_DICTIONARY.input)

    return user_input

def get_password_and_options():
    password_length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    password, password_options = generate_password_options(password_length)
    allocate_password_randomly(password, password_options)

    return password, password_options

def allocate_password_randomly(password, password_options):
    random_index = random.randint(0, len(password_options) - 1)
    password_options[0], password_options[random_index] = password_options[random_index], password_options[0]

def generate_password_options(password_length):
    words = load_words(password_length)
    password = random.choice(words)
    n_of_options = random.randint(MAX_MEMORY_CELLS_TO_DISPLAY // 3, MAX_MEMORY_CELLS_TO_DISPLAY // 2)
    password_options = [password]
    while n_of_options > 0:
        option = find_option(words, password)
        if option in password_options:
            continue
        password_options.append(option)
        n_of_options -= 1

    return password, password_options

def find_option(words, password):
    n_of_words = len(words)
    option = None
    index = random.randint(0, n_of_words)
    while index < len(words):
        word = words[index]
        if can_be_option(word, password):
            option = word
            break
        index += 1

    if not option:
        return find_option(words, password)

    return option

def can_be_option(word, password):
    common_chars_counter = 0
    for i in range(len(password)):
        if word[i] == password[i]:
            common_chars_counter += 1

    return common_chars_counter > 1

def show_computer_memory(password_options):
    print(STRINGS_DICTIONARY.find_password)
    computer_memory = generate_computer_memory(password_options)
    print(computer_memory)

def generate_computer_memory(password_options):
    polluted_password_options = pollute_password_options(password_options)
    computer_memory_lines = []
    n_of_lines = len(polluted_password_options)
    for i in range(n_of_lines // 2):
        one_line_pair = [polluted_password_options[i], polluted_password_options[i + n_of_lines // 2]]
        line = (GAP_CHAR * 3).join(one_line_pair)
        computer_memory_lines.append(line)

    return '\n'.join(computer_memory_lines)

def pollute_password_options(password_options):
    result = []
    prefix_dec = random.randint(MIN_MEMORY_ADDRESS_DEC, MAX_MEMORY_ADDRESS_DEC)
    options_indices_in_result = get_random_indices(MAX_MEMORY_CELLS_TO_DISPLAY, len(password_options))
    cell_length = generate_cell_content_length(password_options[0])
    for i in range(MAX_MEMORY_CELLS_TO_DISPLAY):
        cell_contents = generate_garbage_string(cell_length)
        if i in options_indices_in_result:
            option = password_options.pop()
            cell_contents = get_polluted_password_option(cell_contents, option)
        result.append(hex(prefix_dec) + GAP_CHAR * 2 + cell_contents)
        prefix_dec += 1

    return result

def get_random_indices(array_length, n_of_indices):
    indices = []
    while len(indices) < n_of_indices:
        index = random.randint(0, array_length)
        if index not in indices:
            indices.append(index)

    return indices

def get_polluted_password_option(cell_contents, option):
    cell_content_length = len(cell_contents)
    start_index = random.randint(0, cell_content_length - len(option) - 1)
    result = cell_contents[:start_index] + option.upper() + cell_contents[(start_index + len(option)):]

    return ''.join(result)

def generate_garbage_string(length):
    return ''.join(random.choices(GARBAGE_CHARS, k=length))

def generate_cell_content_length(password):
    return len(password) * 2 + 1

def access_granted():
    print(STRINGS_DICTIONARY.access_granted)
    game_over()

def access_denied(n_of_correct_chars, total_n_of_chars):
    print(STRINGS_DICTIONARY.access_denied.format(n_of_correct_chars, total_n_of_chars))

def out_of_tries(password):
    print(STRINGS_DICTIONARY.out_of_tries.format(password.upper()))
    game_over()

def get_n_of_correct_chars(password, user_input):
    counter = 0
    if len(user_input) != len(password):
        print(STRINGS_DICTIONARY.password_length.format(len(password)))
        return counter

    for i in range(len(password)):
        if password[i] == user_input[i]:
            counter += 1

    return counter

def ask_if_play_again():
    answer = input(STRINGS_DICTIONARY.play_again)
    if not is_valid_y_n(answer):
        return ask_if_play_again()

    return answer.upper() == YES

def is_valid_y_n(answer):
    return answer.upper() in [YES, NO]

def set_game_over(value):
    global GAME_OVER
    GAME_OVER = value

def set_tries(value):
    global TRIES_LEFT
    TRIES_LEFT = value

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Hacking Minigame

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    The hacking mini-game from "Fallout 3". Find out which seven-letter
    word is the password by using clues each guess gives you.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.find_password = '''
    Find the password in the computer's memory: '''
    STRINGS_DICTIONARY.enter_password = '''
    Enter password: ({} tries remaining)'''
    STRINGS_DICTIONARY.input = '''
    >'''
    STRINGS_DICTIONARY.access_denied = '''
    Access Denied ({}/{} correct)'''
    STRINGS_DICTIONARY.access_granted = '''
    A C C E S S   G R A N T E D'''
    STRINGS_DICTIONARY.out_of_tries = '''
    Out of tries. Secret password was: {}.'''
    STRINGS_DICTIONARY.password_length = '''
    Password length must be {}.'''

class StringsDictionary:
    pass

main()
