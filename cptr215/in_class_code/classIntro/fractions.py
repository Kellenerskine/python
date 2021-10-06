class Fraction:
    def __init__(self, numerator, denominator):
        """Initializes a fraction.
        """
        # simply using the euclidean algorithm
        a, b = numerator, denominator
        while b != 0:
            a, b = b, a % b

        self.numerator = numerator // a
        self.denominator = denominator // a
        while denominator != 0:
            numerator, denominator = denominator, numerator % denominator

    def __repr__(self):
        """
        >>> one_third = Fraction(1, 3)
        >>> one_third
        Fraction(1, 3)
        >>> Fraction(2, 4)
        Fraction(1, 2)
        >>> Fraction(768, 1024)
        Fraction(3, 4)
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        """Human readable representation, num/den
        >>> print(Fraction(1, 2))
        1/2
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
        >>> half + third # half.__add__(third), and also Fraction.__add__(helf, third)
        Fraction(5, 6)
        >>>Fraction(1, 4) + Fraction(2, 8)
        Fraction(1, 2)
        """
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator, self.denominator * other.denominator)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
