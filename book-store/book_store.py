from collections import Counter

BOOK_PRICE = 800
DISCOUNTS = [0, 0, 5 / 100, 10 / 100, 20 / 100, 25 / 100]

def calculate_total(list_of_books):
    return DiscountCalculator(DISCOUNTS, BOOK_PRICE).calculate_total(list_of_books)

class DiscountCalculator(object):

    def __init__(self, discounts, book_price):
        self.discounts = discounts
        self.book_price = book_price
        self.price_dict = self.price_for_size_dict()
        self.ranks = self.ranking()
    
    def price_for_size_dict(self):
        return {size: size * self.book_price * (1 - self.discounts[size])
                    for size in range(len(self.discounts))}

    def ranking(self):
        """
        Returns a list rankings based on where the next best addition would be.

        The zeroth element is better than the first, which is better than the
        second and so on.  So, if this function return [2, 1, 3, 0], then
        it would be better to add a book to a group of size two than of size one.
        Similarly, it would be better to add to a group of size 1 than a group of
        size 3.
        """
        total_discounts = [discount * quantity for (quantity, discount) in enumerate(self.discounts)]
        increase_in_discount = [a - b for (a, b) in zip(total_discounts[1:], total_discounts)]
        return [index_increase[0] for index_increase in sorted(
            enumerate(increase_in_discount),
            key=lambda index_increase: index_increase[1],
            reverse=True
        )]

    def grouping(self, list_of_books):
        """
        Return the best grouping based on the discounts.

        The algorithm is as follows the below example:

        Suppose the sorted book counts are [7, 6, 5, 3, 1].

        At each iteration of these counts, look through the cache for the
        best group based ranking().  Add as many books to those groups as you
        can and then proceed unto the next best group.  Continue until you
        have placed all the books.
        """
        number_of_groups = [0] * len(self.discounts)

        if len(list_of_books) == 0:
            return number_of_groups
        
        book_counts = sorted(Counter(list_of_books).values(), reverse=True)
        number_of_groups[1] = book_counts[0]
        for book_count in book_counts[1:]:
            for rank, group_count in self.ranks_to_increased(book_count, number_of_groups):
                number_of_groups[rank] -= group_count
                number_of_groups[rank + 1] += group_count
        return number_of_groups
    
    def ranks_to_increased(self, count, number_of_groups):
        """
        Returns a tuple of the rank that should be increased and the number
        of elements that can be increased based on the number_of_groups
        """
        for rank in self.ranks:
            if number_of_groups[rank] > 0:
                yielded_count = min(count, number_of_groups[rank])
                count -= yielded_count
                yield rank, yielded_count


    def calculate_total(self, list_of_books):
        cost = 0
        for index, size in enumerate(self.grouping(list_of_books)):
            cost += size * self.price_dict[index]
        return cost