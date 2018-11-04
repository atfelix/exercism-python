from collections import deque

def slices(series, length):
    if is_valid(series, length):
        raise ValueError

    return [window(series, length, index) for index in range(len(series) - length + 1)]

def is_valid(series, length):
    return length == 0 or len(series) < length

def window(series, length, index):
    return [int(x) for x in series[index:index + length]]