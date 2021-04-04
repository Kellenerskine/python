number = "something"
numbers = []
while number != "#":
    number = input("Type in a number, hit enter to submit. (Type '#' to stop entering numbers): ")
    if number == "#":
        break
    numbers.append(float(number))

print("User entered: ", numbers)
print("The min is: ", min(numbers))
print("The max is: ", max(numbers))
print("The average is: ", sum(numbers)/len(numbers))