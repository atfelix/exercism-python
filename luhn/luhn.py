class Luhn(object):
    def __init__(self, card_num):
        self.luhn_validity = is_valid_luhn(card_num)

    def is_valid(self):
        return self.luhn_validity

def is_valid_luhn(card_num):
    if any(not (char.isdigit() or char.isspace()) for char in card_num):
        return False

    digits = [int(char) for char in reversed(card_num) if char.isdigit()]

    if len(digits) <= 1:
        return False

    return luhn_count(digits) == 0

def luhn_count(digits):
    count = 0
    for index, digit in enumerate(digits):
        count += luhn_lookup(index, digit)
    return count % 10

def luhn_lookup(index, digit, digit_lookup=(0, 2, 4, 6, 8, 1, 3, 5, 7, 9)):
    if index % 2 != 1:
        return digit
    else:
        return digit_lookup[digit]
