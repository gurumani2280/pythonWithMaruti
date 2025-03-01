#Understanding float() function: Converting Other(int, bool, str) data types to float data type.

#int to float:
c = 20
print(c, type(c)) #output: 20 <class 'int'>
d = float(c)
print(d, type(d)) #output: 20.0 <class 'float'>

c = 0
print(c, type(c)) #output: 0 <class 'int'>
d = float(c)
print(d, type(d)) #output: 0.0 <class 'float'>


#bool to float:
e = True
print(e, type(e)) #output: True <class 'bool'>
f = float(e)
print(f, type(f)) #output: 1.0 <class 'float'>

e = False
print(e, type(e)) #output: False <class 'bool'>
f = float(e)
print(f, type(f)) #output: 0.0 <class 'float'>
#While converting bool to float True is converted as 1.0 and False will be converting as 0.0.

#str to float:
e = '10'
print(e, type(e)) #output: 10 <class 'str'>
f = float(e)
print(f, type(f)) #output: 10.0 <class 'float'>

e = '10.25'
print(e, type(e)) #output: 10.25 <class 'str'>
f = float(e)
print(f, type(f)) #output: 10.25 <class 'float'>

e = 'True'
print(e, type(e)) #output: True <class 'str'>
f = float(e) #ValueError: could not convert string to float: 'True'
print(f, type(f)) #output: ValueError: could not convert string to float: 'True'
#Note: Any int/float value in string format will be able to convert it to float. But other than int/float value in string format can't be converted to float. It can be bool or string'
#Error: ValueError: invalid literal for int() with base 10.




