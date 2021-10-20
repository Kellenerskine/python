user_input = input("Write a whole number")
contains_all = True

all_digits = [str(num) for num in range(0, 10)]
user_input = list(user_input)

for digit in all_digits:
    if digit not in user_input:
        contains_all = False
        break

if contains_all:
    print("Is pangram")
else:
    print("Is not pangram")
