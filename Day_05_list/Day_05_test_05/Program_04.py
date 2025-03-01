#Tuple: Creation. -->
x = ()
print(type(x)) #output: <class 'tuple'>

x = (1)
print(type(x)) #output: <class 'int'>

x = (1.0)
print(type(x)) #output: <class 'float'>

x = ('x')
print(type(x)) #output: <class 'str'>

x = (1,)
print(type(x)) #output: <class 'tuple'>

x = (1, 2)
print(type(x)) #output: <class 'tuple'>





y = tuple('abc') #Converting string to list.
print(type(y)) #output: <class 'tuple'>
print(y) #output: ('a', 'b', 'c')
print(len(y)) #output: 3

y = tuple([1, 2, 3, 'abc'])
print(type(y)) #output: <class 'tuple'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = tuple((1, 2, 3, 'abc'))
print(type(y)) #output: <class 'tuple'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = tuple({1, 2, 3, 'abc'})
print(type(y)) #output: <class 'tuple'>
print(y) #output: (1, 2, 3, 'abc')
print(len(y)) #output: 4

y = tuple(range(1, 6))
print(type(y)) #output: <class 'tuple'>
print(y) #output: (1, 2, 3, 4, 5)
print(len(y)) #output: 5

#y = tuple('abc', 'xyz') #TypeError: tuple expected at most 1 argument, got 2

#Note:
y = (1, 2, 3, 'abc')
#print(y.append('xyz')) #output: AttributeError: 'tuple' object has no attribute 'append'
#print(y.insert(0, 10)) #output: AttributeError: 'tuple' object has no attribute 'insert'
#y.pop() #output: AttributeError: 'tuple' object has no attribute 'pop'
#y.remove(1) #output: AttributeError: 'tuple' object has no attribute 'remove'
#y[1] = 50 #output: TypeError: 'tuple' object does not support item assignment
