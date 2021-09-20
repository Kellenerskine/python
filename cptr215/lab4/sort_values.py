def isStrictlyIncreasing(input_list):
    # """should take in any input and return whether it is incresaing or not
    # >>> isStrictlyIncreasing([1, 3, 5, 7, 9])
    # True
    # >>> isStrictlyIncreasing("almost")
    # True
    # >>> isStrictlyIncreasing([4, 3, 8, 1, 0])
    # False
    # """
    # values = []
    # for i in input_list:
    #     values.append(ord(str(i)))

    for i in input_list:
        if i > i + 1:
            pass
        else:
            return False
    return True


input_list = [45, 45, 90]
if isStrictlyIncreasing(input_list):
    print("true")
else:
    print("false")
