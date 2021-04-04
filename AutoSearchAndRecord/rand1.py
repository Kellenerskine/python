import json
import datetime


curr_date = datetime.datetime.now().strftime("%m/%d/%Y")

file = open("recordKeeping.txt", "r+")
prev_data = file.read()
file.truncate()
data = json.loads(prev_data)
curr_count = data.get(curr_date, -1)
if curr_count == -1:
    # date not in dictionary yet
    data[curr_date] = 0
print(data)