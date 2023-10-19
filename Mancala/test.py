holes1 = [4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0]




for i in range(7, 13):  # checks if top row is empty
    if holes1[i] == 0:
        print("game is over")
    else:
        print("game is ongoing: ", holes1[i])

