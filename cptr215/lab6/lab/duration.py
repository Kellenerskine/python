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

    def __init__(self, time):
        # time is a string
        # separate out the days, hours, minutes, seconds
        self.days = time[0]
        self.hours = time[1]
        self.minutes = time[2]
        self.seconds = time[3]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def to_seconds(self, days, hours, minutes, seconds):
        pass

# need to be able to:
# add durations
# subtract durations
# multiply durations
# compare durations to each other

# TODO: write function that grabs the amount of time from the input string
# TODO: write function to convert that time to seconds
# ie. to_seconds(self.days, self.hours, self.minutes, self.seconds)
# TODO: write function to do the math on the times in seconds
# TODO: write repr function that takes the result from the math function and converts to proper format
