def hello():
    name = input("Enter the name: ")
    if len(name) < 1:
        name = "Harsha"
    print("Hello, ", name)

# Calling the function
hello()

#paramatersing the function
def hello1(name):
    print("Hello, ", name)

name = input("Enter the other name: ")
if len(name) <1:
    name = "vardhan"
hello1(name)

# default for paramater
def hello2(name = "world"):
    print("Hello, ", name)

hello2()
name = input("Enter the other name: ")
hello2(name)

