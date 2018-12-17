from functools import partial, reduce
from itertools import chain

def saddle_points(matrix):
    if not is_valid(matrix):
        raise ValueError('Invalid input:  all rows must have the same length')
    return set(filter(partial(is_saddle_point, matrix=matrix), potential_saddle_points(matrix)))

def is_valid(matrix):
    return all(len(matrix[0]) == len(matrix[i]) for i in range(1, len(matrix)))

def potential_saddle_points(matrix):
    return chain.from_iterable(zip([i] * len(matrix[0]), max_entries(matrix[i])) for i in range(len(matrix)))

def is_saddle_point(candidate, matrix):
    row, column = candidate
    entry = matrix[row][column]
    return entry == max(matrix[row]) and entry == min(matrix[i][column] for i in range(len(matrix)))
        
def max_entries(row):
    max_entry = max(row)
    return map(lambda x: x[0], filter(lambda x: x[1] == max_entry, enumerate(row)))
