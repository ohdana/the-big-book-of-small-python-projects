import random

MIN_N_OF_HEADLINES = 1
MAX_N_OF_HEADLINES = 1000
MIN_RAND_INT = 5
MAX_RAND_INT = 15
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois',
    'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
    'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
    'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
    'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'Right Now', 'Next Week']
SOCIAL_NETWORKS = ['wobsite', 'blag', 'Facebuk', 'Goggle', 'Tweedie', 'Pastagram']
HEADLINE_TYPES = []

def main():
    init()
    show_intro_message()
    try_again = True

    while try_again:
        n_of_headlines = get_n_of_headlines()
        headlines = generate_headlines(n_of_headlines)
        show_headlines(headlines)
        try_again = prompt_try_again()

    say_bye()

def generate_headlines(n):
    return [generate_headline() for i in range(n)]

def generate_headline():
    return random.choice(HEADLINE_TYPES)()

def generate_are_millenials_killing_headline():
    noun = random.choice(NOUNS)

    return STRINGS_DICTIONARY.are_millenials_killing.format(noun)

def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = noun + 's'
    when = random.choice(WHEN)

    return STRINGS_DICTIONARY.what_you_dont_know.format(noun, plural_noun, when)

def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)

    return STRINGS_DICTIONARY.big_companies_hate_her.format(pronoun, state, noun1, noun2)

def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    place = random.choice(PLACES)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)

    return STRINGS_DICTIONARY.you_wont_believe.format(state, noun, pronoun, place)

def generate_dont_want_you_to_know_headline():
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    plural_noun1 = noun1 + 's'
    plural_noun2 = noun2 + 's'

    return STRINGS_DICTIONARY.dont_want_you_to_know.format(plural_noun1, plural_noun2)

def generate_gift_idea_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    number = random.randint(MIN_RAND_INT, MAX_RAND_INT)

    return STRINGS_DICTIONARY.gift_idea.format(number, noun, state)

def generate_reasons_why_headline():
    noun = random.choice(NOUNS)
    plural_noun = noun + 's'
    number1 = random.randint(MIN_RAND_INT, MAX_RAND_INT)
    number2 = random.randint(1, number1)
    return STRINGS_DICTIONARY.reasons_why.format(number1, plural_noun, number2)

def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    personal_pronoun = random.choice(PERSONAL_PRONOUNS)
    possesive_pronoun = get_possesive_pronoun(personal_pronoun)

    string_pattern = ''
    if personal_pronoun == 'They':
        string_pattern = STRINGS_DICTIONARY.job_automated_plural
    else:
        string_pattern = STRINGS_DICTIONARY.job_automated_singular

    return string_pattern.format(state, noun, possesive_pronoun, personal_pronoun)

def get_possesive_pronoun(personal_pronoun):
    return POSSESSIVE_PRONOUNS[PERSONAL_PRONOUNS.index(personal_pronoun)]

def get_object_pronoun(personal_pronoun):
    return OBJECT_PRONOUNS[PERSONAL_PRONOUNS.index(personal_pronoun)]

def show_headlines(headlines):
    print(headlines)

def get_n_of_headlines():
    n_of_headlines = input(STRINGS_DICTIONARY.enter_number)

    while not is_valid_n_of_headlines(n_of_headlines):
        n_of_headlines = input(STRINGS_DICTIONARY.invalid_n_of_headlines)

    return int(n_of_headlines)

def prompt_try_again():
    try_again = input(STRINGS_DICTIONARY.try_again)

    while not is_valid_y_n(try_again):
        try_again = input(STRINGS_DICTIONARY.try_again)

    if try_again == 'n':
        return False

    return True

def is_valid_n_of_headlines(n):
    if not n:
        return False

    if not n.isdigit():
        return False

    return MIN_N_OF_HEADLINES <= int(n) <= MAX_N_OF_HEADLINES

def is_valid_y_n(text):
    if not text:
        return False

    return text in ['y', 'n']

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def say_bye():
    print(STRINGS_DICTIONARY.bye)

def populate_headline_types_list():
    HEADLINE_TYPES.append(generate_are_millenials_killing_headline)
    HEADLINE_TYPES.append(generate_what_you_dont_know_headline)
    HEADLINE_TYPES.append(generate_big_companies_hate_her_headline)
    HEADLINE_TYPES.append(generate_you_wont_believe_headline)
    HEADLINE_TYPES.append(generate_dont_want_you_to_know_headline)
    HEADLINE_TYPES.append(generate_gift_idea_headline)
    HEADLINE_TYPES.append(generate_reasons_why_headline)
    HEADLINE_TYPES.append(generate_job_automated_headline)

def init():
    init_strings_dictionary()
    populate_headline_types_list()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Clickbait Headline Generator

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A clickbait headline generator for your soulless content farm website.'''

    STRINGS_DICTIONARY.enter_number = '''
    Enter the number of clickbait headlines to generate: '''
    STRINGS_DICTIONARY.invalid_number = '''
    Please enter a number between {} and {}'''.format(MIN_N_OF_HEADLINES, MAX_N_OF_HEADLINES)
    STRINGS_DICTIONARY.bye = '''
    Bye!'''
    STRINGS_DICTIONARY.try_again = '''
    Try again? y/n: '''
    STRINGS_DICTIONARY.are_millenials_killing = 'Are Millenials Killing The {} Industry?'
    STRINGS_DICTIONARY.what_you_dont_know = 'Without This {}, {} Could Kill You {}'
    STRINGS_DICTIONARY.big_companies_hate_her = 'Big Companies Hate {}! See How {} {} Invented A Cheaper {}'
    STRINGS_DICTIONARY.you_wont_believe = 'You Won\'t Believe What This {} {} Found in {} {}'
    STRINGS_DICTIONARY.dont_want_you_to_know = 'What {} Don\'t Want You To Know About {}'
    STRINGS_DICTIONARY.gift_idea = '{} Gift Ideas To Give Your {} From {} '
    STRINGS_DICTIONARY.reasons_why = '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'
    STRINGS_DICTIONARY.job_automated_plural = 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong'
    STRINGS_DICTIONARY.job_automated_singular = 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong'

class StringsDictionary:
    pass

main()
