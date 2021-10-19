class Duration:
    # """
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
    # """

    def __init__(self, time):
        # time is a string
        # find out what format the time is being passed in as: dhms or hr:min:sec
        extra_index = 0
        if ":" in time:
            if '-' in time:
                extra_index = 1
            self.hours = int(time[0 + extra_index])
            self.minutes = int((time[2 + extra_index]) + (time[3 + extra_index]))
            self.seconds = int((time[5 + extra_index]) + (time[6 + extra_index]))
        # separate out the days, hours, minutes, seconds
        elif ('d' in time) or ('h' in time) or ('s' in time) or ('m' in time):
            self.days = int(time[(time.find('d') - 1)])
            self.hours = int(time[(time.find('h') - 1) + (time.find('h') - 2)])

        # self.days = time[0]
        # self.hours = time[1]
        # self.minutes = time[2]
        # self.seconds = time[3]
        print(str(time))


    # add in comparison operators

    def __repr__(self):
        pass

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def to_seconds(self):
        days_in_sec = self.days * 24 * 60 * 60

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


times = Duration('-1:30:45')
print()
