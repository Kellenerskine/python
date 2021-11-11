import sys

search_word = sys.argv[1]
lines = ""
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
                    if len(sys.argv) > 3 and count_lines == False:
                        print(f"{current_file}:{lines}", end='')
                    elif len(sys.argv) == 3 and count_lines == False:
                        print(f"{lines}", end='')
                    elif len(sys.argv) > 3 and count_lines == True:
                        print(f"{current_file}:{line_num}:{lines}", end='')
                    elif len(sys.argv) == 3 and count_lines == True:
                        print(f"{line_num}:{lines}", end='')
            elif not ignore_case:
                if search_word in lines:
                    if len(sys.argv) > 3 and count_lines == False:
                        print(f"{current_file}:{lines}", end='')
                    elif len(sys.argv) == 3 and count_lines == False:
                        print(f"{lines}", end='')
                    elif len(sys.argv) > 3 and count_lines == True:
                        print(f"{current_file}:{line_num}:{lines}", end='')
                    elif len(sys.argv) == 3 and count_lines == True:
                        print(f"{line_num}:{lines}", end='')
        line_num = 0

    i += 1
