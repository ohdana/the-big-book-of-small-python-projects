from progressbar import ProgressBar
import random, time

PAUSE = 0.2
BAR = None
BYTES_TO_DOWNLOAD = 4098
BYTES_DOWNLOADED = 0

def main():
    init()
    show_intro_message()
    simulate()

def simulate():
    while not is_download_completed():
        download_chunk()
        show_progress()
    show_download_completed_message()

def show_progress():
    bytes_info = '{}/{}'.format(BYTES_DOWNLOADED, BYTES_TO_DOWNLOAD)
    print(BAR.build(), bytes_info)

def download_chunk():
    simulate_delay()
    chunk_size = get_download_chunk_size()
    set_bytes_downloaded(BYTES_DOWNLOADED + chunk_size)
    bytes_downloaded_percentage = get_bytes_downloaded_percentage()
    BAR.set_progress(bytes_downloaded_percentage)

def get_bytes_downloaded_percentage():
    return round(BYTES_DOWNLOADED * 100 / BYTES_TO_DOWNLOAD, 2)

def set_bytes_downloaded(new_value):
    global BYTES_DOWNLOADED
    BYTES_DOWNLOADED = new_value if new_value < BYTES_TO_DOWNLOAD else BYTES_TO_DOWNLOAD

def simulate_delay():
    time.sleep(PAUSE)

def get_download_chunk_size():
    return random.randint(1, 100)

def is_download_completed():
    return BYTES_DOWNLOADED == BYTES_TO_DOWNLOAD

def show_download_completed_message():
    print(STRINGS_DICTIONARY.download_completed)

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def init_bar():
    global BAR
    BAR = ProgressBar()

def init():
    init_strings_dictionary()
    init_bar()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Progress Bar Simulation

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A sample progress bar animation that can be used in other programs.'''
    STRINGS_DICTIONARY.download_completed = '''
    Download completed!'''

class StringsDictionary:
    pass

main()

