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
        >>> bit = BoundedCounter(0, 1)
        >>> bit == None
        False
        >>> type(bit) == BoundedCounter
        True
        >>> bit.lower_bound
        0
        >>> bit.upper_bound
        1
        >>> bit = BoundedCounter(4, 9, 5)
        >>> bit.increment()
        >>> bit.current_value
        6
        """
        super().__init__()
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound

        if self.current_value is not None:
            self.current_value = val
        else:
            self.current_value = self.lower_bound

    def increment(self):
        """
        >>> digit = BoundedCounter(0, 9)
        >>> digit.increment()
        >>> digit.current_value()
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

    def __repr__(self):
        return f"BoundedCounter({self.lower_bound}, {self.upper_bound}, {self.current_value})"


class ListCounter(BoundedCounter):
    def __init__(self, items, val=None):
        """
        >>> bit = ListCounter([0, 1, 2, 3, 4, 5, 6, 7, 8], 4)
        >>> bit.increment()
        >>> bit.current_value
        5
        >>> bit = ListCounter([0, 1, 2, 3, 4, 6, 7, 8], 4)
        >>> bit.increment()
        >>> bit.get_value()
        6
        """
        self.items = tuple(items)
        super().__init__(0, len(self.items) - 1)
        if val is not None:
            self.current_value = items.index(val)

    def get_value(self):
        return self.items[super().get_value()]

    def __repr__(self):
        return f"ListCounter({self.items}, {self.get_value()})"


class FixedLengthCounter(BoundedCounter):
    def __init__(self, lo, hi, val=None, length=1):
        """
        >>> bit = FixedLengthCounter(0, 9, 6)
        >>> bit.increment()
        >>> bit.current_value
        7
        >>> bit = FixedLengthCounter(5, 20, 8)
        >>> bit.increment()
        >>> bit.current_value
        9
        """
        super().__init__(lo, hi, val)
        self.length = length

    def get_value(self):
        return f"{super().get_value():0{self.length}}"

    def __repr__(self):
        return f"FixedLengthCounter({self.lower_bound}, {self.upper_bound}, {self.current_value}, {self.length})"


class StaticConnector(Neighbor):
    def __init__(self, string):
        """
        >>> bit = StaticConnector(":")
        >>> bit.get_value()
        ':'
        >>> bit = StaticConnector("!")
        >>> bit.get_value()
        '!'
        """
        super().__init__()
        self.string = string

    def get_value(self):
        return self.string

    def __repr__(self):
        return f"StaticConnector({self.string})"


class Date:
    def __init__(self, y, m, d):
        """
        >>> bit = Date(2002, 5, 3)
        >>> bit.next_day()
        2002-5-4
        >>> bit = Date(2002, 1, 31)
        >>> bit.next_day()
        2002-2-1
        """
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
        return f"Date({self.year.get_value()}, {self.month.get_value()}, {self.day.get_value()})"

    def __str__(self):
        return f"{self.year.get_value()}-{self.month.get_value()}-{self.day.get_value()}"

    def next_day(self):
        """
        >>> next = Date(2021, 5, 1)
        >>> next.next_day()
        2021-5-2
        """
        self.day.increment()
        print(self)


class Clock12:
    def __init__(self, h, m, day_half="PM"):
        """
        >>> bit = Clock12(4, 30)
        >>> bit.next_minute()
        PM 4:31
        >>> bit = Clock12(4, 59)
        >>> bit.next_minute()
        PM 5:00
        """
        self.h = h
        self.m = m
        self.day_half = day_half

        # self.hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.ampm = ListCounter(["AM", "PM"], day_half)
        self.space = StaticConnector(" ").add_increment(self.ampm)
        self.hour = ListCounter([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], h).add_increment(self.space)
        self.colon = StaticConnector(':').add_increment(self.hour)
        # self.minute = BoundedCounter(0, 59, m).add_increment(self.colon)
        self.minute = FixedLengthCounter(0, 59, m, 2).add_increment(self.colon)

    def __repr__(self):
        return f"Clock12({self.hour.current_value},{self.space}{self.minute.current_value})"

    def __str__(self):
        return str(self.minute)

    def next_minute(self):
        """
        >>> next_time = Clock12(1, 30, 'AM')
        >>> next_time.next_minute()
        AM 1:31
        >>> next_time = Clock12(2, 58, "PM")
        >>> next_time.next_minute()
        PM 2:59
        >>> next_time = Clock12(11, 59, "AM")
        >>> next_time.next_minute()
        PM 12:00
        >>> next_time = Clock12(11, 59, "PM")
        >>> next_time.next_minute()
        AM 12:00
        >>> next_time = Clock12(11, 3, "PM")
        >>> next_time.next_minute()
        PM 11:04
        """
        self.minute.increment()
        print(self)


class Clock24:
    def __init__(self, h, m):
        """
        >>> bit = Clock24(5, 20)
        >>> bit.next_time()
        05:21
        >>> bit = Clock24(5, 59)
        >>> bit.next_time()
        06:00
        """
        self.h = h
        self.m = m

        self.hour = FixedLengthCounter(1, 24, h, 2)
        self.colon = StaticConnector(":").add_increment(self.hour)
        self.minute = FixedLengthCounter(0, 59, m, 2).add_increment(self.colon)

    def __repr__(self):
        return f"Clock24({self.hour.current_value}, {self.minute.current_value})"

    def __str__(self):
        return str(self.minute)
        # return f"{self.hour.get_value()}{self.colon.get_value()}{self.minute.get_value()}"

    def next_time(self):
        """
        >>> next_time = Clock24(13, 1)
        >>> next_time.next_time()
        13:02
        >>> next_time = Clock24(24, 59)
        >>> next_time.next_time()
        01:00
        """
        self.minute.increment()
        print(self)


# Demo
if __name__ == "__main__":
    import doctest

    # demo for Date:
    print("12hr or 24hr or Date?")
    time_mode = input("which format would you like?")
    if time_mode == "12hr":
        time_initial = input("Enter in the following format: hours,minutes,'AM/PM'   ")
        time_lst = time_initial.split(",")
        result = Clock12(int(time_lst[0]), int(time_lst[1]), time_lst[2].upper())
        print("The next minute is: ", end='')
        result.next_minute()
    elif time_mode == "24hr":
        time_initial = input("Enter in the following format: hour,minute   ")
        time_lst = time_initial.split(",")
        result = Clock24(int(time_lst[0]), int(time_lst[1]))
        print("The next minute is: ")
        result.next_time()
    elif time_mode == "date":
        date_initial = input("Enter in the following format: year,month,day   ")
        date_lst = date_initial.split(",")
        result = Date(int(date_lst[0]), int(date_lst[1]), int(date_lst[2]))
        print("The next day is: ", end='')
        result.next_day()

    doctest.testmod()
