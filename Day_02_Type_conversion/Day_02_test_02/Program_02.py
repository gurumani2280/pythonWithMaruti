#Understanding bool() function: Converting Other(int, float, str) data types to bool data type.

#Int to bool:
a = 10
print(a, type(a)) #output: 10 <class 'int'>
b = bool(a)
print(b, type(b)) #output: True <class 'bool'>

a = 0
print(a, type(a)) #output: 0 <class 'int'>
b = bool(a)
print(b, type(b)) #output: False <class 'bool'>
#Note: Any int value other than 0(False) is considered as True.

#Float to bool:
c = 20.4
print(c, type(c)) #output: 20.4 <class 'float'>
d = bool(c)
print(d, type(d)) #output: True <class 'bool'>

c = 0.0
print(c, type(c)) #output: 0.0 <class 'float'>
d = bool(c)
print(d, type(d)) #output: False <class 'bool'>
#Note: Any float value other than 0.0(False) is considered as True.

#Str to bool:
e = 'Python'
print(e, type(e)) #output: Python <class 'str'>
f = bool(e)
print(f, type(f)) #output: True <class 'bool'>
#Note: Any data type can be converted to string using str() function.

e = ''
print(e, type(e)) #output:   <class 'str'>
f = bool(e)
print(f, type(f)) #output: False <class 'bool'>
#Note: Any String value other than empty string('' or "" or '''''' or """""")(False) is considered as True.



