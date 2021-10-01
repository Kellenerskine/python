class BoundedCounter:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound

    def increment(self):
        if self.current_value > self.upper_bound:
            self.current_value = self.lower_bound
        else:
            self.current_value += 1


digit = BoundedCounter(0, 9)
bit = BoundedCounter(0, 1)

bit.increment()

hour24 = BoundedCounter(0, 23)
minute60 = BoundedCounter(0, 59)

hour12 = BoundedCounter(1, 12)
minute01 = BoundedCounter(0, 9)
minute10 = BoundedCounter(0, 5)
