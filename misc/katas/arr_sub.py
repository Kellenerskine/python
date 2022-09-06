

def array_diff(a, b):
    # your code here
    for i in b:
        for j in a:
            if i == j:
                a.remove(j)
    return a


print(array_diff([1, 2, 2], [2]))
# should produce: [1]
