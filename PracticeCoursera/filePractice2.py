# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = list()
counter = 0
for line in fh:
    if line.startswith("From "):
        var = line.rstrip().split()[1]
        s.append(var)
    counter = counter +1

print(type(s))

for x in s:
    print(x, end="\n")

print("There were", len(s), "lines in the file with From as the first word")

