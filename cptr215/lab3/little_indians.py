n = input()
if n == '':
    n = 10
else:
    n = int(n)

for i in range(1, n):
    print(i, "little", end="")
    if (i % 3) == 0:
        print(" Indians;")
    else:
        print(",", end="")

print("{} little Indian boys.".format(n))
