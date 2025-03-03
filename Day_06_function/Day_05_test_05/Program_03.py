#Create a function which takes two arguments and return sum and difference both:

def sum_diff_func(input1, input2):
    return input1+input2, input1-input2 #returning multiple values as tuple
print(sum_diff_func(input1=40, input2=15)) #output: (55, 25)
print(sum_diff_func(input1=70, input2=35)) #output: (105, 35)
print(sum_diff_func(input2=45, input1=90)) #output: (135, 45)
print(sum_diff_func(input2=145, input1=90)) #output: (235, -55)



