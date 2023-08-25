from canvas import Canvas

WIDTH = 50
HEIGHT = 30
N_OF_ANTS = 10
TICK_DURATION = 0.1

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    canvas = Canvas(WIDTH, HEIGHT, N_OF_ANTS)
    while True:
        canvas.show_canvas()
        canvas.tick()
        time.sleep(TICK_DURATION)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Langton's Ant

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A cellular automata animation.
    More info: https://en.wikipedia.org/wiki/Langton%27s_ant'''

class StringsDictionary:
    pass

main()

