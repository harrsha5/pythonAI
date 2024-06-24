fileName = input("Enter the file name ")
fh = open(fileName)

my_dict = {}

for line in fh:
    if not line.startswith("From "):
        continue
    words = line.rstrip().split()
    word = words[1]
    my_dict[word] = my_dict.get(word, 0) + 1

'''print(my_dict)'''
maxValue = 0
maxKey = None
for key, value in my_dict.items():
    if value > maxValue:
        maxValue = value
        maxKey = key

print(maxKey, maxValue)










