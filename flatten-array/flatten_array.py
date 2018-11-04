from collections import Sequence

def flatten(iterable):
    result = []
    for x in iterable:
        if isinstance(x, Sequence) and not isinstance(x, str):
            result.extend(flatten(x))
        elif x is not None:
            result.append(x)
    return result
