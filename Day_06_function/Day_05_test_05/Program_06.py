#Create a function which takes variable length arguments and return sum:

'''
def sum__ _func(input1=75, input2=30): #SyntaxError: invalid syntax, empty space is not allowed between variable/function/method/class name.
    return input1+input2, input1-input2 #returning multiple values as tuple
'''
#Note: Variable length argument is considered as tuple internally.
def sum_function(*input): #* -> Variable length argument can take any number of argument and process accordingly.
    print(input, type(input))
    return sum(input)
print(sum_function())
print(sum_function(5))
print(sum_function(5, 10))
print(sum_function(5, 10, 15))
print(sum_function(5, 10, 15, 20))
print(sum_function(5, 10, 15, 20, 25))
'''
output:
() <class 'tuple'>
0
(5,) <class 'tuple'>
5
(5, 10) <class 'tuple'>
15
(5, 10, 15) <class 'tuple'>
30
(5, 10, 15, 20) <class 'tuple'>
50
(5, 10, 15, 20, 25) <class 'tuple'>
75
'''
