# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.
#

def high(x):
    values = ["zero", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z"]
    highest = ""
    highest_value = 0
    input_list = x.split()
    word_value = 0

    for word in input_list:
        for letter in str(word):
            word_value += values.index(letter)

        if word_value > highest_value:
            highest_value = word_value
            highest = word
        word_value = 0

    return highest


print(high("man i need a taxi up to ubud"))
