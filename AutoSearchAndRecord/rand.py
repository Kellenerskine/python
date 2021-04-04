import json
from datetime import datetime
from googlesearch import search


today = datetime.now().strftime("%m/%d/%Y")

file = open("recordKeeping.txt", "r+")
prev_data = file.read()
file.truncate()
data = json.loads(prev_data)
curr_count = data.get(today, -1)
if curr_count == -1:
    # date not in dictionary yet
    data[today] = 0
    curr_count = 0
print(data)

while True:
    query = "never gonna give you up"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        print()
    curr_count += 1
    data[today] = curr_count
    print("You have searched 'Never Gonna Give You Up' ", curr_count, " times")
    file.seek(0)
    file.truncate()
    file.write(json.dumps(data))