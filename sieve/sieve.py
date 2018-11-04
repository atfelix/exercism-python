def sieve(limit):
    if limit < 2:
        return []

    primes = [2]

    for n in range(3, limit + 1, 2):
        for p in primes:
            if n % p == 0:
                break
            if p * p > n:
                primes.append(n)
                break

    return primes
