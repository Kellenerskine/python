class Thing:
    def __init__(self, x):
        self.x = x

    def nice(self):
        print('nice')
        return self.x + 1

    @classmethod
    def one(cls):
        print(cls)
        return cls(1)


thing0 = Thing(0)
thing1 = Thing.one()

print(thing0.x, thing1.x)
