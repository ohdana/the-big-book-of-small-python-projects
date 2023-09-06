VOWELS = 'aeiouy'
DEFAULT_SUFFIX = 'ay'
GAP = ' '
ALLOWED_IN_WORD_CHARS = '\'-_'

class PigLatinConverter:
    def __init__(self):
        pass

    def convert(self, message):
        pointer = 0
        converted_message = ''
        while pointer < len(message):
            curr_char = message[pointer]
            if not curr_char.isalpha():
                converted_message += curr_char
                pointer += 1
            else:
                word = self.get_word(message, pointer)
                converted_message += self.convert_word(word)
                pointer += len(word)

        return converted_message

    def get_word(self, message, pointer):
        word = ''
        while self.is_part_of_word(message[pointer]):
            word += message[pointer]
            pointer += 1

        return word

    def is_part_of_word(self, char):
        return char.isalpha() or char in ALLOWED_IN_WORD_CHARS

    def convert_word(self, word):
        if not word:
            return ''

        if self.starts_with_vowel(word):
            converted_word = self.convert_word_starts_with_vowel(word.lower())
        else:
            converted_word = self.convert_word_starts_with_consonant(word.lower())

        if self.check_if_starts_with_capital(word):
            converted_word = converted_word[0].upper() + converted_word[1:]

        return converted_word

    def check_if_starts_with_capital(self, word):
        return 'A' <= word[0] <= 'Z'

    def convert_word_starts_with_vowel(self, word):
        return word + 'y' + DEFAULT_SUFFIX

    def convert_word_starts_with_consonant(self, word):
        suffix = ''
        tail = ''
        for char in word:
            if char not in VOWELS:
                suffix += char
            else:
                break

        return word[len(suffix):] + suffix + DEFAULT_SUFFIX + tail

    def starts_with_vowel(self, word):
        return word[0].lower() in VOWELS
