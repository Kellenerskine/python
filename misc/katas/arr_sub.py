# the array dif function takes two lists, a and b, and subtracts b from a. returning the new a list

def array_diff(a, b):
    # your code here
    index = 0
    while index <= len(b):
        for i in b:
            while i in a:
                a.remove(i)
        index += 1

    return a


print(array_diff([1, 2, 5, 3, 10, 55], [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0, -1, -3000]))
