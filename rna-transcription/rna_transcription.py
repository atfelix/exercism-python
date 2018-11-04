from functools import reduce

def to_rna(dna_strand):
    if is_not_valid(dna_strand):
        raise ValueError

    return replace(dna_strand, {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'})

def is_not_valid(dna_strand, alphabet='ACGT'):
    return any(ch not in alphabet for ch in dna_strand)

def replace(string, dictionary):
    return reduce(lambda x, y: x + dictionary[y], string, '')