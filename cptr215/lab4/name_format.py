# getting the full name of a person
name = input()
names = name.split()
last_name = names.pop(-1)
first_initial = names[0][0]
if len(names) >= 2:
    middle_initial = names[1][0]
    print(last_name + ", " + first_initial + "." + middle_initial + ".")
else:
    print(last_name + ", " + first_initial + ".")
