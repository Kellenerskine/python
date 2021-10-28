# To Do:
# TODO: finish SC constructor DONE
# TODO: add starting value parameter to BC, LC, EC, & FLC DONE
# TODO: match existing classes to class diagram
# TODO: create EnumCounter (?), Date, Clock12, and Clock24 classes
# TODO: doctests


class Neighbor:
    """Neighbor represents an object that can:
    1) Connect to one or more neighbors (and be connected to also), and
    2) Notify those neighbors when it overflows,
        asking them to increment or reset themselves.
    """

    def __init__(self):
        self.increment_neighbors = []
        self.reset_neighbors = []

    def __str__(self):
        return (str(self.get_neighbor()) if self.get_neighbor() is not None else "") + str(self.get_value())

    def increment(self):
        self.notify_increment()
        self.notify_reset()

    def reset(self):
        pass

    def get_value(self):
        pass

    def add_increment(self, new_neighbor):
        if new_neighbor not in self.increment_neighbors:
            self.increment_neighbors.append(new_neighbor)
        return self

    def remove_increment(self, old_neighbor):
        if old_neighbor in self.increment_neighbors:
            self.increment_neighbors.remove(old_neighbor)

    def notify_increment(self):
        """Notifies all increment neighbors of overflow"""
        for neighbor in self.increment_neighbors:
            neighbor.increment()

    def add_reset(self, new_neighbor):
        if new_neighbor not in self.reset_neighbors:
            self.reset_neighbors.append(new_neighbor)
        return self

    def remove_reset(self, old_neighbor):
        if old_neighbor in self.reset_neighbors:
            self.reset_neighbors.remove(old_neighbor)

    def notify_reset(self):
        for neighbor in self.reset_neighbors:
            neighbor.reset()

    def get_neighbor(self):
        """Returns first neighbor, for printing"""
        return self.increment_neighbors[0] if len(self.increment_neighbors) >= 1 else None


class BoundedCounter(Neighbor):
    def __init__(self, lower_bound, upper_bound, val=None):
        """
        # >>> bit = BoundedCounter(0, 1)
        # >>> bit == None
        # False
        # >>> type(bit) == BoundedCounter
        # True
        # >>> bit.lower_bound
        # 0
        # >>> bit.upper_bound
        # 1
        # >>> bit.current_value
        # 0
        """
        super().__init__()
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound

        if self.current_value is not None:
            self.current_value = val
        else:
            self.current_value = lower_bound

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
            self.notify_increment()
            self.notify_reset()
        else:
            self.current_value += 1

    def reset(self):
        self.current_value = self.lower_bound

    def get_value(self):
        return self.current_value


class ListCounter(BoundedCounter):
    def __init__(self, items, val=None):
        self.items = tuple(items)
        super().__init__(0, len(self.items) - 1)
        if val is not None:
            self.current_value = items.index(val)

    def get_value(self):
        return self.items[super().get_value()]


class FixedLengthCounter(BoundedCounter):
    def __init__(self, lo, hi, length, val=None):
        super().__init__(lo, hi)
        self.length = length

    def get_value(self):
        return f"{super().get_value():0{self.length}}"


class StaticConnector(Neighbor):
    def __init__(self, string):
        super().__init__()
        self.string = string

    def get_value(self):
        return self.string


class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
            months[2] = 29
        self.year = BoundedCounter(1752, 9999, y)
        self.month = ListCounter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], m).add_increment(self.year)
        self.day = BoundedCounter(1, months[m], d).add_increment(self.month)

    def __repr__(self):
        return f"{self.day.current_value}, {self.month.current_value}, {self.year.current_value}"

    def __str__(self):
        return f"{self.year.current_value}-{self.month.current_value + 1}-{self.day.current_value}"

    def next_day(self):
        """
        >>> next = Date(2021, 5, 1)
        >>> next.next_day()
        2021-5-2
        """
        self.day.increment()
        print(self)


class Clock12:
    def __init__(self, h, m):
        pass


class Clock24:
    def __init__(self, ):
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # bit4 = FixedLengthCounter(0, 1, 2)
    # plus = StaticConnector("+").add_increment(bit4)
    # bit2 = BoundedCounter(0, 1).add_increment(plus)
    # dash = StaticConnector("-").add_increment(bit2)
    # bit1 = BoundedCounter(0, 1).add_increment(dash)
    # for _ in range(20):
    #     print(bit1)
    #     bit1.increment()

# year bounds: 1752 - 9999
