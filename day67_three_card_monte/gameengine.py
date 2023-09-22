import random
from card import Card
N_OF_SWAPS = 10
JACK, QUEEN, EIGHT = 'J', 'Q', '8'
DIAMONDS, HEARTS, CLUBS = '♦', '♥', '♣'

class GameEngine:
    def __init__(self):
        self.cards = self.init_cards()

    def is_queen_of_hearts(self, card):
        return card.get_suit_value() == (HEARTS, QUEEN)

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
        jack = self.init_card('J', '♦')
        queen = self.init_card('Q', '♥')
        eight = self.init_card('8', '♣')

        return [jack, queen, eight]

    def init_card(self, value, suit):
        return Card(value, suit)
