import random

from math import gcd

def prime_factors(natural_number):
    if natural_number == 1:
        return []
    divisors = [natural_number]
    factors = []
    while divisors:
        d = divisors.pop()
        if millerrabin(d):
            factors.append(d)
            continue
        new_d = pollard(d)
        if d == new_d:
            divisors.append(d)
            continue
        divisors.extend([new_d, d // new_d])
    return list(sorted(factors))

def millerrabin(n):
    if n == 1:
        return False
    if n in [2, 3, 5]:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    for a in [2, 3, 5]:
        if is_composite(a, d, n, s):
            return False

    return True

def pollard(n):
    if n % 2 == 0:
        return 2
    a = random.randint(-100, 100)
    while a == -2:
        a = random.randint(-100, 100)
    x = random.randint(1, 1000)
    y = x
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + a) % n
        y = (pow(y, 2, n) + a) % n
        y = (pow(y, 2, n) + a) % n
        d = gcd(abs(x - y), n)
        if d == n:
            break
    return d

def is_composite(a, d, n, s):
    if pow(a, d, n) == 1:
            return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True