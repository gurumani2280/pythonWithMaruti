#Understanding Type function:
x = 10
print(type(x)) #<class 'int'>
print(x) #x value is 10

x = 15.6
print(type(x)) #<class 'float'>
print(x) #x value is 15.6

x = True
print(type(x)) #<class 'bool'>
print(x) #x value is True

x = 'Python'
print(type(x)) #<class 'str'>
print(x) #x value is Python

x = [1,2,3,4,5]
print(type(x)) #<class 'list'>
print(x) #x value is [1, 2, 3, 4, 5]

x = (1,2,3,4,5)
print(type(x)) #<class 'tuple'>
print(x) #x value is (1, 2, 3, 4, 5)

x = {1,2,3,4,5}
print(type(x)) #<class 'set'>
print(x) #x value is {1, 2, 3, 4, 5}

x = {'a':1,'b':2,'c':3,'d':4,'e':5} #dictionary is key:value pair.
print(type(x)) #<class 'dict'>
print(x) #x value is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

name = input("Please enter your name: ")
print(type(name)) #<class 'str'>
print(name) #Maruti
#Note: input provided by using input function is always string.
'''Note: Input Function always accept string type input. Even though user give different type input 
python accepts that as string type input only.'''

name = input("Please enter input: ")
print(type(name)) #<class 'str'>
print(name) #123

name = input("Please enter your name: ")
print(type(name)) #<class 'str'>
print(name) #True