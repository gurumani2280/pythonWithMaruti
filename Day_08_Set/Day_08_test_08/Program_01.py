#Set creation:
#type 1:
x = {} #empty flower braces represents 'dict' but with atleast one item it represents 'set'
print(type(x)) #output: <class 'dict'>

#type 2:
y = set() #set() function also represents 'set'
print(type(y)) #output: <class 'set'>


x = {1, 2, 3}
print(type(x)) #output: <class 'set'>
print(len(x)) #output: 3
#print(x[0]) #output: TypeError: 'set' object is not subscriptable -> Set doesn't support indexing


#a. count():
#print(x.count()) #AttributeError: 'set' object has no attribute 'count'.

#b. find():
#print(x.find()) #output: AttributeError: 'set' object has no attribute 'find'

#Operations with set() function:
y = set('abc') #Converting string to set.
print(type(y)) #output: <class 'set'>
print(y) #output: {'b', 'c', 'a'} #set doesn't maintain order.
print(len(y)) #output: 3

y = set([1, 2, 3, 'abc'])
print(type(y)) #output: <class 'set'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = set((1, 2, 3, 'abc'))
print(type(y)) #output: <class 'set'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = set({1, 2, 3, 'abc'})
print(type(y)) #output: <class 'set'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = set(range(1, 6))
print(type(y)) #output: <class 'set'>
print(y) #output: (1, 2, 3, 4, 5)
print(len(y)) #output: 5

#y = set('abc', 'xyz') #TypeError: set expected at most 1 argument, got 2 -> set() function expects only one argument.

z = y.copy()
print(z) #output: {1, 2, 3, 4, 5}
print(type(z)) #output: <class 'set'>

z.add(10) #set supports add() instead of append()
print(z) #output: {1, 2, 3, 4, 5, 10}
print(y) #output: {1, 2, 3, 4, 5}

y.add(25)
print(z) #output: {1, 2, 3, 4, 5, 10}
print(y) #output: {1, 2, 3, 4, 5, 25}