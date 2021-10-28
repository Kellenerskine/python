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

    # TODO: get rid of all variables and convert to seconds immediately

    def __init__(self, total_seconds):
        self.total_seconds = total_seconds

        @classmethod
        def from_hms(cls, hours=0, minutes=0, seconds=0):
            return cls(hours * 3600 + minutes * 60 + seconds)

        @classmethod
        def parse_hms(cls, hms_text):
            if ":" in hms_text:
                h, m, s = hms_text.split(':', maxsplit=3)
                return cls.from_hms(h, m, s)
            elif "d" in hms_text or "h" in hms_text or "m" in hms_text or "s" in hms_text:
                if "d" in hms_text:
                    days = hms_text[hms_text.index("d") - 1]
                if "h" in hms_text:  # TODO: edit to handle 2 digit nums
                    hours = hms_text[hms_text.index("h") - 1]
                if "m" in hms_text:
                    minutes = hms_text[0:hms_text.index("m")]
                if "s" in hms_text:
                    seconds = hms_text[0:hms_text.index("s")]

    # comparison operators
    def __add__(self, other):
        return self.total_seconds + other.total_seconds

    def __sub__(self, other):
        return self.total_seconds - other.total_seconds

    def __mul__(self, other):
        return self.total_seconds * other

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
        if ":" in self.time_lst:
            self.hour = self.time_lst[len(self.time_lst) - 7]
            self.minute = self.time_lst[len(self.time_lst) - 5] + self.time_lst[len(self.time_lst) - 4]
            self.second = self.time_lst[len(self.time_lst) - 2] + self.time_lst[len(self.time_lst) - 1]
        elif "d" in self.time_lst or "h" in self.time_lst or "m" in self.time_lst or "s" in self.time_lst:
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

        self.total_seconds = (int(self.day) * 24 * 60 * 60) + (int(self.hour) * 60 * 60) + (
                int(self.minute) * 60) + int(self.second)
        self.hour = str(round((self.total_seconds / 3600) // 1))
        self.minute = str(round(((self.total_seconds - int(self.hour) * 3600) / 60) // 1))
        if self.is_negative:
            self.total_seconds = self.total_seconds * -1

        if self.is_negative:
            sign = "-"
        else:
            sign = ""

        if self.minute < 10:
            self.minute = "0" + str(self.minute)
        if self.second < 10:
            self.second = "0" + str(self.second)

        return f"Duration('{sign}{self.hour}:{self.minute}:{self.second}')"

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

# TODO: write function that grabs the amount of time from the input string
# TODO: write function to convert that time to seconds
# TODO: write function to do the math on the times in seconds
# TODO: write repr function that takes the result from the math function and converts to proper format

#
# times = Duration('-0:00:45')
# print(times)
