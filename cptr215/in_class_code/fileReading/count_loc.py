file_name = input("What file do you want to read? ")
file = open(file_name)
total_lines, loc, other = 0, 0, 0
for line in file:
    total_lines += 1
    if line.strip()[0] == '#':
        other += 1
    else:
        loc += 1

print(f"File: {file_name} \n Code: {loc} \n Other: + {other} \n ---------- \n Total Lines: {loc + other}")
