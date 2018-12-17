def triplets_in_range(start, end, value):
    return set(tuple(multiplier * x for x in triple) 
                for multiplier in divisors(value)
                for triple in helper_primitive(start / multiplier, end / multiplier, value // multiplier))

def divisors(n):
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            yield d
            yield n // d

def helper_primitive(start, end, value):
    for m in range(1, int(min(value ** 0.5, end ** 0.5)) + 1):
        n = value // 2 // m - m
        if not 0 < n < m:
            continue
        n2, m2 = n * n, m * m
        candidate = m2 - n2, 2 * m * n, m2 + n2
        if sum(candidate) == value and start <= min(candidate) and max(candidate) <= end:
            yield tuple(sorted(candidate))

def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2

def triplets_with_sum(value):
    return set((a, b, c) for (a, b, c) in triplets_in_range(1, value, value) if a + b + c == value)
