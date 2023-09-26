import random
QUIT = 'quit'
CORRECT_ANSWER_REACTIONS = ['Correct!', 'That is right.', "You're right.", 'You got it.', 'Righto!']
INCORRECT_ANSWER_REACTIONS = ['Incorrect!', "Nope, that isn't it.", 'Nope.', 'Not quite.', 'You missed it.']

def main():
    init()
    show_intro_message()
    play()
    show_bye_message()

def play():
    input(STRINGS_DICTIONARY.press_enter_to_begin)
    questions = get_all_questions()
    total_n_of_questions = len(questions)
    question_number = 0
    n_of_correct_answers = 0
    while True:
        question_number += 1
        show_stats(question_number, n_of_correct_answers, total_n_of_questions)
        question, correct_answer, accepted_answers = get_random_question(questions)
        ask_question(question)
        user_input = get_user_input()
        if user_input == QUIT:
            break
        if user_input in accepted_answers:
            n_of_correct_answers += 1
            process_correct_answer()
        else:
            process_incorrect_answer(correct_answer)
        input(STRINGS_DICTIONARY.press_enter_for_next_question)

def show_stats(question_number, n_of_correct_answers, total_n_of_questions):
    print(STRINGS_DICTIONARY.stats.format(question_number, n_of_correct_answers, total_n_of_questions))

def get_random_question(questions):
    question_obj = random.choice(questions)
    return question_obj['question'], question_obj['answer'], question_obj['accept']

def ask_question(question):
    print(STRINGS_DICTIONARY.question.format(question))

def get_user_input():
    user_input = input(STRINGS_DICTIONARY.answer).lower()
    if not user_input:
        return get_user_input()
    return user_input

def process_correct_answer():
    reaction = random.choice(CORRECT_ANSWER_REACTIONS)
    print(STRINGS_DICTIONARY.correct.format(reaction))

def process_incorrect_answer(correct_answer):
    reaction = random.choice(INCORRECT_ANSWER_REACTIONS)
    print(STRINGS_DICTIONARY.incorrect.format(reaction, correct_answer))

