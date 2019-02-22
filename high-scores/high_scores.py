from functools import reduce
from heapq import nlargest

class HighScores(object):
    def __init__(self, scores, limit=3):
        self.scores = scores
        self.top_three = nlargest(limit, scores)

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return self.top_three

    def report(self):
        beginning = f'Your latest score was {self.latest()}'
        if self.personal_best() == self.latest():
            ending = 'That\'s your personal best!'
        else:
            ending = f'That\'s {self.personal_best() - self.latest()} short of your personal best!'
        return f'{beginning}. {ending}'