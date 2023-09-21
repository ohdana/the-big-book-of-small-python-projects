import random

GRID_LENGTH = 81

class GridReader:
    def __init__(self, filename):
        self.puzzles = self.load_puzzles(filename)≈

    def load_puzzles(self, filename):
        puzzles_file = open(filename, "r")
        puzzles_file_contents = puzzles_file.read()
        puzzle_strings = puzzles_file_contents.split('\n')

        return [list(puzzle_string) for puzzle_string in puzzle_strings]

    def get_random_puzzle(self):
        return random.choice(self.puzzles)
