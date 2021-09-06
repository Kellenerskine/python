user_text = input()

num_chars = 0

for i in user_text:
    if i != ',' and i != '.' and i != '!' and i != ' ':
        num_chars += 1


print(num_chars)