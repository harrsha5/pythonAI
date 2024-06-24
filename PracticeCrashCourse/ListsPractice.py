# first way defining a list is directly creating a list with values in the list
bicycles = ["Ranger", "Super Ranger", "Hero"]
print(bicycles)

# Second way is directly creating an empty list and appending values 
motorcycles = []
motorcycles.append( "Hero honda")
motorcycles.append("Pulsur")
print(motorcycles)

# Third way is inserting the values in the list
cars = []
cars.insert(0,"Honda Civic")
cars.insert(1,"Sonata")
cars.insert(2,"CRV")

print(cars)

# Updating a value of the element in list by using Insert method
cars.insert(0,"Mazda")
print(cars)

# Removing an element from the list using del statement
clothes = ['t-shirts','pants','shirts','v-neck shirts', 'joggers']
print("Before removing: ",clothes)
del clothes[2]
print("After removing: ", clothes)

# Removing an element from the list using remove method
clothes = ['t-shirts','pants','shirts','v-neck shirts', 'joggers']
print("Before removing: ",clothes)
clothes.remove('v-neck shirts')
print("After removing: ", clothes)

# Removing an element from the list usind pop() method - If just pop() is used, the it will remove the last element
music = ['drums','piano','guitar','flute']
print("Before removing: ", music)
removedElement = music.pop()
print("After removing: ", music)
print("Removed element: ", removedElement)

# Removing an element from the list usind pop() method - If the index is passed for pop() method, then the respective element will be removed from the list
music = ['drums','piano','guitar','flute']
print("Before removing: ", music)
removedElement = music.pop(1)
print("After removing: ", music)
print("Removed element: ", removedElement)


