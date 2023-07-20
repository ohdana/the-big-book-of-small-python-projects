def main():
    init()
    show_intro_message()
    get_word()
    show_bitmap()

def init():
    init_strings_dictionary()

def get_word():
    global WORD
    WORD = input(STRINGS_DICTIONARY.enter_the_message)

def show_bitmap():
    original_bitmap = STRINGS_DICTIONARY.bitmap
    custom_bitmap = ''
    for i in range(len(original_bitmap)):
        if original_bitmap[i] in ['.', '*']:
            custom_bitmap += WORD[i % len(WORD)]
            continue

        custom_bitmap += original_bitmap[i]

    print(custom_bitmap)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()
    STRINGS_DICTIONARY.bitmap = """
 ....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ...................................................................."""
    STRINGS_DICTIONARY.intro_message = '''
    Bitmap Message

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana
    '''

    STRINGS_DICTIONARY.enter_the_message = '''
    Enter the message to display with the bitmap: '''

class StringsDictionary:
    pass

main()
