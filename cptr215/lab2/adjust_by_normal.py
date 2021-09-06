lst = []
count = 0
# number of elements as input
n = int(input())

# inputting into a list
for i in range(0, n):
    ele = float(input())
    lst.append(ele)

biggest_num = max(lst)

result = []

for i in lst:
    new_list_num = i / biggest_num
    result.append(new_list_num)

for i in range(len(result)):
    print('{:.2f}'.format(result[i]))