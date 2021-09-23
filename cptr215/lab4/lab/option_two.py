def wordsFromNumber(number):
    result = ""
    num_as_str = str(number)
    count = 0

    num_names = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                     'twelve', 'thirteen', 'fourteen', 'fifteen',
                     'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
                     'sixty', 'seventy', 'eighty', 'ninety']

    num_strings = [num_as_str[i:i+3] for i in range(0, len(num_as_str), 3)]
    groups_of_three = len(num_strings)

    for i in range(len(num_strings) - 1, -1, -1) :
        print(num_strings[i])




    # print(len(num_strings))




number_input = input("type a num: ")
print(wordsFromNumber(number_input))
