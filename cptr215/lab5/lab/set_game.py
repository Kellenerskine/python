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
        #objectives:
        #1.compare all attributes of the cards
        #2.find a card that matches a specific atribute that both cards share
        #3.output that card using repr
        #4.check when there is no equivalent card
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card1))
        3FGP
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(2, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card2.third_card(card1))
        2FGP
        """
        fill_options = "ESF"
        color_options = "RGB"
        shape_options = "QOP"
        num_is_same = 0
        fill_is_same = 0
        color_is_same = 0
        shape_is_same = 0

        first_card = str(self)
        second_card = str(other)
        result = ""

        # statements for if the numbers are the same
        if first_card[0] == second_card[0]:  # assigns the number of shapes
            result += str(first_card[0])
            num_is_same = 1
            # making sure that every other thing is different
            if num_is_same == 1:
                fill_options = fill_options.replace(str(first_card[1]), "")
                fill_options = fill_options.replace(str(second_card[1]), "")
                result += fill_options
            if num_is_same == 1:
                color_options = color_options.replace(str(first_card[2]), "")
                color_options = color_options.replace(str(second_card[2]), "")
                result += color_options
            if num_is_same == 1:
                shape_options = shape_options.replace(str(first_card[3]), "")
                shape_options = shape_options.replace(str(second_card[3]), "")
                result += shape_options
            return result
        else:
            # finding the correct 3rd num
            for i in range(1, 4):  # assigns a different first num than the previous two cards
                if str(i) != first_card[0] and str(i) != second_card[0]:
                    result += str(i)
            if first_card[1] == second_card[1]:
                pass
            if first_card[2] == second_card[2]:
                pass
            if first_card[3] == second_card[3]:
                pass

        #TODO: maybe use an elif?



def make_deck():
    """Returns a list containing a complete Set deck with 81 unique cards."""


def is_set(card1, card2, card3):
    """Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)
    1.call third card on two of the cards, check if the third on equals the thirds card given
    """


if __name__ == "__main__":
    import doctest

    # user_input = input("type something appropriate: ")
    # user_input.split()
    # inp1 = user_input[0]
    # inp2 = user_input[1]
    # results = SetCard.third_card(inp1, inp2)
    # print(results)
    doctest.testmod()
