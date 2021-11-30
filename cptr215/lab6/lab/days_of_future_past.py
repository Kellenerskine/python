class Date:
    def __init__(self, year, month, day):
        """Initializes a date given a year, month, and day.
        >>> today = Date(2021, 9, 27)
        >>> today.day
        27
        >>> Date(1776, 7, 4).year
        1776
        """
        self.year = year
        self.month = month
        self.day = day

    def day_of_week(self):
        """Determines the day of the week self falls on. 1 = Sun thru 7 = Sat.
        >>> today = Date(2021, 9, 27)
        >>> today.day_of_week()
        2
        >>> Date(2021, 9, 25).day_of_week()
        7
        >>> Date(1776, 7, 4).day_of_week()
        5
        """
        if self.month < 3:
            m = self.month + 12
            y = self.year - 1
        else:
            m = self.month
            y = self.year
        dow = (self.day + (13 * (m + 1)) // 5 + y + y // 4 - y // 100 + y // 400) % 7
        return 7 if dow == 0 else dow

    def __str__(self):
        """Returns a human-readable string representation of self
        in MMM d, yyyy format.
        >>> Date(2000, 1, 1).__str__() # not common
        'Jan 1, 2000'
        >>> str(Date(2021, 9, 27))
        'Sep 27, 2021'
        >>> independence = Date(1776, 7, 4)
        >>> print(independence)
        Jul 4, 1776
        """
        month_name = "BAD Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[self.month]
        return f"{month_name} {self.day}, {self.year}"

    def __repr__(self):
        """Returns a string that would evaluate to an identical Date object.
        >>> Date(2021, 9, 29).__repr__() # not common
        'Date(2021, 9, 29)'
        >>> Date(1970, 12, 31)
        Date(1970, 12, 31)
        >>> repr(Date(1984, 2, 20))
        'Date(1984, 2, 20)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"

    def is_leap_year(self):
        """Determines whether self is in a leap year.
                    Truth Table
            4s place  2s place  1s place
             div 4 | div 100 | div 400 | leap?
            -------+---------+---------+-------
               0         0         0       0
               0         0         1       X
               0         1         0       X
               0         1         1       X
               1         0         0       1
               1         0         1       X
               1         1         0       0
               1         1         1       1
        >>> Date(2021, 9, 29).is_leap_year()
        False
        >>> Date(1984, 4, 27).is_leap_year()
        True
        >>> Date(2000, 1, 1).is_leap_year()
        True
        >>> Date(1900, 11, 30).is_leap_year()
        False
        """
        return self.year % 400 == 0 or \
               (self.year % 4 == 0 and self.year % 100 != 0)

    # TODO: add the proper logic to the following functions

    def previous_day(self):
        """input a date and output the day before
        >>> Date(2021, 9, 20).previous_day()
        Date(2021, 9, 19)
        >>> Date(2021, 3, 1).previous_day()
        Date(2021, 2, 28)
        >>> Date(1984, 3, 1).previous_day()
        Date(1984, 2, 29)
        >>> Date(2002, 1, 1).previous_day()
        Date(2001, 12, 31)
        """

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.month == 3) and self.is_leap_year() and (self.day == 1):
            return Date(self.year, self.month - 1, 29)
        elif self.month == 1 and self.day == 1:
            return Date(self.year - 1, self.month + 11, days_in_month[12])
        elif self.day == 1:
            return Date(self.year, self.month - 1, days_in_month[self.month - 1])
        else:
            return Date(self.year, self.month, self.day - 1)

    def next_day(self):
        """input a date and output the day after
        >>> Date(2021, 9, 20).next_day()
        Date(2021, 9, 21)
        >>> Date(2021, 2, 28).next_day()
        Date(2021, 3, 1)
        >>> Date(1984, 2, 28).next_day()
        Date(1984, 2, 29)
        >>> Date(2002, 12, 31).next_day()
        Date(2003, 1, 1)
        >>> Date(8612, 3, 1).next_day()
        Date(8612, 3, 2)
        >>> Date(6340, 3, 1).next_day()
        Date(6340, 3, 2)
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.month == 2) and self.is_leap_year() and (self.day == 28):
            return Date(self.year, self.month, 29)

        elif self.month == 12 and self.day == 31:
            return Date(self.year + 1, self.month - 11, 1)

        elif days_in_month[self.month] == self.day:
            return Date(self.year, self.month + 1, 1)
        else:
            return Date(self.year, self.month, self.day + 1)

    def equals(self, other):
        """tests to see if the dates are the same and if so returns true
        >>> Date(2002, 4, 9).equals(Date(2002, 4, 9))
        True
        """
        if (self.year == other.year) and (self.month == other.month) and (self.day == other.day):
            return True
        else:
            return False

    def before(self, other):
        """tests to see if one date is before another
        >>> Date(2021, 5, 8).before(Date(2021, 4, 7))
        False
        >>> Date(2021, 5, 8).before(Date(2021, 5, 9))
        True
        >>> Date(2021, 7, 8).before(Date(2021, 6, 9))
        False
        >>> Date(2021, 7, 8).before(Date(2021, 8, 7))
        True
        >>> Date(2020, 7, 8).before(Date(2021, 7, 11))
        True
        >>> Date(2020, 8, 9).before(Date(2019, 4, 9))
        False
        """
        if self.year < other.year:
            return True
        elif (self.year == other.year) and (self.month < other.month):
            return True
        elif (self.year == other.year) and (self.month == other.month) and (self.day < other.day):
            return True
        else:
            return False

    def after(self, other):
        """tests to see if one date is after another
        >>> Date(2021, 5, 8).after(Date(2021, 4, 7))
        True
        >>> Date(2021, 5, 8).after(Date(2021, 5, 9))
        False
        >>> Date(2021, 7, 8).after(Date(2021, 6, 9))
        True
        >>> Date(2021, 7, 8).after(Date(2021, 8, 7))
        False
        >>> Date(2020, 7, 8).after(Date(2021, 7, 11))
        False
        >>> Date(2020, 8, 9).after(Date(2019, 4, 9))
        True
        """
        if self.year > other.year:
            return True
        elif (self.year == other.year) and (self.month > other.month):
            return True
        elif (self.year == other.year) and (self.month == other.month) and (self.day > other.day):
            return True
        else:
            return False

    # TODO: override addition, subtraction, and comparison operators for the following functions

    def Offset(self, offset):
        """
        >>> Date(2021, 5, 8).Offset(-3)
        Date(2021, 5, 5)
        >>> Date(2021, 5, 8).Offset(3)
        Date(2021, 5, 11)
        >>> Date(2021, 5, 20).Offset(22)
        Date(2021, 6, 11)
        """

        new_date = Date(self.year, self.month, self.day)

        if offset > 0:
            for i in range(offset):
                new_date = new_date.next_day()
        else:
            for i in range(abs(offset)):
                new_date = new_date.previous_day()
        return new_date

    def distance(self):
        pass

    def comparison(self):
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# test = Date(2021, 8, 27)
# test.offset(5)
# print(test)