def get_all_questions():
    return [
 {'question': "How many times can you take 2 apples from a pile of 10 apples?",
  'answer': "Once. Then you have a pile of 8 apples.",
  'accept': ['once', 'one', '1']},
 {'question': 'What begins with "e" and ends with "e" but only has one letter in it?',
  'answer': "An envelope.",
  'accept': ['envelope']},
 {'question': "Is it possible to draw a square with three sides?",
  'answer': "Yes. All squares have three sides. They also have a fourth side.",
  'accept': ['yes']},
 {'question': "How many times can a piece of paper be folded in half by hand without unfolding?",
  'answer': "Once. Then you are folding it in quarters.",
  'accept': ['one', '1', 'once']},
 {'question': "What does a towel get as it dries?",
  'answer': "Wet.",
  'accept': ['wet']},
 {'question': "What does a towel get as it dries?",
  'answer': "Drier.",
  'accept': ['drier', 'dry']},
 {'question': "Imagine you are in a haunted house full of evil ghosts. What do you have to do to stay safe?",
  'answer': "Nothing. You're only imagining it.",
  'accept': ['nothing', 'stop']},
{'question': "A taxi driver is going the wrong way down a one-way street. She passes ten cops but doesn't get a ticket. Why not?",
  'answer': "She was walking.",
  'accept': ['walk']},
 {'question': "What does a yellow stone thrown into a blue pond become?",
  'answer': "Wet.",
  'accept': ['wet']},
 {'question': "How many miles does must a cyclist bike to get to training?",
  'answer': "None. They're training as soon as they get on the bike.",
  'accept': ['none', 'zero', '0']},
 {'question': "What building do people want to leave as soon as they enter?",
  'answer': "An airport.",
  'accept': ['airport', 'bus', 'port', 'train', 'station', 'stop']},
 {'question': "If you're in the middle of a square house facing the west side with the south side to your left and the north side to your right, which side of the house are you next to?",
  'answer': "None. You're in the middle.",
  'accept': ['none', 'middle', 'not', 'any']},
 {'question': "How much dirt is in a hole 3 meters wide, 3 meters long, and 3 meters deep?",
  'answer': "There is no dirt in a hole.",
  'accept': ['no', 'none', 'zero']},
 {'question': "A girl mails a letter from America to Japan. How many miles did the stamp move?",
  'answer': "Zero. The stamp was in the same place on the envelope the whole time.",
  'accept': ['zero', '0', 'none', 'no']},
 {'question': "What was the highest mountain on Earth the day before Mount Everest was discovered?",
  'answer': "Mount Everest was still the highest mountain of Earth the day before it was discovered.",
  'accept': ['everest']},
 {'question': "How many fingers do most people have on their two hands?",
  'answer': "Eight. They also have two thumbs.",
  'accept': ['eight', '8']},
 {'question': "The 4th of July is a holiday in America. Do they have a 4th of July in England?",
  'answer': "Yes. All countries have a 4th of July on their calendar.",
  'accept': ['yes']},
 {'question': "Which letter of the alphabet makes honey?",
  'answer': "None. A bee is an insect, not a letter.",
  'accept': ['no', 'none', 'not']},
 {'question': "How can a doctor go 30 days without sleep?",
  'answer': "By sleeping at night.",
  'accept': ['night', 'evening']},
 {'question': "How many months have 28 days?",
  'answer': "12. All months have 28 days. Some have more days as well.",
  'accept': ['12', 'twelve', 'all']},
 {'question': "How many two cent stamps are in a dozen?",
  'answer': "A dozen.",
  'accept': ['12', 'twelve', 'dozen']},
 {'question': "Why is it illegal for a person living in North Dakota to be buried in South Dakota?",
  'answer': "Because it is illegal to bury someone alive.",
  'accept': ['alive', 'living', 'live']},
 {'question': "How many heads does a two-headed coin have?",
  'answer': "Zero. Coins are just circular pieces of metal. They don't have heads.",
  'accept': ['zero', 'none', 'no', '0']},
 {'question': "What kind of vehicle has four wheels and flies?",
  'answer': "A garbage truck.",
  'accept': ['garbage', 'dump', 'trash']},
 {'question': "What kind of vehicle has four wheels and flies?",
  'answer': "An airplane.",
  'accept': ['airplane', 'plane']},
 {'question': "What five-letter word becomes shorter by adding two letters?",
  'answer': "Short.",
  'accept': ['short']},
 {'question': "Gwen's mother has five daughters. Four are named Haha, Hehe, Hihi, and Hoho. What's the fifth daughter's name?",
  'answer': "Gwen.",
  'accept': ['gwen']},
 {'question': "How long is a fence if there are three fence posts each one meter apart?",
  'answer': "Two meters long.",
  'accept': ['2', 'two']},
 {'question': "How many legs does a dog have if you count its tail as a leg?",
  'answer': "Four. Calling a tail a leg doesn't make it one.",
  'accept': ['four', '4']},
 {'question': "How much more are 1976 pennies worth compared to 1975 pennies?",
  'answer': "One cent.",
  'accept': ['1', 'one']},
 {'question': "What two things can you never eat for breakfast?",
  'answer': "Lunch and dinner.",
  'accept': ['lunch', 'dinner', 'supper']},
 {'question': "How many birthdays does the average person have?",
  'answer': "One. You're only born once.",
  'accept': ['one', '1', 'once' 'born']},
 {'question': "Where was the United States Declaration of Independence signed?",
  'answer': "It was signed at the bottom.",
  'accept': ['bottom']},
 {'question': "A person puts two walnuts in their pocket but only has one thing in their pocket five minutes later. What is it?",
  'answer': "A hole.",
  'accept': ['hole']},
 {'question': "What did the sculptor make that no one could see?",
  'answer': "Noise.",
  'accept': ['noise']},
 {'question': "If you drop a raw egg on a concrete floor, will it crack?",
  'answer': "No. Concrete is very hard to crack.",
  'accept': ['no']},
 {'question': "If it takes ten people ten hours to build a fence, how many hours does it take five people to build it?",
  'answer': "Zero. It's already built.",
  'accept': ['zero', 'no', '0', 'already', 'built']},
 {'question': "Which is heavier, 100 pounds of rocks or 100 pounds of feathers?",
  'answer': "Neither. They weigh the same.",
  'accept': ['neither', 'none', 'no', 'same', 'even', 'balance']},
 {'question': "What do you have to do to survive being bitten by a poisonous snake?",
  'answer': "Nothing. Only venomous snakes are deadly.",
  'accept': ['nothing', 'anything']},
 {'question': "What three consecutive days don't include Sunday, Wednesday, or Friday?",
  'answer': "Yesterday, today, and tomorrow.",
  'accept': ['yesterday', 'today', 'tomorrow']},
 {'question': "If there are ten apples and you take away two, how many do you have?",
  'answer': "Two.",
  'accept': ['2', 'two']},
 {'question': "A 39 year old person was born on the 22nd of February. What year is their birthday?",
  'answer': "Their birthday is on February 22nd of every year.",
  'accept': ['every', 'each']},
 {'question': "How far can you walk in the woods?",
  'answer': "Halfway. Then you are walking out of the woods.",
  'accept': ['half', '1/2']},
 {'question': "Can a man marry his widow's sister?",
  'answer': "No, because he's dead.",
  'accept': ['no']},
 {'question': "What do you get if you divide one hundred by half?",
  'answer': "One hundred divided by half is two hundred. One hundred divided by two is fifty.",
  'accept': ['two', '200']},
 {'question': "What do you call someone who always knows where their spouse is?",
  'answer': "A widow or widower.",
  'accept': ['widow', 'widower']},
 {'question': "How can someone take a photo but not be a photographer?",
  'answer': "They can be a thief.",
  'accept': ['thief', 'steal', 'take', 'literal']},
 {'question': "An electric train leaves the windy city of Chicago at 4pm on a Monday heading south at 100 kilometers per hour. Which way does the smoke blow from the smokestack?",
  'answer': "Electric trains don't have smokestacks.",
  'accept': ["don't", "doesn't", 'not', 'no', 'none']},
 {'question': 'What is the only word that rhymes with "orange"?',
  'answer': "Orange.",
  'accept': ['orange']},
 {'question': "Who is the U.S. President if the U.S. Vice President dies?",
  'answer': "The current U.S. President.",
  'accept': ['president', 'current', 'already']},
 {'question': "A doctor gives you three pills with instructions to take one every half-hour. How long will the pills last?",
  'answer': "One hour.",
  'accept': ['1', 'one']},
 {'question': "Where is there an ocean with no water?",
  'answer': "On a map.",
  'accept': ['map']},
 {'question': "What is the size of a rhino but weighs nothing?",
  'answer': "A rhino's shadow.",
  'accept': ['shadow']},
 {'question': "The clerk at a butcher shop is exactly 177 centimeters tall. What do they weigh?",
  'answer': "The clerk weighs meat.",
  'accept': ['meat']}]

