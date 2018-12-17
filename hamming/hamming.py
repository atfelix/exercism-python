from functools import reduce

def distance(strand_a, strand_b):
    if not are_valid_lengths(strand_a, strand_b):
        raise ValueError('Strands do not have the same lengths')

    return reduce(lambda x, y: x + (y[0] != y[1]), zip(strand_a, strand_b), 0)


def are_valid_lengths(s, t):
    return len(s) == len(t)