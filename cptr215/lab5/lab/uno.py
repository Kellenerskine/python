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

        """

    def score_value(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


def create_deck():
    """returns a complete, shuffled Uno deck as a list of 108 UnoCard objects.
    """
    # TODO: make this a shuffled list of cards [works, if allowed to import random]
    # TODO: make sure all cards are included in this deck [done]

    deck = []
    colors = ["R", "G", "B", "Y"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "S", "D", "R"]
    wild_cards = ["Wild", "Draw Four"]

    for color in colors:
        for value in values:
            card_val = f"UnoCard({color}, {value})"
            deck.append(card_val)
            if value != 0:  # adds a duplicate card if the val is not 0
                deck.append(card_val)
    for i in range(4):
        deck.append(wild_cards[0])
        deck.append(wild_cards[1])

    random.shuffle(deck)

    return deck


def deal_hands(deck, num_hands):
    """returns a tuple of num_hands lists of 7 cards dealt from deck, 1 to each hand at a time (not all 7 to a single hand consecutively).
    Removes the cards that were dealt from the "top" of the deck (starting at position 0).
    """

    cards_drawn = []
    hands = []
    for i in range(7):
        for hand in range(num_hands):
            cards_drawn.append(unoDeck.pop(0))








def hand_score(hand):
    """takes a list of UnoCards and returns the total score for that hand.
    """


unoDeck = create_deck()
print(deal_hands(create_deck(), 4))
