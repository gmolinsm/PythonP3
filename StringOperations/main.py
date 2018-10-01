string = "hello"
print(string[0])
print(string[-4])
print(len(string), "\n\n\n")

b = "*"
count = 1
for a in string:
    print(a+count*b)
    count += 1

print("\n\n\n")

print(string[0:2])
print(string[2:])
print(string[:])
print(string[0:4:2])
print(string[4:0:-1])
print(string[::-1])

print("\n\n\n")

print("Hello" < "hello")
print("z" > "abcdefg")
print("a" >= "aa")

print("\n\n\n")

s = "http://google.com and then http://yahoo.com or even http://bbc.co.uk"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    break