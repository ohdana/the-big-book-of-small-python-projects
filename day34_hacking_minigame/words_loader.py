FILE_NAME = 'words.txt'
CACHE = {}

def load_words(word_length):
    if word_length in CACHE:
        return CACHE[word_length]

    file = open(FILE_NAME, 'r')
    words = []
    while True:
        word = file.readline().strip()
        if not word:
            break

        if len(word) == word_length:
            words.append(word)

    CACHE[word_length] = words

    return words

