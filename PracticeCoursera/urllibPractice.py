import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")

for line in fhand:
    print(line.decode().strip())


# word counter from the text file
fhand1 = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
print(type(fhand1))

my_dict = {}
for line in fhand1:
    words = line.decode().rstrip().split()
    for word in words:
        my_dict[word] = my_dict.get(word,0) + 1

for key, value in my_dict.items():
    print(key, value)

