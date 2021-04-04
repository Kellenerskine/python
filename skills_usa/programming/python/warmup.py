print("enter a num between 1 and 10: ")
input1 = int(input())
if(1 < input1 < 10):
    for i in range(input1, 100):
        if(i != 56):
            print(i, end="  ")
        else:
             print("")