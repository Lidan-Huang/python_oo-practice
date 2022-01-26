from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Create word list from file path"""
        self.file_path = file_path
        self.word_list = self.read_file()
        self.count_words()

    def read_file(self):
        """Read file and return a list of words"""
        words_list = []
        file = open(self.file_path)
        for word in file:
            words_list.append(word.strip())
        file.close()
        return words_list

    def count_words(self):
        """Print the counts of words list"""
        print(f"{len(self.word_list)} words read")

    def random(self):
        """Print random word from the words list"""
        print(choice(self.word_list))


class SpecialWordFinder(WordFinder):
    """Word Finder: finds random words from a dictionary excludes the blank line
        and lines start with '#'.
    """

    def read_file(self):
        """Remove the blank line or line starts with '#'"""
        return [
            word for word in super().read_file()
            if not(len(word) == 0 or
                   word.startswith("#"))
        ]
