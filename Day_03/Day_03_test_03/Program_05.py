#Writing python program to compare two input numbers(Using conditional statements)
input1=int(input("Please enter first number: "))
input2=int(input("Please enter second number: "))

if input1>input2:
    print(f"{input1} is greater than {input2}")
elif input2>input1: #elif used to have an extra condition.
    print(f"{input2} is greater than {input1}")
else:
    print(f"{input1} is equal to {input2}")
'''
input1 = 25, input2 = 75 then output = 75 is greater than 25
input1 = 35, input2 = 15 then output = 35 is greater than 15
input1 = 99, input2 = 99 then output =99 is equal to 99
'''

