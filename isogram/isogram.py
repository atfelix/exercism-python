from collections import Counter

def is_isogram(string):
    string = string.lower().replace(' ', '').replace('-', '')
    counter = Counter(string)
    return not any(counter[x] > 1 for x in counter)