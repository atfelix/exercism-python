from functools import reduce

def decode(string):
    return Decoder(string).decoding()

def encode(string):
    return Encoder(string).encoding()

class Encoder(object):

    def __init__(self, string):
        self.scanner = Scanner(string)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.scanner.has_next():
            raise StopIteration

        return self.find_run()

    def find_run(self):
        first_char = self.scanner.get_next_char()
        run = 1

        while self.scanner.has_next():
            next_char = self.scanner.get_next_char()
            if next_char == first_char:
                run += 1
            else:
                self.scanner.get_prev_char()
                break
        
        return first_char if run == 1 else '%d%c' % (run, first_char)

    def encoding(self):
        return reduce(lambda x, y: x + y, self, '')


class Decoder(object):

    def __init__(self, string):
        self.scanner = Scanner(string)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.scanner.has_next():
            raise StopIteration

        if self.scanner.has_next_int():
            answer = self.scanner.get_next_int() * self.scanner.get_next_char()
        else:
            answer = self.scanner.get_next_char() 
        return answer

    def decoding(self):
        return reduce(lambda x, y: x + y, self, '')

class Scanner(object):

    def __init__(self, string):
        self.string = string if string is not None else ""
        self.current_index = 0

    def get_next_int(self):
        if not self.has_next_int():
            return 0

        integer = 0

        while self.string[self.current_index].isdigit():
            integer = 10 * integer + int(self.string[self.current_index])
            self.current_index += 1

        return integer

    def has_next(self):
        return self.current_index < len(self.string)

    def has_next_int(self):
        return self.has_next() and self.string[self.current_index].isdigit()

    def has_next_char(self):
        return self.has_next() and self.string[self.current_index].isupper()

    def get_next_char(self):
        ch = self.string[self.current_index]
        self.current_index += 1
        return ch

    def get_prev_char(self):
        if not self.has_previous:
            raise IndexError
        self.current_index -= 1

    def has_previous(self):
        return self.current_index > 0