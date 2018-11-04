from functools import reduce

class Category(object):

    def __init__(self, closure, condition=lambda dice: True):
        self.closure = closure
        self.condition = condition

    def score(self, dice):
        print(dice, self.condition(dice))
        return self.closure(dice) if self.condition(dice) else 0

def weighted_sum(weight):
    return lambda dice: weight * dice.count(weight)

def four_of_a_kind_sum(dice):
    return sum(dice) - reduce(lambda x, y: x ^ y, dice)

def is_four_of_a_kind(dice):
    return any(dice.count(die) >= 4 for die in dice)

def is_full_house(dice):
    return len(set(dice)) == 2 and all(dice.count(die) >= 2 for die in dice)

def is_yacht(dice):
    return all(die == dice[0] for die in dice)

def is_straight(start, end):
    def func(dice):
        return sorted(dice) == list(range(start, end))
    
    return func

def score(dice, category):
    return category.score(dice)

YACHT = Category(lambda dice: 50, condition=is_yacht)
ONES = Category(weighted_sum(1))
TWOS = Category(weighted_sum(2))
THREES = Category(weighted_sum(3))
FOURS = Category(weighted_sum(4))
FIVES = Category(weighted_sum(5))
SIXES = Category(weighted_sum(6))
FULL_HOUSE = Category(sum, condition=is_full_house)
FOUR_OF_A_KIND = Category(four_of_a_kind_sum, condition=is_four_of_a_kind)
LITTLE_STRAIGHT = Category(lambda dice: 30, condition=is_straight(1, 6))
BIG_STRAIGHT = Category(lambda dice: 30, condition=is_straight(2, 7))
CHOICE = Category(sum)
