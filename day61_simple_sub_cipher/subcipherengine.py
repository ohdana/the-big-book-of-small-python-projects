import random

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class SubCipherEngine:
    def __init__(self):
        pass

    def generate_key(self):
        abc = list(ABC)
        random.shuffle(abc)
        return ''.join(abc)

    def encrypt(self, key, message):
        return self.map(self.get_encrypted_char, key, message)

    def decrypt(self, key, message):
        return self.map(self.get_decrypted_char, key, message)

    def map(self, mapping_function, key, message):
        if not self.is_valid_key(key):
            return message

        return ''.join(mapping_function(key, char) for char in message)

    def get_encrypted_char(self, key, char):
        return self.get_mapped_char(char, ABC, key)

    def get_decrypted_char(self, key, char):
        return self.get_mapped_char(char, key, ABC)

    def get_mapped_char(self, char, src, dest):
        uppercase_char = char.upper()
        if uppercase_char not in dest:
            return char

        index = src.index(uppercase_char)
        return self.bring_char_to_original_case(char, dest[index])

    def bring_char_to_original_case(self, original_char, char):
        if original_char.isupper():
            return char.upper()
        return char.lower()

    def is_valid_key(self, key):
        return len(set(key)) == len(ABC)
