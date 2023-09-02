import time
INITIAL_N_OF_BOTTLES = 99
PAUSE_BETWEEN_STANZA = 0.1

def main():
    init()
    show_intro_message()
    sing_song()

def sing_song():
    n_of_bottles = INITIAL_N_OF_BOTTLES
    while n_of_bottles > 0:
        sing_stanza(n_of_bottles)
        n_of_bottles -= 1
        time.sleep(PAUSE_BETWEEN_STANZA)

def sing_stanza(n_of_bottles):
    is_last_stanza = n_of_bottles == 1
    if is_last_stanza:
        print(STRINGS_DICTIONARY.last_stanza)
        return

    print(STRINGS_DICTIONARY.regular_stanza.format(n_of_bottles, n_of_bottles, n_of_bottles - 1))

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Ninety-Nine Bottles

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Print the full lyrics to one of the longest songs ever!'''
    STRINGS_DICTIONARY.regular_stanza = '''
    {} bottles of milk on the wall,
    {} bottles of milk,
    Take one down, pass it around,
    {} bottles of milk on the wall!'''
    STRINGS_DICTIONARY.last_stanza = '''
    1 bottle of milk on the wall,
    1 bottle of milk,
    Take one down, pass it around,
    No more bottles of milk on the wall!'''

class StringsDictionary:
    pass

main()
