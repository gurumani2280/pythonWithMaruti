#Print numbers from 10 to 1: Reverse order

#Using while loop:
x = 1
y = 10

while y>=x:
    print(y, end=" ") #output: 10 9 8 7 6 5 4 3 2 1
    y=y-1
else:
    print("\nCondition become False. Hence, else block is printing") #output: Condition become False. Hence, else block is printing

#Using for loop:
#range(1, 11, 1) - range(start, end, step) - end value will be excluded and till n-1 is considered.
print(range(10, 0, -1)) #output: range(1, 11)
print(list(range(10, 0, -1))) #output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(tuple(range(10, 0, -1))) #output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(set(range(10, 0, -1))) #output: {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}

#Using for loop:
for item in range(10, 0, -1):
    print(item, end=" ") #output: 10 9 8 7 6 5 4 3 2 1
else:
    print("\nAll the elements in the range printed. Hence now else block is executed")  # output: Condition become False. Hence, else block is printing
