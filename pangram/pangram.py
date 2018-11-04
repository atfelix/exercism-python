def is_pangram(sentence):
    return set(filter(lambda x: x.isalpha(), sentence.lower())) == set('abcdefghijklmnopqrstuvwxyz')
