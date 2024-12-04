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

#print(sum)



sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

print(sf_population)