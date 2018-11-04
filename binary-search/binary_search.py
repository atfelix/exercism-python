def binary_search(list_of_numbers, number):
    index = left_insertion_index(list_of_numbers, number)

    if not 0 <= index < len(list_of_numbers) or list_of_numbers[index] != number:
        raise ValueError('number is not in list_of_numbers')

    return index

def left_insertion_index(sorted_list, element):
    """
    @param sorted_list: an ascending list
    @param element:  search parameter to query sorted_list for
    @return:  returns i where all e sorted_list[:i] all satisfy 
    e < element and all e in sorted_list[i:] satisfy element <= e.
    """
    low, high = 0, len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < element:
            low = mid + 1
        else:
            high = mid

    return low