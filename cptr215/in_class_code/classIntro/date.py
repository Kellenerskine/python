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
        """Determines the day of the week self falls on. 1 = Sun through 7 = Sat.
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
        # i wrote the above zeller form wrong, program therefore does not work.
        return 7 if dow == 0 else dow

    def __str__(self):
        """Outputs self in MMM d, yyy format.
        >>> Date(2000, 1, 1).__str__() # not common
        'Jan 1, 2000'
        >>> str(Date(2021, 9, 27))
        'Sep 27, 2021'
        >>> independence = str(Date(1776, 7, 4))
        >>> print(independence)
        Jul 4, 1776
        """
        month_name = "not Jan Feb Mar Apr May Jun Aug Sep Oct Nov Dec".split()[self.month]
        print(f"{month_name} {self.day}, {self.year}")

    def __repr__(self):
        """Returns a string that would evaluate to an identical Date object
        >>> Date(2021, 9, 29).__repr__() #still not common
        'Date(2021, 9, 29)'
        >>> Date(1970, 12, 31)
        Date(1970, 12, 31)
        >>> repr(Date(1984, 2, 20))
        'Date(1984, 2, 20)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"

    def is_leap_year(self):
    """determines whether self is in a leap year
    >>> Date(2021, 9, 29).is_leap_year()
    False
    >>> Date(1984, 4, 27).is_leap_year()
    True
    >>> Date(2000, 1, 1).is_leap_year()
    True
    >>> Date(1900, 11, 30).is_leap_year()
    False
    """
    return self.year %


if __name__ == '__main__':
    import doctest

    doctest.testmod()
