def wordsFromNumber(number):
    result = ""
    counter = 0
    num_as_str = str(number)
    num_as_str_len = len(num_as_str)
    while num_as_str_len % 3 != 0:
        num_as_str = '0' + num_as_str

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    tens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    hundreds = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    suffixes = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

    num_strings = [num_as_str[i:i + 3] for i in range(0, len(num_as_str), 3)]
    groups_of_three = len(num_strings)

    counter = groups_of_three - 1

    for string in num_strings:
        for num in string:
            if ((num == string[0]) or (num == string[2])) and num != 0:
                result = (result + " " + ones[int(num)] + " ")
                if groups_of_three != len(num_strings):
                    if num == string[0]:
                        result += suffixes[0]
            else:
                last_two_nums = int(string) % 100
                if last_two_nums < 20:
                    result = result + tens[int(num) - 1]
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
