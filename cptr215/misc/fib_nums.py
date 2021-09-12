# figured i would grab this snippet of code as it seems like something ordonez could assign for
# homework someday and this way i wont need to think about it, just copy paste lol.

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


top_num = int(input("How far in the fibonacci sequence would you like to go? "))
fib(top_num)
