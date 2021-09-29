def wordsFromNumber(number):
    """Function should take a number and return that number in words
    >>> wordsFromNumber(278644094904718128) #big numbers
    'two hundred seventy-eight quadrillion six hundred forty-four trillion ninety-four billion nine hundred four million seven hundred eighteen thousand one hundred twenty-eight'
    >>> wordsFromNumber(400)
    'four hundred'
    >>> wordsFromNumber(420)
    'four hundred twenty'
    >>> wordsFromNumber(418)
    'four hundred eighteen'
    >>> wordsFromNumber(428)
    'four hundred twenty-eight'
    >>> wordsFromNumber(408)
    'four hundred eight'
    >>> wordsFromNumber(888568485034000808)
    'eight hundred eighty-eight quadrillion five hundred sixty-eight trillion four hundred eighty-five billion thirty-four million eight hundred eight'
    """
    if int(number) == 0:
        return "zero"
    result = ""
    counter = 0
    num_as_str = str(number)
    num_as_str_len = len(num_as_str)
    while num_as_str_len % 3 != 0:
        num_as_str = '0' + num_as_str
        num_as_str_len += 1

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
    hundreds = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    suffixes = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']
    num_strings = [num_as_str[i:i + 3] for i in range(0, len(num_as_str), 3)]
    groups_of_three = len(num_strings)

    counter = groups_of_three - 1
    pos = 0
    is_a_teen = 0
    hiphen = 0  # means the words have no hiphens

    for string in num_strings:
        is_a_teen = 0
        for num in string:
            pos += 1
            if pos > 3:
                pos = 1
            last_two_nums = int(string) % 100  # string concat required?
            if pos == 1 and int(num) != 0:  # num == string[0]
                result = (result + ones[int(num)])
                if ((counter != len(num_strings)) or len(num_strings) == 1) and (num == string[0]):
                    result += " hundred "
            if pos == 2 and num != 0:
                # the if statement below checks each and every teen, open at your own risk
                if 20 > last_two_nums > 9:
                    if last_two_nums == 10:
                        result += tens[0]
                    elif last_two_nums == 11:
                        result += tens[1]
                    elif last_two_nums == 12:
                        result += tens[2]
                    elif last_two_nums == 13:
                        result += tens[3]
                    elif last_two_nums == 14:
                        result += tens[4]
                    elif last_two_nums == 15:
                        result += tens[5]
                    elif last_two_nums == 16:
                        result += tens[6]
                    elif last_two_nums == 17:
                        result += tens[7]
                    elif last_two_nums == 18:
                        result += tens[8]
                    elif last_two_nums == 19:
                        result += tens[9]

                    is_a_teen += 1  #
                elif last_two_nums < 10:
                    result = result + ones[int(num)]
                else:
                    result = result + hundreds[int(num) - 1]
                    if (last_two_nums % 10) != 0:  # determines if a hyphen is needed
                        result += "-"
                        hiphen += 1  # means the word has a hyphen
            if pos == 3 and num != 0 and is_a_teen != 1:
                result = (result + ones[int(num)])
                if ((counter != len(num_strings)) or len(num_strings) == 1) and (pos == 1):
                    result += " hundred "
        sum_of_string = int(string[0]) + int(string[1]) + int(string[2])
        if sum_of_string != 0:
            result += " " + suffixes[counter] + " "
        counter -= 1

    result_strings = result.split()
    result = ""
    for i in range(len(result_strings)):
        result += result_strings[i]
        if i != (len(result_strings) - 1):  # and (hiphen == 0)
            result += " "

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    number_input = input("type a num: ")
    print(wordsFromNumber(number_input))




# still having some issues with big numbers, is_a_teen = 1 and so the program skips over the last number
# need some way to reset


