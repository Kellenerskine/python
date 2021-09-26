def wordsFromNumber(number):
    result = ""
    counter = 0
    num_as_str = str(number)
    num_as_str_len = len(num_as_str)
    while num_as_str_len % 3 != 0:
        num_as_str = '0' + num_as_str

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
    hundreds = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    suffixes = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']
    num_strings = [num_as_str[i:i + 3] for i in range(0, len(num_as_str), 3)]
    groups_of_three = len(num_strings)

    counter = groups_of_three - 1

    for string in num_strings:
        for num in string:
            last_two_nums = int(string) % 100
            if num == string[0] and num != 0:
                result = (result + " " + ones[int(num)] + " ")
                if ((counter != len(num_strings)) or len(num_strings) == 1) and (num == string[0]):
                    result += "hundred "
            elif num == string[2]:
                result = (result + " " + ones[int(num)] + " ")
                if ((counter != len(num_strings)) or len(num_strings) == 1) and (num == string[0]):
                    result += "hundred "

            else:
                # last_two_nums = int(string) % 100
                if 20 > last_two_nums > 9:
                    result = result + tens[int(num)]
                elif last_two_nums < 10:
                    result = result + ones[int(num)]
                else:
                    result = result + hundreds[int(num) - 1]
        result += suffixes[counter]
        counter -= 1
        # for every number in every string
        # change number to word value
        # as well as add the proper suffixes
        # add suffix

    return result


number_input = input("type a num: ")
print(wordsFromNumber(number_input))
