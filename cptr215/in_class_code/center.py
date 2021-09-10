import math


def center(message, width, fill=' '):
    """Pad messgae so its centered in a field of size width (leaning left if an odd number of spaces are left)
    Padding uses fill character (space by defaults)
    >>> center("May 2021", 20)
    '      May 2021      '
    >>> center("hello", 12, fill = '-')
    '---hello----'
    >>> len(center("hello", 12, fill = '-'))
    12
    """

    padding = (width - len(message)) /2
    return (fill[0] * math.floor(padding)) + message + (fill[0] * (math.ceil(padding)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
