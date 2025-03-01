#Addition or Summation of two user input values.
number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")

sum = number_1 + number_2
print(number_1, number_2, "Sum is: ", sum) #Output: 105 55 Sum is:  10555.
#Since input() function always consider input value as string hence concatenation happened.

sum = int(number_1) + int(number_2)
print(number_1, number_2, "Sum is: ", sum) #Output: 105 55 Sum is:  160

"or"
#We can directly convert input value to int using int() function as below:
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

sum = number_1 + number_2
print(number_1, number_2, "Sum is: ", sum) #Output: 105 55 Sum is:  160.