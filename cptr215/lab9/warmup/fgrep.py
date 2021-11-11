import sys

search_word = sys.argv[1]
results = ""
i = 2
line_num = 0
count_lines = False
ignore_case = False

for k in sys.argv:
    if k == "-i":
        sys.argv.remove(k)
        ignore_case = True

for j in sys.argv:
    if j == "-n":
        sys.argv.remove(j)
        count_lines = True

while i < len(sys.argv):
    current_file = sys.argv[i]
    with open(current_file) as file:
        for lines in file:
            line_num += 1
            if ignore_case:
                if search_word.lower() in lines.lower() or search_word in lines:
                    results += lines
            elif not ignore_case:
                if search_word in lines:
                    results += lines

        if len(sys.argv) > 2 and count_lines == False:
            print(f"{current_file} {results}")
        elif len(sys.argv) <= 2 and count_lines == False:
            print(f"{results}")
        elif len(sys.argv) > 2 and count_lines == True:
            print(f"Line {line_num} {current_file} {results}")
        elif len(sys.argv) <= 2 and count_lines == True:
            print(f"Line {line_num} {results}")

        results = ""
    i += 1
