from googlesearch import search
from datetime import date
today = date.today()

p = open("recordKeeping.txt", "w+")
counter = 0
p.write('Date: %s' % (today))
p.close()
while True:
    r = open("recordKeeping.txt", "a+")
    r.close()
    o = open("recordKeeping.txt", "a+")
    o.write('   - Number of searches: %s\n' % (counter))
    query = "never gonna give you up"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        print("")
    counter += 1
    print("You have searched 'Never Gonna Give You Up' ", counter, " times")

    data2 = o.readlines()
    o.close()

    g = open("recordKeeping.txt", "r")
    data = g.readlines()
    g.close()
    print(data)
    del data[1]
    print(data)

    j = open("recordKeeping.txt", "w+")
    for line in data:
        j.write('%s' % (data))
    j.close()