import re

file = open("regexTest.txt")
sum = 0
regex = "[0-9]+"

for line in file:
    line = line.rstrip()
    numberStrings = re.findall(regex, line)
    for numbers in numberStrings:
        number = int(numbers)
        sum = sum +number

print(sum)
