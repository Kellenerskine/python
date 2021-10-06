class BoundedCounter:
    def __init__(self, lower_bound, upper_bound, neighbor):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound

    def increment(self):
        if self.current_value > self.upper_bound:
            self.current_value = self.lower_bound
            if self.neighbor:
                self.neighbor.increment
        else:
            self.current_value += 1
    def get_value(self):
        return self.current_value
    def __str__(self):
        return (str(self.neighbor) if self.neighbor else "") + str(self.current_value)


# digit = BoundedCounter(0, 9)
bit = BoundedCounter(0, 1)
for _ in range(3):
    bit = BoundedCounter(0, 1, bit)

for _ in range(10):
    print(f"Before: {bit}", end='')
    bit.increment()
    print(f" and after: {bit}")

hour24 = BoundedCounter(0, 23)
minute60 = BoundedCounter(0, 59)

hour12 = BoundedCounter(1, 12)
minute01 = BoundedCounter(0, 9)
minute10 = BoundedCounter(0, 5)
