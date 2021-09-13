"""3a_duplicates.py
Check for duplicates
Prof O and CPTR-215
2021-09-13 first draft"""


def get_numbers():
    return [2, 4, 6, 8, 7, 5, 9]


def has_duplicates(items):
    """Determines whether numbers contains any duplicates.
    >>> has_duplicates([1, 3, 5, 7, 1])
    True
    >>> has_duplicates([1])
    False
    """
    for i in range(len(numbers)):
        if numbers[i] in numbers[i:]:
            return


#  get list of nums from user until 'STOP'
numbers = get_numbers()
#  check for duplicates
if has_duplicates(numbers):
    print("There's at least on duplicate number!")
else:
    print("There are no duplicates!")
#  show results
