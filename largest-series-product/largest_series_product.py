from functools import reduce

def largest_product(series, size):
    if not is_valid(series, size):
        raise ValueError('Invalid input: either size is too short or series contains non-numeric characters')

    digits = list(map(lambda x: int(x), list(series)))

    return reduce(lambda x, start: max(x, contiguous_product(digits, start, size)),
                  range(1, len(series)),
                  contiguous_product(digits, 0, size))

def is_valid(series, size):
    assert(type(series) == type(''))
    return 0 <= size <= len(series) and (series.isdigit() or series == '')

def contiguous_product(int_series, start, size):
    if start + size >= len(int_series) + 1:
        return -1
    return reduce(lambda x, y: x * y, int_series[start:start + size], 1)
