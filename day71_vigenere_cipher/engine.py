ENCRYPT, DECRYPT = "e", "d"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Engine:
    def __init__(self):
        pass

    def encrypt(self, message, key):
        return self.translate(ENCRYPT, message, key)

    def decrypt(self, message, key):
        return self.translate(DECRYPT, message, key)

    def translate(self, mode, message, key):
        result = ""
        key = key.upper()
        key_index = 0
        for char in message:
            char_index_in_abc = ABC.find(char.upper())
            if char_index_in_abc < 0:
                result += char
                continue

            result += self.translate_char(
                mode, char_index_in_abc, key[key_index], char.isupper()
            )
            key_index = (key_index + 1) % len(key)

        return result

    def translate_char(self, mode, char_index_in_abc, key_char, is_uppercase):
        translate_char_function = (
            self.encrypt_char if mode == ENCRYPT else self.decrypt_char
        )
        new_char = translate_char_function(char_index_in_abc, key_char)
        return self.format_case(new_char, is_uppercase)

    def format_case(self, string, is_uppercase):
        return string.upper() if is_uppercase else string.lower()

    def encrypt_char(self, char_index_in_abc, key_char):
        return ABC[(char_index_in_abc + ABC.find(key_char)) % len(ABC)]

    def decrypt_char(self, char_index_in_abc, key_char):
        return ABC[(char_index_in_abc - ABC.find(key_char)) % len(ABC)]
