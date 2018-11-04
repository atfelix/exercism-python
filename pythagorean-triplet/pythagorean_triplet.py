import math

from functools import partial

def primitive_triplets(number_in_triplet):
    return set(filter(is_triplet, map(candidate_triplet, primitive_divisors(number_in_triplet // 2))))

def candidate_triplet(pair):
    n, m = pair
    n2, m2 = n * n, m * m
    return tuple(sorted([m2 - n2, 2 * m * n, m2 + n2]))

def primitive_divisors(n):
    return ((d, n // d) for d in filter(partial(is_primitive_divisor, n=n), range(1, math.ceil(n ** 0.5))))

def is_primitive_divisor(d, n):
    return (n % d == 0 
            and math.gcd(d, n // d) == 1
            and not (d % 2 == 1 == (n // d) % 2))

def triplets_in_range(start, end):
    return set(tuple(multiplier * x for x in triple) 
                for multiplier in range(1, end)
                for triple in helper_primitive(start / multiplier, end / multiplier))

def helper_primitive(start, end):
    m = 1
    while m <= math.floor(end ** 0.5):
        n = 1
        while 0 < n < m:
            if m % 2 == 1 and n % 2 == 1 or math.gcd(n, m) != 1:
                n += 1
                continue
            n2 = n * n
            m2 = m * m
            candidate = m2 - n2, 2 * m * n, m2 + n2
            if start <= min(candidate) and max(candidate) <= end:
                yield tuple(sorted(candidate))
            n += 1
        m += 1

def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
