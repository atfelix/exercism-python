from collections import Counter
from functools import reduce

def word_count(phrase):
    return Counter(map(lambda x: remove_quotations(x), remove_chars(phrase.lower()).split()))

def remove_chars(string, chars='!@#$%^&*(){}[]-_+=,.:'):
    return reduce(lambda x, y: x + (' ' if y in chars else y), string, '')

def remove_quotations(string):
    return remove_quotations(string[1:-1]) if is_quotation(string) else string

def is_quotation(string):
    return string[0] == string[-1] == '\'' or string[0] == string[-1] == '"'