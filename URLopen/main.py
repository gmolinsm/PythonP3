from urllib.request import urlopen

counter = 0

link = str(input("Please enter URL: "))
keyword = str(input("Please enter keyword: "))

page = urlopen(link)
for line in page:
    line = line.decode()
    pos = 0
    while True:
        pos = line.find(keyword, pos)
        if pos != -1:

            counter += 1
            pos += 1
        else:
            break
print(counter)