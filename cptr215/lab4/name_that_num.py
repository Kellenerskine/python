# Design, implement, and fully test a Python3 function that converts a number to words (wordsFromNumber).
# It should expect to be passed a whole number (such as 12345) and return the corresponding words (i.e., "twelve thousand three hundred forty-five").
# Since Python integers can grow arbitrarily large, your code should be flexible, handling at least 20 digits (realistically, it's just as easy up to 30 digits). '
# Spell everything correctly, and use correct punctuation (hyphens for forty-five and thirty-seven, no commas or plurals).
# You may only use built-in Python functions, not any modules or third-party libraries!'

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def number_to_words(number):
    if number - 11 >= 0:
        pass
    else:
        for i in str(number):
            return "".join(words[int(i)])


print(number_to_words(10))













































# def words_from_number(number):  # converts a number to words
#     num_name_dict = {
#         1: "one",
#         2: "two",
#         3: "three",
#         4: "four",
#         5: "five",
#         6: "six",
#         7: "seven",
#         8: "eight",
#         9: "nine"
#     }
#     num_as_str = str(number)
#     for num in num_as_str:
#         for key in num_name_dict:
#             if num == key:
#                 print(num_name_dict[key])
#     # take the right-most numbers
#
#     return num_as_str
#
#
# user_number = int(input())
# word_output = words_from_number(user_number)
# # print(word_output)
