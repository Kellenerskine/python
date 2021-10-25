"""Bounded Counter
Prof. O & CPTR-215
2021-10-22 add doctests
2021-10-13 fix 12-hour clock using composition
2021-10-11 4-bit counter, 24-hour clock, (broken) 12-hour clock
2021-10-01 first draft
"""


class BoundedCounter:
    def __init__(self, lower_bound, upper_bound, neighbor=None):
        """
        >>> bit = BoundedCounter(0, 1)
        >>> bit == None
        False
        >>> type(bit) == BoundedCounter
        True
        >>> bit.lower_bound
        0
        >>> bit.upper_bound
        1
        >>> bit.current_value
        0
        >>> print(bit.neighbor)
        None
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound
        self.neighbor = neighbor

    def increment(self):
        """
        >>> digit = BoundedCounter(0, 9)
        >>> digit.increment()
        >>> digit.current_value
        1
        >>> for _ in range(8): digit.increment()
        >>> digit.get_value()
        9
        >>> digit.increment()
        >>> digit.get_value()
        0
        """
        if self.current_value == self.upper_bound:
            self.current_value = self.lower_bound
            if self.neighbor:
                self.neighbor.increment()
        else:
            self.current_value += 1

    def get_value(self):
        return self.current_value

    def __str__(self):
        return (str(self.neighbor) if self.neighbor else "") + str(self.current_value)


class ListCounter(BoundedCounter):
    def __init__(self, items, neighbor=None):
        self.items = tuple(items)
        BoundedCounter.__init__(self, 0, len(self.items) - 1, neighbor)

    def get_value(self):
        return self.items[self.current_value]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
