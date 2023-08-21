import random

GAME_OVER = None
WORD_SKELETON_CHAR = '_'
GAP_CHAR = ' '
YES, NO = 'Y', 'N'
TRIES_LEFT = None
CATEGORY_WORDS_MAP = { 'Animals': 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()}

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
    word, word_skeleton = get_secret_word()
    missed_letters = []
    while not GAME_OVER:
        show_missed_letters(missed_letters)
        show_word_skeleton(word_skeleton)
        show_hangman(len(missed_letters))
        letter = take_guess(word, word_skeleton, missed_letters)
        if letter in word:
            guessed_successfully(letter, word, word_skeleton)
        else:
            guessed_wrong(letter, missed_letters)

        if ran_out_of_tries():
            player_lost(word)
            break

def player_wins(word):
    print(STRINGS_DICTIONARY.you_won.format(word))
    game_over()

def player_lost(word):
    print(STRINGS_DICTIONARY.you_lost.format(word))
    game_over()

def guessed_wrong(letter, missed_letters):
    set_tries_left(TRIES_LEFT - 1)
    if letter not in missed_letters:
        missed_letters.append(letter)

def guessed_successfully(letter, word, word_skeleton):
    word_skeleton = update_word_skeleton(letter, word, word_skeleton)
    if guessed_all_letters(word_skeleton):
        player_wins(word)

def guessed_all_letters(word_skeleton):
    return WORD_SKELETON_CHAR not in word_skeleton

def ran_out_of_tries():
    return TRIES_LEFT <= 0

def update_word_skeleton(letter, word, word_skeleton):
    for i in range(len(word)):
        if word[i] == letter:
            word_skeleton[i] = letter

    return word_skeleton

def show_missed_letters(missed_letters):
    if not missed_letters:
        print(STRINGS_DICTIONARY.no_missed_letters)
    else:
        missed_letters_string = ', '.join(missed_letters)
        print(STRINGS_DICTIONARY.missed_letters.format(missed_letters_string))

def show_word_skeleton(word_skeleton):
    print('''
    {}'''.format(GAP_CHAR.join(word_skeleton)))

def show_hangman(n_of_missed_letters):
    print(STRINGS_DICTIONARY.hangman_stages[n_of_missed_letters])

def get_initial_n_of_tries():
    return len(STRINGS_DICTIONARY.hangman_stages) - 1

def take_guess(word, word_skeleton, missed_letters):
    letter = get_user_input()
    return letter.upper()

def generate_word_skeleton(word):
    return [WORD_SKELETON_CHAR for i in range(len(word))]

def get_category():
    return random.choice(list(CATEGORY_WORDS_MAP))

def get_secret_word():
    category = get_category()
    word = random.choice(CATEGORY_WORDS_MAP[category])
    return word, generate_word_skeleton(word)

def get_user_input():
    print(STRINGS_DICTIONARY.guess_letter)
    user_input = input(STRINGS_DICTIONARY.input)
    if not is_valid_user_input(user_input):
        return get_user_input()

    return user_input

def is_valid_user_input(user_input):
    if len(user_input) != 1:
        return False

    return user_input.isalpha()

def game_over():
    set_game_over(True)

def reset_game():
    set_game_over(False)
    set_tries_left(get_initial_n_of_tries())

def set_tries_left(value):
    global TRIES_LEFT
    TRIES_LEFT = value

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
    Hangman

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Guess the letters to a secret word before the hangman is drawn.'''
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.play_again = '''
    Play again? y/n: '''
    STRINGS_DICTIONARY.category_is = '''
    The category is: {}'''
    STRINGS_DICTIONARY.missed_letters = '''
    Missed letters: {}'''
    STRINGS_DICTIONARY.no_missed_letters = '''
    No missed letters yet.'''
    STRINGS_DICTIONARY.guess_letter = '''
    Guess a letter.'''
    STRINGS_DICTIONARY.you_won = '''
    Yes! The secret word is: {}
    You have won!'''
    STRINGS_DICTIONARY.you_lost = '''
    Oops! The secret word is: {}
    You have lost.'''
    STRINGS_DICTIONARY.input = '''
    >'''
    STRINGS_DICTIONARY.hangman_stages = ['''
     +--+
     |  |
        |
        |
        |
        |
     ====''', '''
     +--+
     |  |
     O  |
        |
        |
        |
     ====''', '''
     +--+
     |  |
     O  |
     |  |
        |
        |
     ====''', '''
     +--+
     |  |
     O  |
    /|  |
        |
        |
     ====''', '''
     +--+
     |  |
     O  |
    /|\ |
        |
        |
     ====''', '''
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
     ====''', '''
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
     ====''']

class StringsDictionary:
    pass

main()
