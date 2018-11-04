import random

from string import ascii_lowercase

class Cipher(object):
    def __init__(self, key=None):
        if key is not None and not key.islower():
            raise ValueError("Invalid key for cipher: %s", key)
        self.key = key or ''.join(random.choice(ascii_lowercase) for _ in range(100))

    def encode(self, text):
        return self.shifted(text, 1)

    def decode(self, text):
        return self.shifted(text, -1)

    def shifted(self, text, direction):
        return ''.join(
            map(
                lambda pair: shifted_char(ord(pair[1]), ord(self.key[pair[0] % len(self.key)]), direction),
                enumerate(text)
            )
        )
    
def shifted_char(order, shift_order, direction, base=ord('a')):
    return chr((order - base + direction * (shift_order - base)) % 26 + base)