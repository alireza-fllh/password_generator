import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    """ Abstract class for password generators.
    """

    @abstractmethod
    def generate(self):
        pass


class RandomPasswordGenerator(PasswordGenerator):
    """ Generate random password. The password can include numbers and symbols.
    """

    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        """
        :param length: length of the password, defaults to 8
        :param include_numbers: whether to include numbers in the password, defaults to False
        :param include_symbols: whether to include symbols in the password, defaults to False
        """
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if self.include_numbers:
            self.characters += string.digits
        if self.include_symbols:
            self.characters += string.punctuation

    def generate(self):
        password = random.choices(self.characters, k=self.length)
        return ''.join(password)


class MemorablePasswordGenerator (PasswordGenerator):
    """ Generate memorable password. The password is a combination of words. Words are separated by a separator and can be capitalized.
    """

    def __init__(self, num_words: int = 4, separator: str = '-', is_capitalize: bool = False, vocabulary: list[str] = None):
        """
        :param num_words: number of words in the password, defaults to 4
        :param separator: separator between words, defaults to '-'
        :param is_capitalize: whether to capitalize words, defaults to False
        :param vocabulary: list of words to use as the vocabulary, defaults to None
        """
        self.num_words = num_words
        self.separator = separator
        self.is_capitalize = is_capitalize
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()                 # use the nltk corpus as the default vocabulary
        else:
            self.vocabulary = vocabulary

    def generate(self):
        password = random.choices(self.vocabulary, k=self.num_words)
        if self.is_capitalize:
            password = [word.upper() if random.choice([True, False]) else word.lower() for word in password]
        return self.separator.join(password)


class PinCodeGenerator (PasswordGenerator):

    def __init__(self, length: int = 8):
        """
        :param length: length of the pin code, defaults to 8
        """
        self.length = length

    def generate(self):
        pin = random.choices(string.digits, k=self.length)
        return ''.join(pin)


if __name__ == '__main__':
    p_obj = RandomPasswordGenerator(length=10, include_symbols=True, include_numbers=True)
    print(p_obj.generate())