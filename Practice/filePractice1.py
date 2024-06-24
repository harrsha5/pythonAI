# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0.0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s = s + float(line.lstrip('X-DSPAM-Confidence:    '))
    counter = counter+1

print('Average spam confidence:', (s/counter))