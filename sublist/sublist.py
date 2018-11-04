EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"

def check_lists(first_list, second_list):
    if is_equal(first_list, second_list):
        return EQUAL
    elif is_sub_list(first_list, second_list):
        return SUBLIST
    elif is_super_list(first_list, second_list):
        return SUPERLIST
    else:
        return UNEQUAL

def is_equal(first, second):
    return len(first) == len(second) and first == second

def is_sub_list(first, second):
    return len(first) < len(second) and any(first == second[i:i + len(first)] for i in range(len(second) - len(first) + 1))

def is_super_list(first, second):
    return len(second) < len(first) and is_sub_list(second, first)