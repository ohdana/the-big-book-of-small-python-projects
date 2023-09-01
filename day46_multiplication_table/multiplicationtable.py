MAX_NUMBER = 12

def main():
    init()
    show_intro_message()
    show_table()

def show_table():
    show_headers()
    show_products()

def show_headers():
    print('    |   0   1   2   3   4   5   6   7   8   9  10  11  12')
    print('----+----------------------------------------------------')

def show_products():
    for i in range(MAX_NUMBER + 1):
        new_line = get_new_products_line(i)
        print(new_line)

def get_new_products_line(number):
    line = get_str(number) + '|'
    for i in range(MAX_NUMBER + 1):
        line += '{}'.format(get_str(number * i))

    return line

def get_str(number):
    gap = (4 - len(str(number))) * ' '

    return '{}{}'.format(gap, number)

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
