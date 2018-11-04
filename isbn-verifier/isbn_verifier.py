from functools import reduce

def verify(isbn):
    if not is_valid(isbn):
        return False
    digits = parse(isbn)
    return reduce(lambda x, y: x + y[0] * y[1], zip(digits, range(10, 0, -1)), 0) % 11 == 0

def is_valid(isbn):
    return len(parse(isbn)) == 10 and set(isbn[:-1]) <= set('0123456789-') and is_valid_check_sum(isbn)

def is_valid_check_sum(isbn):
    return isbn[-1] in set('1234567890X')

def parse(isbn):
    isbn = isbn.replace('-', '')
    return [value_from_char(x) for x in isbn]

def value_from_char(x):
    return int(x) if x.isdigit() else 10