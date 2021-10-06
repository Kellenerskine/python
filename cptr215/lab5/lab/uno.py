class UnoCard:
    def __init__(self, color, rank):
        """takes a color (string, one character of "RGBYK") and a rank (string, one of 0-9, S, D, R for the first 4 colors,
        and Wild or Draw Four for blacK)

        """
        self.color = color
        self.rank = rank

    def can_be_played_on(self, other):
        """takes another card and determines whether this card can be played on it, following standard rules
        (matches color or number/symbol, or is a Wild/Draw Four).

        """
    def score_value(self):
        pass

    def __repr__(self):
        pass
    def __str__(self):
        pass

