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
#
#
#


def integer_to_english(number):
    if number>=1 and number<=1000:
        a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
             'sixteen','seventeen','eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' and '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' and '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1

number=789
print(integer_to_english(number))







































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
