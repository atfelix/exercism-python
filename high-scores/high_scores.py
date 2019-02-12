from functools import reduce

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self, limit=3):
        return reduce(
            lambda triple, score: sorted(triple + [score], reverse=True)[:limit],
            self.scores[limit:],
            sorted(self.scores[:limit], reverse=True)
        )

    def report(self):
        beginning = f'Your latest score was {self.latest()}'
        if self.personal_best() == self.latest():
            ending = 'That\'s your personal best!'
        else:
            ending = f'That\'s {self.personal_best() - self.latest()} short of your personal best!'
        return f'{beginning}. {ending}'