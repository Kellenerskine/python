def fibonacci(n):
    """Function should take a number as an index location and tell what number in the fib sequence
    is in that position
    >>> fibonacci(7)
    '13'
    >>> fibonacci(12)
    '144'
    """
    num1 = 0
    num2 = 1
    new_num = 0
    fib_string = []

    if n < 0:
        return -1
    else:
        fib_string.append(str(num1))
        fib_string.append(str(num2))
        for i in range(-1, n):
            new_num = num1 + num2
            num1 = num2
            num2 = new_num
            fib_string.append(str(new_num))

        result = fib_string[n]

    return int(result)



if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
