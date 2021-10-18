def num_nums(number):
    """should take in a number and convert to string then count characters
    >>> num_nums(989)
    3
    >>> num_nums(345689)
    6
    >>> num_nums(2)
    1
    >>> num_nums(1234987912038740198274)
    22
    """
    user_input = str(number)
    count = 0
    for i in user_input:
        count += 1

    return count
