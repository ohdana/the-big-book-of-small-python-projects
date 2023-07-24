import pygame

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LOGO_FONT = 'arial'
LOGO_FONT_SIZE = 25
LOGO_TEXT = 'DVD'
LOGO_SPEED = [1, 1]

def main():
    init()
    screen = get_screen()
    bounce_logo(screen)

def bounce_logo(screen):
    logo = pygame.draw.circle(surface=screen, color=BLACK, center=[LOGO_FONT_SIZE, LOGO_FONT_SIZE], radius=LOGO_FONT_SIZE)
    font = pygame.font.SysFont(LOGO_FONT, LOGO_FONT_SIZE)
    text = font.render(LOGO_TEXT, True, WHITE)

    while True:
        screen.fill(BLACK)
        logo = logo.move(LOGO_SPEED)
        update_direction(logo)
        redraw_logo(screen, logo, text)


def update_direction(logo):
    if logo.left <= 0 or logo.right >= WINDOW_WIDTH:
        LOGO_SPEED[0] = -LOGO_SPEED[0]
    if logo.top <= 0 or logo.bottom - LOGO_FONT_SIZE >= WINDOW_HEIGHT:
        LOGO_SPEED[1] = -LOGO_SPEED[1]

def redraw_logo(screen, logo, text):
    pygame.draw.circle(surface=screen, color=BLACK, center=logo.center, radius=LOGO_FONT_SIZE)
    screen.blit(text, (logo.center[0] - LOGO_FONT_SIZE, logo.center[1] - LOGO_FONT_SIZE))
    pygame.display.update()
    pygame.display.flip()

def get_screen():
    screen_res = (WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_caption(STRINGS_DICTIONARY.window_title)

    return pygame.display.set_mode(screen_res)

def init():
    init_strings_dictionary()
    pygame.init()

##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Bouncing DVD Logo

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    A bouncing DVD logo animation. You have to be 'of a certain age' to
    appreciate this. Press Ctrl-C to stop.

    NOTE: Do not resize the terminal window while this program is running.
    '''
    STRINGS_DICTIONARY.window_title = 'Bouncing DVD Logo'

class StringsDictionary:
    pass

main()
