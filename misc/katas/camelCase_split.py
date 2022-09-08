# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    # I know this is inefficient af, but I can't think of a better way
    caps_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z", ]
    input_list = list(s)
    result = ""

    for letter in input_list:
        if letter in caps_list:
            position_of_caps = input_list.index(letter)
            result += " "
            result += letter
        else:
            result += letter

    return result


print(solution("breakCamelCase"))
