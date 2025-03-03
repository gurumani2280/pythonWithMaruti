#Create a function which takes keyword arguments and print all keyword arguments:

def user_date_function(**input): #** -> Keyword argument, It is dictionary internally.
    print(input, type(input))
user_date_function() #output: {} <class 'dict'>
#user_date_function(30) #TypeError: user_date_function() takes 0 positional arguments but 1 was given
user_date_function(name="Arjun")
user_date_function(name="Rahul", age=25)
user_date_function(name="Tilak", age=25, occupation="Student")

'''
output:
{} <class 'dict'>
{'name': 'Arjun'} <class 'dict'>
{'name': 'Rahul', 'age': 25} <class 'dict'>
{'name': 'Tilak', 'age': 25, 'occupation': 'Student'} <class 'dict'>
'''

'''
while defining function:
positional 
keyword: **
default
variable length: *

while calling:
positional
keyword
'''
