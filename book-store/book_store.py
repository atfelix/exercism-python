from collections import Counter
from functools import reduce

BOOK_PRICE = 800
DISCOUNTS = (1, 1, 0.95, 0.9, 0.8, 0.75)

def group_price(book_price=BOOK_PRICE, discounts=DISCOUNTS):
    return {quantity: book_price * quantity * discounts[quantity]
                for quantity in range(len(discounts))}

GROUP_PRICE = group_price()

def calculate_total(list_of_books, book_price=BOOK_PRICE):
    book_counts = sorted(Counter(list_of_books).values(), reverse=True)
    return reduce(
        lambda acc, books: min(acc, cost_of_books(groups_of_books(books))), 
        partitions(book_counts), 
        book_price * len(list_of_books)
    )

def cost_of_books(partitions_of_books, group_price_mapping=GROUP_PRICE):
    cost = 0
    for size, number_of_size in enumerate(partitions_of_books):
        cost += group_price_mapping[size] * number_of_size
    return cost

def groups_of_books(partition):
    return (0,) + tuple(partition[i] - partition[i + 1] 
                    if i + 1 != len(partition) else partition[i]
                    for i in range(len(partition)))

def partitions(counts):
    """
    This function generates all equivalent partitions for this problem.

    This algorithm is as follows:
        If there are at most two types of books,
        then return the list of partitions [(max counts, min counts)],
        else we make the following observation:

        Any partition can be made up of a base partition and a restricted
        partition where the length of the restricted partition is dictated
        by the penultimate length of the base partition and the last two
        elements of counts.

        For example, suppose you had counts = [5, 4, 2, 2, 1].  A valid
        partition is 

        1 1 1 1 1
        2 2 2 2 4
        3 3
        4 5

        Note that this partition is equivalent to the following partition

        1 1 1 1 1
        2 2 2 2 3
        3 4
        4 5

        In this second partition, the first two rows is the base partition
        and the last two rows are the restricted.

    @param counts:  sorted list of books counts

    Returns all partitions converted to counts based on row.

    For example, the above partition is returned as (5, 5, 2, 2, 0)
    """
    assert(all(counts[i] >= counts[i + 1] for i in range(len(counts) - 1)))
    if len(counts) <= 2: return [tuple(counts)]
    list_of_partitions = []
    for base_partition in partitions(counts[:-1]):
        for restricted_partition in restricted_partitions(base_partition[-2], 
                                                          max(counts[-1], base_partition[-1]),
                                                          min(counts[-1], base_partition[-1])):
            list_of_partitions.append(base_partition[:-1] + restricted_partition)
    return list_of_partitions

def restricted_partitions(length, num_xs, num_ys):
    """
    Returns all partitions
    """
    assert(num_xs >= num_ys)
    return [(num_xs + i, num_ys - i) for i in range(min(length - num_xs, num_ys) + 1)]
