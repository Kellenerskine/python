class Duration:
    """
    # >>> dur_almost_1_day = Duration(23, 59, 59)
    # >>> dur_90_min = Duration("1:30:00")
    # >>> dur_45_sec = Duration("0d0h45s")
    # >>> dur_neg_45_sec = Duration("-45s")
    # >>> dur_1_min = Duration(60) # number of seconds
    # >>> dur_neg_45_sec
    # Duration('-0:00:45')
    # >>> str(dur_45_sec * (2 * 60))
    # '1:30:00'
    # >>> dur_90_min - dur_45_sec # you can represent it however you want, but the repr MUST look like this:
    # Duration('1:29:15')
    # >>> dur_45_sec - dur_90_min
    # Duration('-1:29:15')
    # >>> dur_45_sec - dur_45_sec
    # Duration('0:00:00')
    # >>> dur_45_sec + Duration('1m')
    # Duration('0:01:45')
    # >>> dur_45_sec > Duration('0:1:0') # add the other comparison operators!
    # False
    # >>> print(dur_45_sec + dur_neg_45_sec)
    # 0:00:00
    >>> dur_90_min = Duration("1:30:00")
    >>> dur_45_sec = Duration("0d0h45s")
    >>> dur_90_min - dur_45_sec # you can represent it however you want, but the repr MUST look like this:
    Duration('1:29:15')
    >>> dur_45_sec - dur_90_min
    Duration('-1:29:15')
    """

    # TODO: get rid of all variables and convert to seconds immediately

    @classmethod
    def from_hms(cls, hours=0, minutes=0, seconds=0):
        total = 0
        total += (int(hours) * 3600) if hours is not None and int(hours) > 0 else 0
        total += (int(minutes) * 60) if minutes is not None and int(minutes) > 0 else 0
        total += int(seconds) if seconds is not None and int(seconds) > 0 else 0
        return total

    @classmethod
    def parse_hms(cls, hms_text):
        is_negative = True if hms_text[0] == "-" else False
        days_in_hrs, hours, minutes, seconds = 0, 0, 0, 0
        if ":" in hms_text:
            h, m, s = hms_text.split(':', maxsplit=3)
            return cls.from_hms(h, m, s)
        elif "d" in hms_text or "h" in hms_text or "m" in hms_text or "s" in hms_text:
            if "d" in hms_text:
                days_in_hrs = int(hms_text[hms_text.index("d") - 1]) * 24
            if "h" in hms_text:
                hours = int(hms_text[hms_text.index("h") - 1])
            if "m" in hms_text:
                if "h" in hms_text:
                    minutes = int(hms_text[(hms_text.index("h") + 1):hms_text.index("m")])
                else:
                    minutes = int(hms_text[0:hms_text.index("m")])
            if "s" in hms_text:
                if "h" in hms_text:
                    seconds = int(hms_text[(hms_text.index("h") + 1):hms_text.index("s")])
                elif is_negative:
                    seconds = int(hms_text[1:hms_text.index("s")])
                else:
                    seconds = int(hms_text[0:hms_text.index("s")])
        return cls.from_hms((days_in_hrs + hours), minutes, seconds)

    def __init__(self, a, b=None, c=None):
        self.hour, self.minute, self.second = 0, 0, 0
        if isinstance(a, str):
            self.is_negative = True if a[0] == "-" else False
            self.total_seconds = Duration.parse_hms(a)
            self.hour = self.total_seconds // 3600
            self.minute = (self.total_seconds - (self.hour * 3600)) // 60
            self.second = (self.total_seconds - (self.hour * 3600) - (self.minute * 60))
        else:
            self.is_negative = a < 0
            self.total_seconds = Duration.from_hms(a, b, c)
            self.hour = a
            self.minute = b
            self.second = c

    # comparison operators
    def __add__(self, other):
        secs = self.total_seconds
        other_secs = other.total_seconds
        secs *= -1 if self.is_negative else 1
        other_secs *= -1 if self.is_negative else 1
        total_seconds = secs + other_secs
        hour = total_seconds // 3600
        minute = (total_seconds - (hour * 3600)) // 60
        second = (total_seconds - (hour * 3600) - (minute * 60))
        return Duration(hour, minute, second)

    def __sub__(self, other):
        secs = self.total_seconds
        other_secs = other.total_seconds
        secs *= -1 if self.is_negative else 1
        total_seconds = secs - other_secs
        hour = total_seconds // 3600
        minute = (total_seconds - (hour * 3600)) // 60
        second = (total_seconds - (hour * 3600) - (minute * 60))
        return Duration(hour, minute, second)

    def __mul__(self, other):
        total_seconds = self.total_seconds * other
        hour = total_seconds // 3600
        minute = (total_seconds - (hour * 3600)) // 60
        second = (total_seconds - (hour * 3600) - (minute * 60))
        return Duration(hour, minute, second)

    def __gt__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds > other.total_seconds else False

    def __ge__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds >= other.total_seconds else False

    def __lt__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds < other.total_seconds else False

    def __le__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds <= other.total_seconds else False

    def __eq__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds == other.total_seconds else False

    def __ne__(self, other):
        self.total_seconds *= -1 if self.is_negative else self.total_seconds * 1
        return True if self.total_seconds != other.total_seconds else False

    def __repr__(self):
        if self.total_seconds == 0:
            return '0:00:00'
        else:
            sign = "-" if self.is_negative else ""
            min2 = "0" if self.minute < 10 else ""
            sec2 = "0" if self.second < 10 else ""
            if self.hour < 0:
                sign = ""
            return f"Duration('{sign}{self.hour}:{min2}{self.minute}:{sec2}{self.second}')"

    def __str__(self):
        sign = "-" if self.is_negative else ""
        hour = self.total_seconds // 3600
        minute = (self.total_seconds - (hour * 3600)) // 60
        second = (self.total_seconds - (hour * 3600) - (minute * 60))
        min2 = "0" if self.minute < 10 else ""
        sec2 = "0" if self.second < 10 else ""
        return f"{sign}{hour}:{min2}{minute}:{sec2}{second}"

# TODO: write function to convert that time to seconds
# TODO: write function to do the math on the times in seconds
# TODO: write repr function that takes the result from the math function and converts to proper format
