from enum import Enum


class HalfInning(Enum):
    TOP = 0
    BOTTOM = 1


class BaseballCounter:
    def __init__(self, balls=0, strikes=0, outs=0, half=HalfInning.TOP, inning=1):
        self.balls = balls
        self.strikes = strikes
        self.outs = outs
        self.half = half
        self.inning = inning

    def __str__(self):
        # 3 balls, 2 strikes, 2 outs, bottom of the 9th inning
        """should return a human readable version of object
        >>> str(BaseballCounter(3, 2, 1, HalfInning.TOP, 8))
        '3 balls, 2 strikes, 1 out, top of the 8th inning'
        >>> str(BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 1))
        '1 ball, 1 strike, 1 out, bottom of the 1st inning'
        >>> str(BaseballCounter(2, 1, 2, HalfInning.TOP, 8))
        '2 balls, 1 strike, 2 outs, top of the 8th inning'
        >>> str(BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 1))
        '1 ball, 1 strike, 1 out, bottom of the 1st inning'
        """
        if self.inning == 1:
            suffix = "st"
        elif self.inning == 2:
            suffix = "nd"
        elif self.inning == 3:
            suffix = "rd"
        else:
            suffix = "th"

        if self.half == HalfInning.BOTTOM:
            half_name = "bottom"
        else:
            half_name = "top"

        if self.balls == 1:
            balls_suffix = ""
        else:
            balls_suffix = "s"

        if self.strikes == 1:
            strikes_suffix = ""
        else:
            strikes_suffix = "s"

        if self.outs == 1:
            outs_suffix = ""
        else:
            outs_suffix = "s"

        return f"{self.balls} ball{balls_suffix}, {self.strikes} strike{strikes_suffix}, {self.outs} out{outs_suffix}, {half_name} of the {self.inning}{suffix} inning"

    def __repr__(self):
        # BaseballCounter(3, 2, 2, HalfInning.BOTTOM, 9)
        """should return a machine readable string
        >>> repr(BaseballCounter(3, 2, 1, HalfInning.TOP, 8))
        'BaseballCounter(3, 2, 1, HalfInning.TOP, 8)'
        >>> repr(BaseballCounter(2, 3, 1, HalfInning.BOTTOM, 3))
        'BaseballCounter(2, 3, 1, HalfInning.BOTTOM, 3)'
        >>> repr(BaseballCounter(1, 2, 3, HalfInning.TOP, 8))
        'BaseballCounter(1, 2, 3, HalfInning.TOP, 8)'
        >>> repr(BaseballCounter(2, 2, 2, HalfInning.BOTTOM, 3))
        'BaseballCounter(2, 2, 2, HalfInning.BOTTOM, 3)'
        >>> repr(BaseballCounter(3, 3, 3, HalfInning.TOP, 8))
        'BaseballCounter(3, 3, 3, HalfInning.TOP, 8)'
        >>> repr(BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 3))
        'BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 3)'
        >>> repr(BaseballCounter(3, 2, 1, HalfInning.TOP, 8))
        'BaseballCounter(3, 2, 1, HalfInning.TOP, 8)'
        >>> repr(BaseballCounter(2, 3, 1, HalfInning.BOTTOM, 3))
        'BaseballCounter(2, 3, 1, HalfInning.BOTTOM, 3)'
        """
        return f"BaseballCounter({self.balls}, {self.strikes}, {self.outs}, {self.half}, {self.inning})"

    def ball(self):
        """
        >>> game = BaseballCounter(1, 3, 2)
        >>> game.strikes
        3
        >>> game = BaseballCounter()
        >>> game.strikes = 3
        >>> game.balls = 1
        >>> game.outs = 2
        >>> str(game)
        '1 ball, 3 strikes, 2 outs, top of the 1st inning'
        """
        self.balls += 1
        if self.balls >= 4:
            self.balls = 0
            self.new_batter()

    def strike(self):
        """
        >>> game = BaseballCounter(1, 3, 2)
        >>> game.strikes
        3
        >>> game = BaseballCounter()
        >>> game.strikes = 3
        >>> game.balls = 1
        >>> game.outs = 2
        >>> str(game)
        '1 ball, 3 strikes, 2 outs, top of the 1st inning'
        """
        self.strikes += 1
        if self.strikes > 2:
            self.out()
            self.new_batter()

    def out(self):
        """
        >>> game = BaseballCounter(1, 3, 2)
        >>> game.strikes
        3
        >>> game = BaseballCounter()
        >>> game.strikes = 3
        >>> game.balls = 1
        >>> game.outs = 2
        >>> str(game)
        '1 ball, 3 strikes, 2 outs, top of the 1st inning'
        """
        self.outs += 1
        if self.outs > 2 and self.half == HalfInning.TOP:
            self.half = HalfInning.BOTTOM
            self.new_batter()
            self.outs = 0
        elif self.outs > 2 and HalfInning.BOTTOM:
            self.inning += 1
            self.half = HalfInning.TOP
            self.outs = 0
            self.new_batter()



    def new_batter(self):
        self.balls = 0
        self.strikes = 0

    def new_game(self):
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        self.half = HalfInning.TOP
        self.inning = 1
