# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    """sorts list in descending order
    >>> selection_sort_descend_trace([20, 10, 30, 40])
    40 10 30 20
    40 30 10 20
    40 30 20 10
    """

    for i in range(len(numbers)):
        min_idx = i

        for j in range(i+1, len(numbers)):
            if int(numbers[min_idx]) < int(numbers[j]):
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

        if numbers[i] != numbers[len(numbers)-1]:
            for k in numbers:
                print(k, end=' ')
            print()


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    inputs = input()
    numbers = []
    stuff = inputs.split(" ")
    for i in stuff:
        numbers.append(i)

    selection_sort_descend_trace(numbers)

