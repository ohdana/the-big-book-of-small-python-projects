IMAGE_PATTERN = ' ___ \n|{value}  |\n| {suit} |\n|__{value}|'

class Card:
    height = len(IMAGE_PATTERN.split('\n'))
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = IMAGE_PATTERN.format(value=value, suit=suit)

    def get_suit_value(self):
        return self.suit, self.value

    def get_image(self):
        return self.image
