import random


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
        >>> UnoCard("B", "3").can_be_played_on(UnoCard("B", "4"))
        True
        >>> UnoCard("B", "3").can_be_played_on(UnoCard("R", "4"))
        False
        >>> UnoCard("B", "3").can_be_played_on(UnoCard("R", "3"))
        True
        >>> UnoCard("R", "D").can_be_played_on(UnoCard("B", "D"))
        True
        >>> UnoCard("K", "W").can_be_played_on(UnoCard("R", "R"))
        True
        """
        if self.color == other.color:
            return True
        elif self.rank == other.rank:
            return True
        elif self.color == "K":
            return True
        else:
            return False

    def score_value(self):
        """
        >>> UnoCard("K", "F").score_value()
        50
        >>> UnoCard("R", "S").score_value()
        20
        >>> UnoCard("Y", "D").score_value()
        20
        >>> UnoCard("G", "R").score_value()
        20
        >>> UnoCard("K", "W").score_value()
        50
        >>> UnoCard("R", "4").score_value()
        4
        """
        if self.color == "K":
            return 50
        elif self.rank == "S" or self.rank == "D" or self.rank == "R":
            return 20
        else:
            return int(self.rank)

    def __repr__(self):
        """

        """
        return f"UnoCard('{self.color}', '{self.rank}')"

    def __str__(self):
        """
        >>> str(UnoCard("G", "1"))
        'G1'
        >>> str(UnoCard("B", "2"))
        'B2'
        >>> str(UnoCard("Y", "6"))
        'Y6'
        >>> str(UnoCard("K", "F"))
        'KF'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        >>> str(UnoCard("K", "D"))
        'KD'
        """
        return f"{self.color}{self.rank}"


def create_deck():
    """returns a complete, shuffled Uno deck as a list of 108 UnoCard objects.

    """
    # TODO: make this a shuffled list of cards [works, if allowed to import random]
    # TODO: make sure all cards are included in this deck [done]

    deck = []
    count = 0
    colors = ["R", "G", "B", "Y"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "S", "D", "R"]
    wild_cards = ["W", "F"]
    new_list = []

    for color in colors:
        for value in values:
            card_val = f"{color}{value}"
            deck.append(card_val)
            count += 1
            if value != 0:  # adds a duplicate card if the val is not 0
                deck.append(card_val)
                count += 1
    for i in range(4):
        deck.append(f"K{wild_cards[0]}")
        deck.append(f"K{wild_cards[1]}")
        count += 2

    for i in deck:
        new_val = UnoCard(i[0], i[1])
        new_list.append(new_val)

    random.shuffle(new_list)

    return new_list


def deal_hands(deck, num_hands):  # (deck, num_hands)
    """returns a tuple of num_hands lists of 7 cards dealt from deck, 1 to each hand at a time (not all 7 to a single hand consecutively).
    Removes the cards that were dealt from the "top" of the deck (starting at position 0).
    """
    # deck = [0, 1, 2, 0, 1, "2", 0, 1, 2, 0, 1, 2]
    # num_hands = 3
    cards_drawn = []
    test_cards_drawn = () + tuple(cards_drawn)
    hands = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    # draws 28 cards from the deck from the top
    for i in range(7):
        for hand in range(num_hands):
            cards_drawn.append(deck.pop(0))
            card = cards_drawn.pop(0)
            hands[hand].append(card)

    # removes empty lists from hands
    hands = [x for x in hands if x != []]  # unsure of how this works...stack overflow...pls don't break :(

    return tuple(hands)


def hand_score(hand):
    """takes a list of UnoCards and returns the total score for that hand.
    # >>> hand_score(([]))
    """
    score = 0
    for i in hand:
        card_score = UnoCard.score_value(i)
        score += card_score

    return score

#
# # unoDeck = (create_deck())
# for i in create_deck():
#     strings = str(i)
#     print(repr(strings), end='')
print(create_deck())

