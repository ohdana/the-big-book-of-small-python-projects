ENCRYPT, DECRYPT = 'e', 'd'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Engine:
    def __init__(self):
        pass

    def encrypt(self, message, key):
        return self.translate(ENCRYPT, message, key)

    def decrypt(self, message, key):
        return self.translate(DECRYPT, message, key)

    def translate(self, mode, message, key):
        result = ''
        key = key.upper()
        key_index = 0
        for char in message:
            char_index_in_abc = ABC.find(char.upper())
            if char_index_in_abc < 0:
                result += char
                continue

            result += self.translate_char(mode, char_index_in_abc, key[key_index], char.isupper())
            key_index = (key_index + 1) % len(key)

        return result

    def translate_char(self, mode, char_index_in_abc, key_char, is_uppercase):
        new_char_index_in_abc = 0
        if mode == ENCRYPT:
            new_char_index_in_abc = (ABC.find(key_char) + char_index_in_abc) % len(ABC)
        else:
            new_char_index_in_abc = (ABC.find(key_char) - char_index_in_abc) % len(ABC)
        new_char = ABC[new_char_index_in_abc]
        if is_uppercase:
            return new_char.upper()
        else:
            return new_char.lower()

e = Engine()
print(e.translate('d', 'Bmds mt jx sht znre qcrgeh bnmivps.', 'pizza'))
