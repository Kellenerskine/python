user_input = input()
count = 0

output = ''.join(filter(str.isalnum, user_input))
output_list = list(output)

for i in output_list:
    if i.isalpha():
        continue
    else:
        output_list.remove(i)

for i in output_list:
    print(i, end='')

print()
