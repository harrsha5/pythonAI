name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
myDict = {}
for lines in fh:
    if not lines.startswith("From "):
        continue
    words = lines.rstrip().split()
    word = words[5].split(":")[0]
    myDict[word] = myDict.get(word, 0) + 1

for key, value in sorted(myDict.items()):
    print(key, value)


