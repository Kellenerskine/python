def integer_to_reverse_binary(integer_value):
    """this function should take a number and convert it to binary, but in reverse
    >>> integer_to_reverse_binary(6)
    '011'
    >>> integer_to_reverse_binary(19)
    '11001'
    """
    bin_revers = ""

    x = integer_value

    while x > 0:
        bin_revers = bin_revers + str((x % 2))
        x = x // 2

    return bin_revers


def reverse_string(input_string):
    """this function should reverse the string from the previous function
    >>> reverse_string('011')
    '110'
    >>> reverse_string('11001')
    '10011'
    """
    result = ""
    for i in input_string:
        result = i + result

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    integer_value = int(input())
    reversed_binary = integer_to_reverse_binary(integer_value)
    binary = reverse_string(reversed_binary)
    print(binary)
