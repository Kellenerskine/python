import sys
import os

# TODO: open every file
# TODO: count every line, word, char in every file using for loop

i = 1
total_num_lines = 0
total_num_words = 0
total_num_chars = 0

while i < len(sys.argv):
    filename = sys.argv[i]
    num_lines = 0
    num_words = 0
    num_chars = 0
    with open(filename) as file:
        for lines in file:
            line = lines.strip('\n')
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
        i += 1

    total_num_lines += num_lines
    total_num_words += num_words
    total_num_chars += num_chars
    if len(sys.argv) > 2:
        print(f"{num_lines} {num_words} {num_chars} {filename}")
    else:
        print(f"{num_lines} {num_words} {num_chars}")
print(f"total: {total_num_lines} {total_num_words} {total_num_chars}")

