import sys

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
            line = lines.split()
            num_lines += 1
            num_words += len(line)
            num_chars += len(lines)
        i += 1

    total_num_lines += num_lines
    total_num_words += num_words
    total_num_chars += num_chars
    if len(sys.argv) > 2:
        print(f"{num_lines} {num_words} {num_chars} {filename}")
    else:
        print(f"{num_lines} {num_words} {num_chars}")

if len(sys.argv) > 2:
    print(f"{total_num_lines} {total_num_words} {total_num_chars} Total")
elif len(sys.argv) == 1:
    print("No file was specified.")
