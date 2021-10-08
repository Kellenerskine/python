# all three characteristics diff or all same
from enum import Enum


class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Shape(Enum):
    QUAD = 5
    OVAL = 17
    PYRAMID = 234


class SetCard:
    def __init__(self, number, fill, color, shape):
        """int in [1,3], Fill, Color, Shape -> SetCard"""
        self.number = number
        self.fill = fill
        self.color = color
        self.shape = shape

    def __str__(self):
        """Human-readable representation of this card.
        >>> str(SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL))
        '1SBO'
        >>> str(SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD))
        '2ERQ'
        """
        return f"{self.number}{self.fill.name[0]}{self.color.name[0]}{self.shape.name[0]}"

    def __repr__(self):
        """Python code to recreate this card.
        >>> SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> repr(SetCard(2,Fill.EMPTY,Color.RED,Shape.QUAD))
        'SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)'
        """
        return f"SetCard({self.number}, {self.fill}, {self.color}, {self.shape})"

    def third_card(self, other):
        """Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card1))
        3FGP
        """

        card1 = str(self)
        card2 = str(other)

        for j in card1:
            for k in card2:
                if j == k:
                    print(j,k)



def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.'''


def is_set(card1, card2, card3):
    '''Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)'''
