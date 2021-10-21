from enum import Enum


class HalfInning(Enum):
    TOP = 0
    BOTTOM = 1

class BaseballCounter:
    def __init__(self, balls=0, strikes=0, outs=0, half=0, inning=0):
        self.balls = balls
        self.strikes = strikes
        self.outs = outs
        self.half = half
        self.inning = inning

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def ball(self):
        if self.balls >= 4:
            self.new_batter()



    def strike(self):
        self.balls += 1
        if self.strikes == 3:
            self.out()


    def new_batter(self):
        self.balls = 0
        self.strikes = 0

    def out(self):
        self.outs += 1
        if self.outs == 3:


    def new_game(self):
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        self.half = ""
        self.inning = 0


# class BoundedCounter:
#     def __init__(self, lower_bound, upper_bound, neighbor=None):
#         self.lower_bound = lower_bound
#         self.upper_bound = upper_bound
#         self.current_value = self.lower_bound
#         self.neighbor = neighbor
#
#     def increment(self):
#         if self.current_value == self.upper_bound:
#             self.current_value = self.lower_bound
#             if self.neighbor:
#                 self.neighbor.increment()
#         else:
#             self.current_value += 1
#
#     def get_value(self):
#         return self.current_value
#
#     def __str__(self):
#         return (str(self.neighbor) if self.neighbor else "") + str(self.current_value)
#
#
# class ListCounter:
#     def __init__(self, items, neighbor=None):
#         self.items = tuple(items)
#         self.index = BoundedCounter(0, len(self.items) - 1, neighbor)
#
#     def increment(self):
#         self.index.increment()
#
#     def get_value(self):
#         return self.items[self.index.get_value()]

counter = BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)
