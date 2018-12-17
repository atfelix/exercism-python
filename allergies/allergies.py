class Allergies(object):

    allergens = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.score & Allergies.allergens[item] != 0

    @property
    def lst(self):
        return sorted(set(x for x in Allergies.allergens
                        if self.is_allergic_to(x)), key=lambda x: x[1])