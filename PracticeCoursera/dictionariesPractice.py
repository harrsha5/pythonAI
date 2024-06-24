# Dictionaries Practice

#two ways to declare a dictionary
x = {'a': 1, 'b': 2, 'c': 4}
y = dict()
y['d'] = 5
y['e'] = 6
y['e'] = y['e']+2

print(y['e'])

z = {'string': "test string", 'number': 1, 'float': 0.45}

x.update(y)
x.update(z)

print('f' in x)
print('e' in x)

print(x)

stuff = dict()
print(stuff.get('candy',-1))
