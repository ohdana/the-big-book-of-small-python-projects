import time, random
INITIAL_N_OF_BOTTLES = 99
PAUSE_BETWEEN_STANZA = 0.1
MUTATION_TYPES = None
AVAILABLE_CHARS = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+"*%&/()=?`;:-_.,!'

def main():
    init()
    show_intro_message()
    sing_song()

def sing_song():
    n_of_bottles = INITIAL_N_OF_BOTTLES
    stanza = STRINGS_DICTIONARY.regular_stanza
    while n_of_bottles > 0:
        sing_stanza(n_of_bottles, stanza)
        stanza = mutate_stanza(stanza)
        n_of_bottles -= 1
        time.sleep(PAUSE_BETWEEN_STANZA)

def mutate_stanza(stanza):
    mutation = get_random_mutation()
    return mutation(stanza)

def sing_stanza(n_of_bottles, stanza):
    is_last_stanza = n_of_bottles == 1
    if is_last_stanza:
        stanza = replace_last_line_for_last_stanza(stanza)

    print(stanza.format(n_of_bottles, n_of_bottles, n_of_bottles - 1))

def replace_last_line_for_last_stanza(stanza):
    lines = stanza.split('\n')
    return '\n'.join(lines[:-1] + [STRINGS_DICTIONARY.last_stanza_last_line])

def duplicate_random_char_in_string(string):
    index = get_random_index(string)
    return duplicate_char_in_string(string, index)

def remove_random_char_in_string(string):
    index = get_random_index(string)
    return remove_char_in_string(string, index)

def add_random_char_in_string(string):
    index = get_random_index(string)
    random_char = random.choice(AVAILABLE_CHARS)
    return string[:index] + random_char + string[index:]

def uppercase_random_char_in_string(string):
    index = get_random_index(string)
    return uppercase_char_in_string(string, index)

def lowercase_random_char_in_string(string):
    index = get_random_index(string)
    return lowercase_char_in_string(string, index)

def uppercase_char_in_string(string, index):
    return string[:index] + string[index].upper() + string[index+1:]

def lowercase_char_in_string(string, index):
    return string[:index] + string[index].lower() + string[index+1:]

def duplicate_char_in_string(string, index):
    return string[:index+1] + string[index:]

def remove_char_in_string(string, index):
    return string[:index] + string[index+1:]

def get_random_index(string):
    random_index = random.randint(0, len(string) - 1)
    if string[random_index] in '{}\n':
        return get_random_index(string)

    return random_index

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def get_random_mutation():
    return random.choice(MUTATION_TYPES)

def init_mutation_types():
    global MUTATION_TYPES
    MUTATION_TYPES = [duplicate_random_char_in_string, remove_random_char_in_string,
    add_random_char_in_string, uppercase_random_char_in_string, lowercase_random_char_in_string]

def init():
    init_strings_dictionary()
    init_mutation_types()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    niNety-nniinE BoOttels of Mlik On teh waLl

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Print the full lyrics to one of the longest songs ever! The song
    gets sillier and sillier with each verse.'''
    STRINGS_DICTIONARY.regular_stanza = '''
    {} bottles of milk on the wall,
    {} bottles of milk,
    Take one down, pass it around,
    {} bottles of milk on the wall!'''
    STRINGS_DICTIONARY.last_stanza_last_line = '''
    No more bottles of milk on the wall!'''

class StringsDictionary:
    pass

main()
