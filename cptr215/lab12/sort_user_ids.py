# Global variable
num_calls = 0


def sort(user_ids):
    less = []
    equal = []
    greater = []
    global num_calls
    num_calls += 1

    if len(user_ids) > 1:
        pivot = user_ids[0]
        for x in user_ids:
            if x > pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x < pivot:
                greater.append(x)
        result = sort(greater) + equal + sort(less)
        return result
    else:
        return user_ids


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to sort
    user_ids = sort(user_ids)

    # Print number of calls to sort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
