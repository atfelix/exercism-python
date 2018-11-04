from __future__ import division
from math import gcd

class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __eq__(self, other):
        return self.numer * other.denom == other.numer * self.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a, b, c, d = self.numer, self.denom, other.numer, other.denom
        return Rational(a * d + b * c, b * d)

    def __sub__(self, other):
        return self + other * Rational(-1, 1)

    def __mul__(self, other):
        a, b, c, d = self.numer, self.denom, other.numer, other.denom
        return Rational(a * c, b * d)

    def __truediv__(self, other):
        return self * Rational(other.denom, other.numer)

    def __abs__(self):
        return self if (self.numer < 0) == (self.denom < 0) else self * Rational(-1, 1)

    def __pow__(self, power):
        return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return pow(base, self.numer / self.denom)