def show_intro_message():
    print(STRINGS_DICTIONARY.intro_message)

def show_bye_message():
    print(STRINGS_DICTIONARY.bye_message)

def init():
    init_strings_dictionary()
##############################
def init_strings_dictionary():
    global STRINGS_DICTIONARY
    STRINGS_DICTIONARY = StringsDictionary()

    STRINGS_DICTIONARY.intro_message = '''
    Trick Questions

    Idea by Al Sweigart al@inventwithpython.com
    Implementation by @ohdana

    Can you figure out the answers to these trick questions?
    (Enter QUIT to quit at any time.)'''
    STRINGS_DICTIONARY.bye_message = '''
    Bye!'''
    STRINGS_DICTIONARY.press_enter_to_begin = '''
    Press Enter to begin...'''
    STRINGS_DICTIONARY.press_enter_for_next_question = '''
    Press Enter for the next question...'''
    STRINGS_DICTIONARY.answer = '''
        ANSWER: '''
    STRINGS_DICTIONARY.question = '''
    QUESTION: {}'''
    STRINGS_DICTIONARY.stats = '''
    Question: {}
    Score: {} / {}'''
    STRINGS_DICTIONARY.incorrect = '''
    {} The answer is: {}'''
    STRINGS_DICTIONARY.correct = '''
    {}'''

class StringsDictionary:
    pass

main()

