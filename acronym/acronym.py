def abbreviate(words):
    return AcronymEncoder(words).encoding()

class AcronymEncoder(object):

    def __init__(self, words):
        self.scanner = Scanner(words)
        self.searching_for_word = True

    def __iter__(self):
        return self

    def __next__(self):
        if not self.scanner.has_next():
            raise StopIteration

        char = self.scanner.get_next_char()

        if (char.isalpha() or char == '\'') and self.searching_for_word:
            self.searching_for_word = False
            return char.upper()
        elif not (char.isalpha() or char == '\''):
            self.searching_for_word = True
        
        return ''

    def encoding(self):
        return ''.join(x for x in self)


class Scanner(object):

    def __init__(self, string):
        self.string = string if string is not None else ""
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.string)

    def has_next_char(self):
        return self.has_next() and self.string[self.current_index].isalpha()

    def get_next_char(self):
        ch = self.string[self.current_index]
        self.current_index += 1
        return ch