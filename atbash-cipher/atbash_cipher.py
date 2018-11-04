from functools import reduce
from string import ascii_lowercase

def encode(plain_text):
    return Encoder(plain_text.lower()).encoding()

def decode(ciphered_text):
    return Decoder(ciphered_text).decoding()

class Encoder(object):

    def __init__(self, string):
        self.scanner = Scanner(Encoder.sanitize(string))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.scanner.has_next():
            raise StopIteration

        ans = ''
        while len(ans) < 5 and self.scanner.has_next():
            ans += Encoder.opposite_char(self.scanner.get_next_char())
        
        if self.scanner.has_next():
            ans += ' '
        
        return ans

    @staticmethod
    def opposite_char(char):
        base_dict = {x:y for (x, y) in zip(ascii_lowercase, ascii_lowercase[::-1])}
        return base_dict.get(char, char)

    @staticmethod
    def sanitize(string):
        return ''.join(char for char in string if Encoder.is_valid(char))

    @staticmethod
    def is_valid(char):
        return char.isalpha() or char.isdigit()
    
    def encoding(self):
        return reduce(lambda x, y: x + y, self, '')

class Decoder(Encoder):

    def __next__(self):
        if not self.scanner.has_next():
            raise StopIteration

        ans = ''
        while len(ans) < 5 and self.scanner.has_next():
            ans += Encoder.opposite_char(self.scanner.get_next_char())
        
        return ans 

    def decoding(self):
        return self.encoding()

class Scanner(object):

    def __init__(self, string):
        self.string = string if string is not None else ""
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.string)

    def has_next_char(self):
        return self.has_next() and self.string[self.current_index].isupper()

    def get_next_char(self):
        ch = self.string[self.current_index]
        self.current_index += 1
        return ch