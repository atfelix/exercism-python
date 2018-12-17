def is_paired(string):
    starting_pairs = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    ending_pairs = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    stack = []
    for char in string:
        if char in starting_pairs:
            stack.append(char)
        elif stack and char in ending_pairs:
            if ending_pairs[char] != stack[-1]:
                return False
            else:
                stack.pop()
        elif char in ending_pairs:
            return False
    return len(stack) == 0