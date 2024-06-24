for i in "banana":
    print(i) # prints all the letters in a word

print("-------------")

i = 0
while i<(len("potato")): #prints all the letters in a word
    letter = "potato"[i]
    print(letter)
    i = i+1

print("-------------")

#counts how many times a given letter is present in the word
count = 0
word = "Harrsha"
for i in word:
    if i== "r":
        count = count +1
print(count)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = '40'
y = int(x) + 2
print(y)

x = 'From marquard@uct.ac.za'
print(x[8])

x = 'From marquard@uct.ac.za'
print(x[14:17])

greet = 'Hello Bob'
print(greet.upper())

text = "X-DSPAM-Confidence:    0.8475"
x= text.find('0')
print(x)
new_text = text[x:]
print(type(new_text))
new_text = float(text[x:])
print(type(new_text))
print(new_text)

print("Sri","name","text", sep='/',end='')
print("something")

# print(*objects, sep=' ', end='\n', file=None, flush=False)

x= 'Harsha'
print("Hello", x)

name = input("Enter your name? ")
name = name.strip() # strips the extra white spaces
name = name.title() # Captilizes the first letter of the sentence
name = name.strip().title() # two actions at the same time
print("Your name is", name)


x = int(input("Enter a number "))
print (x)






