#List creation:
x = []
print(type(x)) #output: <class 'list'>

y = list()
print(type(y)) #output: <class 'list'>

x = [1, 2, 3]
print(type(x)) #output: <class 'list'>
print(len(x)) #output: 3
print(x[0]) #output: 1
print(x[1]) #output: 2
print(x[2]) #output: 3
print(x[-1]) #output: 3
print(x[-2]) #output: 2
print(x[-3]) #output: 1
print(x[::-1]) #output: [3, 2, 1]

#print(x.count()) #TypeError: list.count() takes exactly one argument (0 given).
print(x.count(1)) #output: 1
print(x.count(2)) #output: 1
print(x.count(3)) #output: 1
print(x.count(4)) #output: 0

#print(x.find()) #output: AttributeError: 'list' object has no attribute 'find'

print(x.index(3)) #output: 2
print(x.index(2)) #output: 1
print(x.index(1)) #output: 0
#print(x.index(10)) #ValueError: 10 is not in list

y = list('abc') #Converting string to list.
print(type(y)) #output: <class 'list'>
print(y) #output: ['a', 'b', 'c']
print(len(y)) #output: 3

y = list([1, 2, 3, 'abc'])
print(type(y)) #output: <class 'list'>
print(y) #output: [1, 2, 3, 'abc']
print(len(y)) #output: 4

y = list((1, 2, 3, 'abc'))
print(type(y)) #output: <class 'list'>
print(y) #output: [1, 2, 3, 'abc']
print(len(y)) #output: 4

y = list({1, 2, 3, 'abc'})
print(type(y)) #output: <class 'list'>
print(y) #output: [1, 2, 3, 'abc']
print(len(y)) #output: 4

y = list(range(1, 6))
print(type(y)) #output: <class 'list'>
print(y) #output: [1, 2, 3, 4, 5]
print(len(y)) #output: 5

#y = list('abc', 'xyz') #TypeError: list expected at most 1 argument, got 2

#print(y.split(" ")) #AttributeError: 'list' object has no attribute 'split'

a = "Python Programming is good"
b = a.split(" ")
print(b) #output: ['Python', 'Programming', 'is', 'good']
print(type(b)) #output: <class 'list'>





