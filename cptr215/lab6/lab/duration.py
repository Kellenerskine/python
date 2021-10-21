class Duration:
    """
    >>> dur_almost_1_day = Duration(23, 59, 59)
    >>> dur_90_min = Duration("1:30:00")
    >>> dur_45_sec = Duration("0d0h45s")
    >>> dur_neg_45_sec = Duration("-45s")
    >>> dur_1_min = Duration(60) # number of seconds
    >>> dur_neg_45_sec
    Duration('-0:00:45')
    >>> str(dur_45_sec * (2 * 60))
    '1:30:00'
    >>> dur_90_min - dur_45_sec # you can represent it however you want, but the repr MUST look like this:
    Duration('1:29:15')
    >>> dur_45_sec - dur_90_min
    Duration('-1:29:15')
    >>> dur_45_sec - dur_45_sec
    Duration('0:00:00')
    >>> dur_45_sec + Duration('1m')
    Duration('0:01:45')
    >>> dur_45_sec > Duration('0:1:0') # add the other comparison operators!
    False
    >>> print(dur_45_sec + dur_neg_45_sec)
    0:00:00
    """

    def __init__(self, first_arg, second_arg=None, third_arg=None):
        self.time_lst = []
        self.day = ""
        self.days = ""
        self.total_seconds = 0
        self.is_negative = False
        self.hour = first_arg
        self.minute = second_arg
        self.second = third_arg
        if type(first_arg) is int:
            self.hour = first_arg
            self.minute = second_arg
            self.second = third_arg
            time_lst = [self.hour, self.minute, self.second]
        else:
            time_lst = list(first_arg)

        if "-" in time_lst:
            self.is_negative = True

    def to_seconds(self):
        # '-1:30:45'
        # '0d0h45s'

        if ":" in self.time_lst:
            self.hour = self.time_lst[len(self.time_lst) - 7]
            self.minute = self.time_lst[len(self.time_lst) - 5] + self.time_lst[len(self.time_lst) - 4]
            self.second = self.time_lst[len(self.time_lst) - 2] + self.time_lst[len(self.time_lst) - 1]
        elif "d" in self.time_lst:
            self.day = ""
            self.hour = ""
            self.minute = ""
            self.second = ""
            if "d" in self.time_lst:
                d_pos = self.time_lst.index("d")
                self.day = self.time_lst[0:d_pos]
                for i in self.day:
                    self.days += i
            if "h" in self.time_lst:
                h_pos = self.time_lst.index("h")
                if self.time_lst[h_pos - 2] != "d":
                    self.hour = self.time_lst[h_pos - 2]
                self.hour += self.time_lst[h_pos - 1]
            if "m" in self.time_lst:
                m_pos = self.time_lst.index("m")
                if self.time_lst[m_pos - 2] != "h":
                    self.minute = self.time_lst[m_pos - 2]
                self.minute += self.time_lst[m_pos - 1]
            if "s" in self.time_lst:
                s_pos = self.time_lst.index("s")
                if (self.time_lst[s_pos - 2] != "m") and (self.time_lst[s_pos - 2] != "h"):
                    self.second = self.time_lst[s_pos - 2]
                self.second += self.time_lst[s_pos - 1]
        else:
            self.hour = self.time_lst[0]
            self.minute = self.time_lst[1]
            self.second = self.time_lst[2]

        self.total_seconds = (int(self.day) * 24 * 60 * 60) + (int(self.hour) * 60 * 60) + (int(self.minute) * 60) + int(self.second)
        self.hour = str(round((self.total_seconds / 3600) // 1))
        self.minute = str(round(((self.total_seconds - int(self.hour) * 3600) / 60) // 1))
        if self.is_negative:
            self.total_seconds = self.total_seconds * -1

    # add in comparison operators
    def __add__(self, other):
        return self.total_seconds + other.total_seconds

    def __sub__(self, other):
        return self.total_seconds - other.total_seconds

    def __mul__(self, other):
        return self.total_seconds * other.total_seconds

    def __gt__(self, other):
        return True if self.total_seconds > other.total_seconds else False

    def __ge__(self, other):
        return True if self.total_seconds >= other.total_seconds else False

    def __lt__(self, other):
        return True if self.total_seconds < other.total_seconds else False

    def __le__(self, other):
        return True if self.total_seconds <= other.total_seconds else False

    def __eq__(self, other):
        return True if self.total_seconds == other.total_seconds else False

    def __ne__(self, other):
        return True if self.total_seconds != other.total_seconds else False

    def __repr__(self):
        return f"Duration({self.hour}:{self.minute}:{self.second})"

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

# need to be able to:
# add durations
# subtract durations
# multiply durations
# compare durations to each other

# TODO: write function that grabs the amount of time from the input string
# TODO: write function to convert that time to seconds
# TODO: write function to do the math on the times in seconds
# TODO: write repr function that takes the result from the math function and converts to proper format


# times = Duration('0d0h45s')
# print(times)
