from __future__ import division, annotations
import math


class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        gcd = math.gcd(numer, denom)
        self.numer: int = int(math.copysign(numer, numer * denom)) // gcd
        self.denom: int = abs(denom) // gcd

    def __eq__(self, other: Rational):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other: Rational):
        return Rational(
            self.numer * other.denom + self.denom * other.numer,
            self.denom * other.denom,
        )

    def __sub__(self, other: Rational):
        return Rational(
            self.numer * other.denom - self.denom * other.numer,
            self.denom * other.denom,
        )

    def __mul__(self, other: Rational):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: Rational):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power: int):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base: int) -> float:
        return base ** (self.numer / self.denom)
