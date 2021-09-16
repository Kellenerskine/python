def isStrictlyIncreasing(liste):
    listee = list(liste)
    print(listee)
    maxi = -200000
    for i in listee:
        if i > maxi:
            maxi = i
        else:
            return False
    return True


liste = "almost"
if isStrictlyIncreasing(liste):
    print("true")
else:
    print("false")