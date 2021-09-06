user_input = int(input())


def dec_to_bin(user_input):
    return int(bin(user_input)[2:]) # returning the decimal to binary reversed


result = str(dec_to_bin(user_input))[::-1]
print(result)