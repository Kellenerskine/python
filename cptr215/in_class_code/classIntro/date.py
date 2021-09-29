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

    def print(self):
        """Outputs self in MMM d, yyy format.
        >>> Date(2021, 9, 27)
        Sep 27, 2021
        >>> independence = Date(1776, 7, 4)
        >>> independence.print()
        Jul 4, 1776
        """
        month_name = "not Jan Feb Mar Apr May Jun Aug Sep Oct Nov Dec".split()[self.month]
        print(f"{month_name} {self.day}, {self.year}")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
