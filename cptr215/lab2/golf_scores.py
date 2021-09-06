par = int(input())
num_shots_taken = int(input())

if par < 3:
    print("Error")
elif par > 5:
    print("Error")
else:
    if par == num_shots_taken:
        print("Par")
    elif (par - 1) == num_shots_taken:
        print("Birdie")
    elif (par - 2) == num_shots_taken:
        print("Eagle")
    elif (par + 1) == num_shots_taken:
        print("Bogey")
