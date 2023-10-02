import random
from card import Card
N_OF_SWAPS = 10
JACK, QUEEN, EIGHT = 'J', 'Q', '8'
DIAMONDS, HEARTS, CLUBS = '♦', '♥', '♣'
ALWAYS_LOSE = True

class GameEngine:
    def __init__(self):
        self.cards = self.init_cards()

    def is_winning_answer(self, user_answer):
        queen_index = self.get_queen_index()
        print(user_answer, queen_index)
        is_answer_correct = (user_answer == queen_index)
        if is_answer_correct and ALWAYS_LOSE:
            self.make_random_queen_swap(queen_index)
            is_answer_correct = False
        return is_answer_correct

    def make_random_queen_swap(self, queen_index):
        random_index = queen_index
        while random_index == queen_index:
            random_index = self.get_random_index()
        self.swap(queen_index, random_index)

    def get_queen_index(self):
        for i in range(len(self.cards)):
            card = self.cards[i]
            if self.is_queen_of_hearts(card):
                return i

    def shuffle(self):
        shuffle_log = []
        for i in range(N_OF_SWAPS):
            index_1, index_2 = self.get_indices_to_swap()
            self.swap(index_1, index_2)
            shuffle_log.append((index_1, index_2))

        return shuffle_log

    def get_cards(self):
        return self.cards

    def get_card_height(self):
        return Card.height

    def swap(self, index_1, index_2):
        self.cards[index_1], self.cards[index_2] = self.cards[index_2], self.cards[index_1]

    def is_queen_of_hearts(self, card):
        return card.get_suit_value() == (HEARTS, QUEEN)

    def get_indices_to_swap(self):
        indices = []
        required_n_of_indices = 2
        while len(indices) < required_n_of_indices:
            new_index = self.get_random_index()
            if new_index not in indices:
                indices.append(new_index)
        return indices

    def get_random_index(self):
        return random.randint(0, len(self.cards) - 1)

    def init_cards(self):
        jack = self.init_card(JACK, DIAMONDS)
        queen = self.init_card(QUEEN, HEARTS)
        eight = self.init_card(EIGHT, CLUBS)

        return [jack, queen, eight]

    def init_card(self, value, suit):
        return Card(value, suit)

    def get_cards_image(self):
        card_images = [card.get_image() for card in self.cards]
        card_images_lines = [image.split('\n') for image in card_images]
        card_height = self.get_card_height()
        lines = []
        for i in range(card_height):
            lines.append(' '.join([image[i] for image in card_images_lines]))

        return '\n'.join(lines)
