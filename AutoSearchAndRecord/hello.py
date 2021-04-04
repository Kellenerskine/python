from googlesearch import search
from datetime import date

counter = 0
while True:
    query = "never gonna give you up"
    search(query, tld="co.in", num=1, stop=1, pause=2)

    counter += 1
    print("You have searched 'Never Gonna Give You Up' ", counter, " times")

    with open('recordKeeping.txt', 'w') as f:
        time = date.today()
        f.write('%s\nNumber of times searched: %s' % (time, counter))
        f.close()