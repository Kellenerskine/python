def move_zeros(lst):
    listy = list(lst)
    counter = 0
    for i in listy:
        if i == 0:
            listy.remove(i)
            counter += 1

    for k in range(0, counter):
        listy.append(int("0"))

    return listy


free = move_zeros([1, 0, 1, 2, 0, 1, 3])
print(free)
