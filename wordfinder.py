"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    def __init__(self, path):

        dict_file = open(path)

        self.words = self.readlines(dict_file)

        print(f"{len(self.words)} words read")

    def readlines(self, dict_file):

        return [word for word in dict_file]

    def random(self):

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):

    def readcleanlines(self, dict_file):
        return [word.strip() for word in dict_file if not word.startswith("#")]

