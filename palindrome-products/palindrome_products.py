def is_number_palindrome(n):
    return n == reverse(n)

def reverse(n):
    m = 0
    while n:
        m = 10 * m + n % 10
        n //= 10
    return m
    
def all_are_nines(n):
    s = str(n)
    return s == '9' * len(s)

def divisors(n, min_factor, max_factor):
    pairs = set()
    a = min_factor
    while a <= min(max_factor, n // a):
        if n % a == 0 and min_factor <= n // a <= max_factor:
            pairs.add((a, n // a))
        a += 1
    return pairs

def largest_palindrome(max_factor, min_factor):
    end, start = min_factor * min_factor, max_factor * max_factor + 1
    return optimal_palindrome(previous_palindrome, 
                              min_factor,
                              max_factor,
                              start,
                              end,
                              lambda a: a >= end)

def smallest_palindrome(max_factor, min_factor):
    start, end = min_factor * min_factor - 1, max_factor * max_factor
    return optimal_palindrome(next_palindrome, 
                              min_factor,
                              max_factor,
                              start,
                              end,
                              lambda a: a <= end)

def optimal_palindrome(iterator, min_factor, max_factor, start, end, condition):
    if not is_valid_range(min_factor, max_factor):
        raise ValueError("min is larger than max")

    a = iterator(start)
    factors = divisors(a, min_factor, max_factor)

    while not factors and condition(a):
        a = iterator(a)
        factors = divisors(a, min_factor, max_factor)

    if not factors:
        raise ValueError("No palindrome found")

    return a, factors

def is_valid_range(min_factor, max_factor):
    return min_factor < max_factor

def next_palindrome(n):
    if all_are_nines(n):
        return n + 2
    if n == 0:
        return 1

    return next_palindrome_helper(n)

def next_palindrome_helper(n):
    digits = list(map(int, str(n)))
    mid, left, right = start(digits)
    is_left_smaller = left < 0 or digits[left] < digits[right]
    balance_digits(digits, left, right)

    if not is_left_smaller:
        return int(''.join(map(str, digits)))

    carry, left = 1, mid - 1

    if n % 2:
        digits[mid] += carry
        carry = digits[mid] // 10
        digits[mid] %= 10
        right = mid + 1
    else:
        right = mid

    while left >= 0:
        left, right, carry = increment_opposite_digits(digits, left, right, carry)
        
    return int(''.join(map(str, digits)))

def start(digits):
    length = len(digits)
    mid = length // 2
    left, right = mid - 1, mid + 1 if length % 2 else mid

    while left >= 0 and digits[left] == digits[right]:
        left -= 1
        right += 1
    
    return mid, left, right

def balance_digits(digits, left, right):
    while left >= 0:
        digits[right] = digits[left]
        right += 1
        left -= 1

def increment_opposite_digits(digits, left, right, carry):
    digits[left] += carry
    carry = digits[left] // 10
    digits[left] %= 10
    digits[right] = digits[left]
    return left - 1, right + 1, carry


def previous_palindrome(n):
    if all_are_nines(n - 2):
        return n - 2
    
    return previous_palindrome_helper(n)

def previous_palindrome_helper(n):
    left, right = left_side(n), right_side(n)
    reverse_left = left[::-1]
    s = str(n)
    length = len(s)
    mid = length // 2
    if int(left) < int(right) and length % 2 == 0:
        return int(reverse_left + left)
    elif int(left) < int(right):
        return int(reverse_left + str(n)[mid] + left)
    elif length % 2 == 0:
        new_left = str(int(reverse_left) - 1)
        return int(new_left + new_left[::-1])
    else:
        first_half = str(int(str(n)[:mid + 1]) - 1)
        second_half = first_half[:-1][::-1]
        return int(first_half + second_half)

def left_side(n):
    s = str(n)
    return str(reverse(int(s[:len(s) // 2]))).zfill(len(s) // 2)

def right_side(n):
    s = str(n)
    length = len(s)
    modified_length = length // 2 if length % 2 == 0 else length // 2 + 1
    start = length // 2 if length % 2 == 0 else length // 2 + 1
    return str(int(s[start:])).zfill(modified_length)