import random, time

MIN_REPLY_PAUSE_DURATION_TACTS = 4
MAX_REPLY_PAUSE_DURATION_TACTS = 12
TACT_DURATION_SECONDS = 0.7
TYPING_PAUSE = 0.1
SLOW_TYPING_PAUSE = 0.2
SPACE_CHAR = ' '
DOT_CHAR = '.'
ASK_ME = 'ASK ME YOUR YES/NO QUESTION.'
REPLIES = [
'LET ME THINK ON THIS...',
'AN INTERESTING QUESTION...',
'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
'YES... NO... MAYBE... I WILL THINK ON IT...',
'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
'I SHALL CONSULT MY VISIONS...',
'YOU MAY WANT TO SIT DOWN FOR THIS...']
I_HAVE_AN_ANSWER = 'I HAVE AN ANSWER...'
ANSWERS = [
'YES, FOR SURE',
'MY ANSWER IS NO',
'ASK ME LATER',
'I AM PROGRAMMED TO SAY YES',
'THE STARS SAY YES, BUT I SAY NO',
'I DUNNO MAYBE',
'FOCUS AND ASK ONCE MORE',
'DOUBTFUL, VERY DOUBTFUL',
'AFFIRMATIVE',
'YES, THOUGH YOU MAY NOT LIKE IT',
'NO, BUT YOU MAY WISH IT WAS SO'
]

class MagicBall:
    def __init__(self):
        self.type(ASK_ME, TYPING_PAUSE)

    def get_answer(self):
        self.type(random.choice(REPLIES), TYPING_PAUSE)
        self.make_pause()
        self.type(I_HAVE_AN_ANSWER, SLOW_TYPING_PAUSE)
        self.type(random.choice(ANSWERS), TYPING_PAUSE)

    def make_pause(self):
        dots = DOT_CHAR * random.randint(MIN_REPLY_PAUSE_DURATION_TACTS, MAX_REPLY_PAUSE_DURATION_TACTS)
        self.type(dots, TACT_DURATION_SECONDS)

    def type(self, text, pause_between_letters):
        for char in text:
            print(char + SPACE_CHAR, end='', flush=True)
            time.sleep(pause_between_letters)
        print()
        print()
