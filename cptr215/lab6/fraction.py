"""Fractions
Prof. O & CPTR-215
2021-10-06 first draft

TDD = Test-Driven Development
No production code is written without a failing test to necessitate it.
Steps:
1. Write a test
2. See it fail
3. Write just enough code to make it pass
4. See it pass
5.   Or revise until passes
6. Refactor
7. Repeat

YAGNI = You Ain't Gonna Need It
"""


class Fraction:
    def __init__(self, numerator, denominator=1):
        """Initializes a fraction and gets the reduced form.
        >>> one_third = Fraction(1, 3)
        """
        # Simplify using the Euclidean algorithm
        # https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
        a, b = numerator, denominator
        while b != 0:
            a, b = b, a % b
            # a = b
            # b = a % b
        self.numerator = numerator // a
        self.denominator = denominator // a

    def __repr__(self):
        """Python-executable representation
        >>> one_third = Fraction(1, 3)
        >>> one_third
        Fraction(1, 3)
        >>> Fraction(2, 4)
        Fraction(1, 2)
        >>> Fraction(768, 1024)
        Fraction(3, 4)
        >>> Fraction(5, 1)
        Fraction(5)
        """
        return f"Fraction({self.numerator}, {self.denominator})" if self.denominator != 1 else f"Fraction({self.numerator})"

    def __str__(self):
        """Human-readable representation, num/den
        >>> print(Fraction(1, 2))
        1/2
        >>> print(Fraction(1, 2) + Fraction(1, 2))
        1
        >>> print(Fraction(2, 3) + Fraction(4, 3))
        2
        """
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

    def __add__(self, other):
        """
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        >>> half = Fraction(1, 2)
        >>> third = Fraction(1, 3)
        >>> half + third # same as half.__add__(third), and also Fraction.__add__(half, third)
        Fraction(5, 6)
        >>> Fraction(1, 4) + Fraction(2, 8)
        Fraction(1, 2)

        """
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        """
        >>> Fraction(1, 2) - Fraction(1, 3)
        Fraction(1, 6)
        >>> half = Fraction(1, 2)
        >>> third = Fraction(1, 3)
        >>> half - third # same as half.__add__(third), and also Fraction.__add__(half, third)
        Fraction(1, 6)
        >>> Fraction(1, 4) - Fraction(2, 8)
        Fraction(0)
        """

        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        """
        >>> Fraction(1, 2) * Fraction(1, 3)
        Fraction(1, 6)
        >>> half = Fraction(1, 2)
        >>> third = Fraction(1, 3)
        >>> half * third # same as half.__add__(third), and also Fraction.__add__(half, third)
        Fraction(1, 6)
        >>> Fraction(1, 4) * Fraction(2, 8)
        Fraction(1, 16)
        >>> Fraction(1, 4) * Fraction(2, 8)
        Fraction(1, 16)
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """
        >>> Fraction(1, 2) / Fraction(1, 3)
        Fraction(3, 2)
        >>> half = Fraction(1, 2)
        >>> third = Fraction(1, 3)
        >>> half / third # same as half.__add__(third), and also Fraction.__add__(half, third)
        Fraction(3, 2)
        >>> Fraction(1, 4) / Fraction(2, 8)
        Fraction(1)
        """
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        """
        >>> Fraction(1, 2) == Fraction(1, 3)
        False
        >>> Fraction(1, 4) == Fraction(2, 8)
        True
        """
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        >>> Fraction(1, 2) < Fraction(1, 3)
        False
        >>> Fraction(1, 4) < Fraction(2, 8)
        False
        >>> Fraction(1, 2) < Fraction(1, 8)
        False
        >>> Fraction(1, 8) < Fraction(1, 2)
        True
        """
        if (self.numerator * other.denominator) < (self.denominator * other.numerator):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        >>> Fraction(1, 2) > Fraction(1, 3)
        True
        >>> Fraction(1, 4) > Fraction(2, 8)
        False
        >>> Fraction(1, 2) > Fraction(1, 8)
        True
        >>> Fraction(1, 8) > Fraction(1, 2)
        False
        >>> Fraction(3, 14) > Fraction(2, 11)
        True
        """
        if self < other or self == other:
            return False
        else:
            return True

    def __ge__(self, other):
        """
        >>> Fraction(1, 2) >= Fraction(1, 3)
        True
        >>> Fraction(1, 4) >= Fraction(2, 8)
        True
        >>> Fraction(1, 9) >= Fraction(1, 2)
        False
        """
        if self > other or self == other:
            return True
        else:
            return False

    def __le__(self, other):
        """
        >>> Fraction(1, 2) <= Fraction(1, 3)
        False
        >>> Fraction(1, 4) <= Fraction(2, 8)
        True
        >>> Fraction(1, 9) <= Fraction(1, 2)
        True
        """
        if self < other or self == other:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        >>> Fraction(1, 2) != Fraction(1, 3)
        True
        >>> Fraction(1, 4) != Fraction(2, 8)
        False
        >>> Fraction(2, 5) != Fraction(2, 5)
        False
        >>> Fraction(2, 5) != Fraction(2, 6)
        True
        """

        return not self == other


if __name__ == "__main__":
    import doctest

    doctest.testmod()
