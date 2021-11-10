import sys

search_word = "" + sys.argv[2]
results = ""
i = 3

while i < len(sys.argv):
    current_file = sys.argv[i]
    with open(current_file) as file:
        for lines in file:
            line = lines.split()
            for word in line:
                if word == search_word:
                    results += lines


    i += 1

print(results)
