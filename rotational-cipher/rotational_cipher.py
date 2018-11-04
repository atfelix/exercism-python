def rotate(text, key):
    return ''.join(map(lambda x: rotate_char_if_alpha(x, key), text))

def rotate_char_if_alpha(ch, key):
    assert(is_char(ch))
    if not ch.isalpha():
        return ch

    return rotate_upper(ch, key) if ch.isupper() else rotate_lower(ch, key)

def is_char(ch):
    return ch.isalpha and len(ch) == 1

def rotate_upper(ch, key, alphabet_length=26):
    assert(ch.isupper())
    return rotate_char(ch, key, 'A')

def rotate_lower(ch, key, alphabet_length=26):
    assert(ch.islower())
    return rotate_char(ch, key, 'a')

def rotate_char(ch, key, base_char, alphabet_length=26):
    assert(ch.isalpha() and len(ch) == 1)
    order = ord(ch) - ord(base_char)
    order += key
    order %= alphabet_length
    return chr(order + ord(base_char))