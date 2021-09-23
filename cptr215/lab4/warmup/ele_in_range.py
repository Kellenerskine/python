list_of_int = input()
nums = list_of_int.split()
range1 = input().split()
lower = range1[0]
upper = int(range1[1]) +1

for i in nums:
    if int(i) in range(int(lower), upper):
        print(i, end="")
        print(" ", end='')
