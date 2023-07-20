def main():
    init()
    show_intro_message()
    word = get_word()
    show_bitmap(word)

def init():
    init_strings_dictionary()

def get_word():
    return input(STRINGS_DICTIONARY.enter_the_message)

def show_bitmap(word):
    original_bitmap = STRINGS_DICTIONARY.bitmap
    custom_bitmap = ''
    for i in range(len(original_bitmap)):
        if original_bitmap[i] == '*':
            custom_bitmap += word[i % len(word)]
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
