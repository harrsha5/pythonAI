set1 = set()
set1.add("first element")
set1.add(1)

print (set1)

set2={1,2,"fn","ln"}

print(set2)

 # sets are unordered and mutable
 # unordered in the sense - after you print the set observe the order that we added elements doesn't matter
 # mutable, meaning you can add or remove elements after their creation
 # the individual elements within the set must be immutable and cannot be changed directly.

a = [1,2,3,4]

set3 = set(a) # type casting the list to sets

print(len(set3))

# sets will not accept the duplicates
#set4 = set(1,1,2,2,3,3,4,4,5,5)
#print(set4)

# removing the dupliactes in the list by converting them to sets
list1 = [1,1,2,2,3,3,4,4,5,5]
set5 = set(list1)
print(set5)

