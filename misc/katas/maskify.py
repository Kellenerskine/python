# return masked string
def maskify(cc):
    masked = ""
    counter = 0
    for i in cc:
        if counter <= len(cc) - 5:
            masked += "#"
        else:
            masked += i
        counter += 1

    return masked


print(maskify("Nananananananananananananananana Batman!"))



# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""
#
# // "What was the name of your first pet?"
#
# "Skippy" --> "##ippy"
#
# "Nananananananananananananananana Batman!"
# -->
# "####################################man!"
