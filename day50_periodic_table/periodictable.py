QUIT = 'QUIT'

def main():
    init()
    show_intro_message()

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.enter_symbol)
    if not is_valid_user_input(user_input):
        return get_user_input()

    return user_input.upper()

def is_valid_user_input(user_input):
    pass

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Periodic Table of Elements

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Displays atomic information for all the elements.'''
    STRINGS_DICTIONARY.enter_symbol = '''
    Enter a symbol or atomic number to examine, or QUIT to quit: '''
    STRINGS_DICTIONARY.table = '''
                   Periodic Table of Elements
       01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18
     1 H                                                  He
     2 Li Be                               B  C  N  O  F  Ne
     3 Na Mg                               Al Si P  S  Cl Ar
     4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
     5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
     6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
     7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

             Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
             Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr'''
class StringsDictionary:
    pass

main()
