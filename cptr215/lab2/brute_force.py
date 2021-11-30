# first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

# second equation, dx + ey = f
d = int(input())
e = int(input())
f = int(input())

no_sol = True

for x in range(-10, 10):
    for y in range(-10, 10):
        g = a * x + b * y
        h = d * x + e * y
        if c == g and f == h:
            print(f"x = {x} , y = {y}")
            no_sol = False

if no_sol:
    print("There is no solution")

