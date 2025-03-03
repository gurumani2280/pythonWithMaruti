#Create a function which takes two arguments(one mandatory and other default/optional) and return sum and difference both:

#def sum_diff_func(input1=75, input2): #SyntaxError: non-default argument follows default argument.
#    return input1+input2, input1-input2 #returning multiple values as tuple

def sum_diff_func(input1=75, input2=30): #SyntaxError: non-default argument follows default argument.
    return input1+input2, input1-input2 #returning multiple values as tuple
print(sum_diff_func()) #output: (105, 45)
print(sum_diff_func(input1=40, input2=15)) #output: (55, 25)
print(sum_diff_func(input1=70, input2=35)) #output: (105, 35)
print(sum_diff_func(input2=45, input1=90)) #output: (135, 45)
print(sum_diff_func(input2=145, input1=90)) #output: (235, -55)

#
print(sum_diff_func(40)) #output: (70, 10)
print(sum_diff_func(input1=-70)) #output: (-40, -100)
#print(sum_diff_func(45, input1=90)) #TypeError: sum_diff_func() got multiple values for argument 'input1'
print(sum_diff_func(input2=0, input1=90)) #output: (90, 90)



