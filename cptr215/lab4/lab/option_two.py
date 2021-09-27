def wordsFromNumber(number):
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

    for string in num_strings:
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
            if pos == 3 and num != 0 and is_a_teen != 1:
                result = (result + ones[int(num)])
                if ((counter != len(num_strings)) or len(num_strings) == 1) and (pos == 1):
                    result += " hundred "
            result += " "
        result += " " + suffixes[counter] + " "
        counter -= 1

    result_strings = result.split()
    result = ""
    for i in range(len(result_strings)):
        result += result_strings[i]
        if i != (len(result_strings)-1):
            result += " "

    return result


number_input = input("type a num: ")
print(wordsFromNumber(number_input))
