def square_of_sum(n):
    return sum_of_first_n_numbers(n) ** 2

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

def sum_of_first_n_numbers(n):
    return n * (n + 1) // 2