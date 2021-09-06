hw_num = int(input())

if hw_num == 0:
    print("0 is not a valid interstate highway number.")
elif hw_num == 200:
    print("200 is not a valid interstate highway number.")
elif hw_num >= 1000:
    print("1000 is not a valid interstate highway number.")
else:
    if 0 < hw_num < 100:
        hw_num_const = hw_num
        hw_num %= 2
        if hw_num == 0:
            print("I-{} is primary, going east/west.".format(hw_num_const))
        else:
            print("I-{} is primary, going north/south.".format(hw_num_const))
    elif 99 < hw_num < 1000:
        hw_num_const = hw_num
        hw_num_right = hw_num % 100  # getting the rightmost 2 numbers
        if (hw_num_right % 2) == 0:
            print(f"I-{hw_num_const} is auxiliary, serving I-{hw_num_right}, going east/west.")
        else:
            print(f"I-{hw_num_const} is auxiliary, serving I-{hw_num_right}, going north/south.")