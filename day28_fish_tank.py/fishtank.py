import random, time

from tank import Tank
from kelp import Kelp
from bubbler import Bubbler

N_OF_KELPS = 3
N_OF_BUBBLERS = 2
CANVAS_WIDTH, CANVAS_HEIGHT = 100, 30

def main():
    init()
    show_intro_message()
    run_animation()

def run_animation():
    tank = generate_tank()
    add_bubblers_to_tank(tank)
    add_kelps_to_tank(tank)
    while True:
        tank.tick()
        tank.show()
        time.sleep(0.5)

def add_bubblers_to_tank(tank):
    bubblers = generate_bubblers()
    for bubbler in bubblers:
        tank.add_bubbler(bubbler)

def add_kelps_to_tank(tank):
    kelps = generate_kelps()
    for kelp in kelps:
        tank.add_kelp(kelp)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def generate_tank():
    return Tank(CANVAS_WIDTH, CANVAS_HEIGHT)

def generate_bubblers():
    bubblers = []
    for i in range(N_OF_BUBBLERS):
        bubbler = generate_bubbler()
        bubblers.append(bubbler)

    return bubblers

def generate_bubbler():
    return Bubbler(CANVAS_HEIGHT)

def generate_kelps():
    kelps = []
    for i in range(N_OF_KELPS):
        kelp = generate_kelp()
        kelps.append(kelp)
    return kelps

def generate_kelp():
    return Kelp(CANVAS_HEIGHT)

def init():
    init_strings_dictionary()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Fish Tank

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A peaceful animation of a fish tank.'''

class StringsDictionary:
    pass

main()
