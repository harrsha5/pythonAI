import re

String = "123 is 3 digit number and not 5 digit number"

match = re.findall("[0-9]+", String)

sum = 0
for m in match:
    m= int(m)
    sum = sum+m

print(sum)


