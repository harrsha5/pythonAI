'''fname = input("Enter file name: ")
fh = open(fname)
my_list = []
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in my_list:
            my_list.append(word)

print(my_list.sort())'''

fname = input("Enter file name: ")
try:
    with open(fname, 'r') as fh:
        my_list = []
        for line in fh:
            words = line.rstrip().split()
            for word in words:
                if word not in my_list:
                    my_list.append(word)

    my_list.sort()  # Sort the list alphabetically
    print(my_list)
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")