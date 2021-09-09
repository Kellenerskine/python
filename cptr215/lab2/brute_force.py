# Read in first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

# Read in second equation, dx + ey = f
d = int(input())
e = int(input())
f = int(input())

# Type your code here.
for x in range(-10, 11):
    for y in range(-10, 11):

        g = a * x + b * y
        h = d * x + e * y
        if c == g and f == h:
            print("x = {} , y = {}".format(g, h))
        else:
            print("There is no solution.")
