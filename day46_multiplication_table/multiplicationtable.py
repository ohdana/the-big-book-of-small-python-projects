from tablebuilder import TableBuilder
MAX_NUMBER = 12

def main():
    init()
    show_intro_message()
    show_table()

def show_table():
    tablebuilder = TableBuilder(MAX_NUMBER)
    tablebuilder.show()

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Multiplication Table

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Print a multiplication table.'''

class StringsDictionary:
    pass

main()
