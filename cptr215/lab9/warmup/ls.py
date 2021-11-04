import sys
import os

working_dir = os.getcwd()

result_list = []

for dirname, subdirs, files in os.walk(working_dir):
    for i in subdirs:
        result_list.append(i + "/")
    for file in files:
        result_list.append(file)

result_list = sorted(result_list, key=str.lower)
for i in result_list:
    print(i)
