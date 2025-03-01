#Print numbers from 1 to 10:

#Using while loop:
x = 1
y = 10

while x<=y:
    print(x, end=" ") #output: 1 2 3 4 5 6 7 8 9 10
    x=x+1
else:
    print("\nCondition become False. Hence, else block is printing") #output: Condition become False. Hence, else block is printing

#Using for loop:
#range(1, 11, 1) - range(start, end, step) - end value will be excluded and till n-1 is considered.
print(range(1, 11, 1)) #output: range(1, 11)
print(list(range(1, 11, 1))) #output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(range(1, 11, 1))) #output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(set(range(1, 11, 1))) #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Using for loop:
for item in range(1, 11, 1):
    print(item, end=" ") #output: 1 2 3 4 5 6 7 8 9 10
else:
    print("\nAll the elements in the range printed. Hence now else block is executed")  # output: Condition become False. Hence, else block is printing

try: #try catch
    x=5/0
except:
    print("This except block will be executed if exception is there")
else:
    print("This else block will be executed if exception is Not there")
finally: #this finally block will be executing irrespective of the exception occurring or not.
    print("This finally block will be executed in both the scenarios")



#print(z) #NameError: name 'z' is not defined
#x=5/0
#print(x) #output: ZeroDivisionError: division by zero
#name = "Python"
#print(int(name)) #output: ValueError: invalid literal for int() with base 10: 'Python'