good_worth_dict = {
    "Hobbits": 1,
    "Men": 2,
    "Elves": 3,
    "Dwarves": 3,
    "Eagles": 4,
    "Wizards": 10,
}
evil_worth_dict = {
    "Orcs": 1,
    "Men": 2,
    "Wargs": 2,
    "Goblins": 2,
    "Uruk_hai": 3,
    "Trolls": 5,
    "Wizards": 10
}

def good_vs_evil(good, evil):
    good_list = []
    good_total = 0
    evil_list = []
    evil_total = 0


    for i in good:
        if i.isnumeric():
            good_list += i
    for j in evil:
        if j.isnumeric():
            evil_list += j

    for i in good_list:
        good_total += (int(i) * list(good_worth_dict.values())[good_list.index(i)])
        #need to multiply the number by it's dict(position(number))

    for i in evil_list:
        evil_total += (int(i) * list(evil_worth_dict.values())[evil_list.index(i)])

    print(good_total)
    print(evil_total)

    return

input_values = good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
#result should be evil winning
