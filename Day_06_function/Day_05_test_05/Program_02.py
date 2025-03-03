#Create a python function to add two input numbers and return the sum.

def sum(input1, input2):
    print("Inside sum function and it is used to sum two input values", input1, input2)
    return input1+input2 #return is not mandatory but can be used to return some value.
#sum() #TypeError: sum() missing 2 required positional arguments: 'input1' and 'input2'
#sum(10) #TypeError: sum() missing 1 required positional argument: 'input2'
sum(10, 15) #output: Inside sum function and it is used to sum two input values 10 15
print(sum(10, 15)) #return value can be printed using print() function.
'''output:
25
Inside sum function and it is used to sum two input values 10 15.
'''
c = sum(10, 15)
print(c) #output: 25
print(c+25) #output: 50

print(sum(input2=10, input1=15)) #By default Python takes first value for first argument and second for second argument. But we can explicitely change the value by specifying the argument and it's value.
'''
output:
Inside sum function and it is used to sum two input values 15 10
25
'''
#print(sum(input2=10, 20)) #SyntaxError: positional argument follows keyword argument
#Here input2 is keyword argument and 20 is positional argument. Providing positional argument after keyword argument is not supported.

print(sum(20, input2=10))
'''
output: 
Inside sum function and it is used to sum two input values 20 10
30
'''

#print(sum(20, input1=10)) #TypeError: sum() got multiple values for argument 'input1'