#Understanding int() function: Converting Other(float, bool, str) data types to int data type.

#float to int:
c = 20.4
print(c, type(c)) #output: 20.4 <class 'float'>
d = int(c)
print(d, type(d)) #output: 20 <class 'int'>

c = 0.0
print(c, type(c)) #output: 0.0 <class 'float'>
d = int(c)
print(d, type(d)) #output: 0 <class 'int'>


#bool to int:
e = True
print(e, type(e)) #output: True <class 'bool'>
f = int(e)
print(f, type(f)) #output: 1 <class 'int'>

e = False
print(e, type(e)) #output: False <class 'bool'>
f = int(e)
print(f, type(f)) #output: 0 <class 'int'>
#While converting bool to int True is converted as 1 and False will be converting as 0.

#str to int:
e = '10'
print(e, type(e)) #output: 10 <class 'str'>
f = int(e)
print(f, type(f)) #output: 10 <class 'int'>

e = '10.25' #Float value in string format cannot be converted to int.
print(e, type(e)) #output: 10.25 <class 'str'>
f = int(e) #ValueError: could not convert string to float: 'True'
print(f, type(f)) #output: #ValueError: invalid literal for int() with base 10: '10.25'

e = 'Python'
print(e, type(e)) #output: Python <class 'str'>
f = int(e) #ValueError: could not convert string to float: 'True'
print(f, type(f)) #output: ValueError: invalid literal for int() with base 10: 'Python'
#Note: Any int value in string format will be able to convert it to int. But other than int value in string format can't be converted to int. It can be float, bool or string'.
#We get Error: "ValueError: invalid literal for int() with base 10."




