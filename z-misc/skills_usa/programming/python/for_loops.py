how_far = int(input("how far do you want me to count?"))
for number in range(1, how_far +1):
    print(number)

name = "something"
names = []
while name != "":
    name = input("type a name and hit enter (just hit Enter when done):")
    names.append(name)
print("Thanks for entering", len(names), "names!")
