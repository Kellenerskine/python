"""3a_duplicates.py
Check for duplicates
Prof O and CPTR-215
2021-09-13 first draft"""


def get_numbers():
    """Asks user to enter numbers until they enter STOP.
    Returns a list that contains all the numbers.
    >>>
    """
    while True:
        user_input = input("Enter a number (STOP when done): ")
        if user_input == "STOP":
            return numbers
        else:
            numbers.append(float(user_input))

def has_duplicates(items):
    """Determines whether numbers contains any duplicates.
    >>> has_duplicates([1, 3, 5, 7, 1])
    True
    >>> has_duplicates([1])
    False
    >>> has_duplicates([])
    False
    >>> has_duplicates([6, 6, 6, 6, 6, 6])
    True
    """
    for i in range(len(numbers)):
        if numbers[i] in numbers[i+1:]:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

#  get list of nums from user until 'STOP'
numbers = get_numbers()
#  check for duplicates
if has_duplicates(numbers):
    print("There's at least on duplicate number!")
else:
    print("There are no duplicates!")
#  show results
