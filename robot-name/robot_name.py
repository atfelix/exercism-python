import random

class PatternGenerator(object):

    InvalidPatternCharacterError = ValueError('Pattern character no recognized:  Expecting \'a\' or \'#\', given \'%c\'')

    def __init__(self, pattern):
        self.generator = random.Random()
        self.pattern = pattern
    
    def name(self):
        map_functions = {
            'a': self.letter,
            '#': self.digit
        }
        return ''.join(map(lambda char: map_functions.get(char, lambda _: PatternGenerator.InvalidPatternCharacterError % char)(), self.pattern))


    def letter(self):
        return self.character('A', 25)

    def digit(self):
        return self.character('0', 9)

    def character(self, start, end):
        return chr(ord(start) + self.generator.randint(0, end))


class Robot(object):
    def __init__(self):
        self.generator = PatternGenerator('aa###')
        self.stored_name = None
    
    @property
    def name(self):
        if self.stored_name is None:
            self.stored_name = self.generator.name()
            
        return self.stored_name
    
    def reset(self):
        self.stored_name = None