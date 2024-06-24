str = "test1 test2 test3"
x= str.split()
print(x, type(x))
# when you split a string and store in a variable, it becomes a list type
# lists in poython can be defined by list() or []
str1 = "Please learn Python to reach greater heights"
stuff = str1.split()
count = 0
for w in stuff:
    if(count==len(stuff)-1):
        print(w)
    else:
        print(w, end=",\n") # removing the comma (,) at the last word
    count = count +1

print(len(str1))
print(len(stuff))
print(stuff[2:])
print(stuff[0:3])

x= list(range(5))
print(x, type(x))

fruit = 'Banana'
#fruit[0] = 'b'
print(fruit[0:4])

l= list()
print(dir(l))