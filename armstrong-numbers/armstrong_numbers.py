from functools import reduce

def is_armstrong(number):
    length = num_digits(number)
    return number == sum(map(lambda x: x ** length, digits(number)))

def num_digits(number, base=10):
    number = abs(number)
    length = 0

    while number > 0:
        length += 1
        number //= base
    
    return max(1, length)

def digits(number, base=10):
    _digits = []
    while number > 0:
        _digits.append(number % 10)
        number //= base
    
    return _digits[::-1]