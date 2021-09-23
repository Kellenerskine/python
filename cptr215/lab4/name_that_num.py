# Design, implement, and fully test a Python3 function that converts a number to words (wordsFromNumber).
# It should expect to be passed a whole number (such as 12345) and return the corresponding words (i.e., "twelve thousand three hundred forty-five").
# Since Python integers can grow arbitrarily large, your code should be flexible, handling at least 20 digits (realistically, it's just as easy up to 30 digits). '
# Spell everything correctly, and use correct punctuation (hyphens for forty-five and thirty-seven, no commas or plurals).
# You may only use built-in Python functions, not any modules or third-party libraries!'

# words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
#
# def number_to_words(number):
#     if number - 11 >= 0:
#         pass
#     else:
#         for i in str(number):
#             return "".join(words[int(i)])
#
#
# print(number_to_words(10))


def words_from_number(number):
    # """This function should take a number and return the number in english.
    # >>> words_from_number(500)
    # 'five hundred'
    # >>> words_from_number(657)
    # 'six hundred and fifty seven'
    # """
    if 1 <= number <= 1000:  # TODO expand this to proper scope, as well as expand the num_names list
        num_names = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                     'twelve', 'thirteen', 'fourteen', 'fifteen',
                     'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty ', 'thirty ', 'forty ', 'fifty ',
                     'sixty ', 'seventy ', 'eighty ', 'ninety ']
        if number <= 20:
            return num_names[number]
        elif number < 100:  # TODO fix logic here
            b = number - 20
            r = b % 10
            b //= 10
            return num_names[20 + b + num_names[r]]
        elif number < 1000:
            if number % 100 == 0:  # if the num is an even hundred ie. 900
                b = number // 100
                return num_names[b] + ' hundred'
            else:  # if the number is not an even hundred ie. 980
                r = number % 100  # get back two nums
                b = number // 100  # get front num ie 980 % 100 = 9
                if r <= 20:
                    return num_names[b] + ' hundred' + ' and ' + num_names[r]
                else:
                    r = r - 20
                    d = r // 10
                    r %= 10
                    return num_names[b] + ' hundred' + ' and ' + num_names[20 + d] + num_names[r]
        elif number == 1000:
            return 'one thousand'
        # elif: #TODO implement logic for numbers over 1000
        #     pass
        #     return 89
        else:
            return -1
    else:
        return 'zero'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    number_input = input("enter a num: ")

    print(words_from_number(int(number_input)))
