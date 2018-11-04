from collections import Counter

def detect_anagrams(word, candidates):
    return list(filter(lambda candidate: is_anagram(word, candidate), candidates))

def is_anagram(s, t):
    s = s.lower()
    t = t.lower()
    return len(s) == len(t) and s != t and Counter(s) == Counter(t)