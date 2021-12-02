# Global variable
num_calls = 0

# # TODO: Write the partitioning algorithm - pick the middle element as the
# #       pivot, compare the values using two index variables l and h (low and high),
# #       initialized to the left and right sides of the current elements being sorted,
# #       and determine if a swap is necessary
# def partition(user_ids, low, high):
#     global num_calls
#     i_index = (low-1)
#     pivot = user_ids[high]
#     for j_index in range(low , high):
#         if user_ids[j_index] <= pivot:
#             i_index = i_index+1
#         user_ids[i_index],user_ids[j_index] = user_ids[j_index],user_ids[i_index]
#     user_ids[i_index+1],user_ids[high] = user_ids[high], user_ids[i_index+1]
#     return (i_index+1)
#
# # TODO: Write the quicksort algorithm that recursively sorts the low and
# #       high partitions. Add 1 to num_calls each time quisksort() is called
# def quicksort(user_ids, i, k):
#     global num_calls
#     num_calls = num_calls + 1
#     if i < k:
#         pi = partition(user_ids,i,k)
#         quicksort(user_ids, i , pi-1)
#         quicksort(user_ids, pi+1, k)





def sort(user_ids):
    less = []
    equal = []
    greater = []
    global num_calls

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
        num_calls += 1
        return result
    else:
        num_calls += 1
        return user_ids




if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to sort
    user_ids = sort(user_ids)
    num_calls += 1


    # Print number of calls to sort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
