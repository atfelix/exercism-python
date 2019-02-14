class PigLatinTokenizer(object):

    class Token(object):
        def __init__(self, token, is_vowel):
            self.value = token
            self.is_vowel = is_vowel

    _tokens = [
        Token("str", False),
        Token("sch", False),
        Token("thr", False),
        Token("th", False),
        Token("tr", False),
        Token("qu", False),
        Token("ch", False),
        Token("sh", False),
        Token("rh", False),
        Token("st", False),
        Token("a", True),
        Token("b", False),
        Token("c", False),
        Token("d", False),
        Token("e", True),
        Token("f", False),
        Token("g", False),
        Token("h", False),
        Token("i", True),
        Token("j", False),
        Token("k", False),
        Token("l", False),
        Token("m", False),
        Token("n", False),
        Token("o", True),
        Token("p", False),
        Token("q", False),
        Token("r", False),
        Token("s", False),
        Token("t", False),
        Token("u", True),
        Token("v", False),
        Token("w", False),
        Token("x", False),
        Token("y", False),
        Token("z", False)
    ]

    def __init__(self, word):
        self.word = word
        self.current_index = 0
        self.tokens = []
        self.populate_tokens()

    def populate_tokens(self):
        token = self.next_token()
        while token:
            self.tokens.append(token)
            self.current_index += len(token.value)
            token = self.next_token()
        self.cleanup()

    def next_token(self):
        for token in PigLatinTokenizer._tokens:
            if self.word[self.current_index:].startswith(token.value):
                return token

    def cleanup(self):
        if len(self.tokens) <= 1:
            return
        elif self.tokens[0].value == "x" or self.tokens[0].value == "y":
            self.tokens[0].is_vowel = not self.tokens[1].is_vowel
        elif not self.tokens[0].is_vowel and self.tokens[1].value == "qu":
            self.tokens[:2] = [PigLatinTokenizer.Token(self.tokens[0].value + "qu", False)]

def translate(text):
    return ' '.join(map(pig_latin_word, text.split()))

def pig_latin_word(word):
    tokenizer = PigLatinTokenizer(word)
    start, ending = (0, "ay") if tokenizer.tokens[0].is_vowel else (1, tokenizer.tokens[0].value + "ay")
    pig_latin_word = ''.join(map(lambda token: token.value, tokenizer.tokens[start:]))
    
    return pig_latin_word + ending
