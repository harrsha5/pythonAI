# Printing the entire text using read() function
fname = input("Enter file name: ")
x= input(4)
fh = open(fname)
file = fh.read(10)
print(file.upper())

# Printing the entire text using readlines() function
fname = input("Enter file name: ")
fh = open(fname)
file = fh.readlines()
print(file)

# Printing the entire text file using for loop
fname = input("Enter file name: ")
fh1 = open(fname)
for l in fh1:
    print(l.rstrip().upper())


# Printing the first ten lines of the text file using for loop
fname = input("Enter file name: ")
fh1 = open(fname)
num = 0
for l in fh1:
    if num < 10:
        print(l.rstrip().upper())
        num = num+1




