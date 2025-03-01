#Slicing operations with String:
x="Python Programming"
print(x[0]) #output: P
print(len(x)) #output: 18
print(x[len(x)-1]) #output: g
print(x[-1]) #output: g
print(x[-len(x)]) #output: P

#'in' Operator: To check sub-string in main string.
print("S" in x) #output: False
print("g" in x) #output: True
print("G" in x) #output: False

#'not in' Operator: It is Reverse of 'in' operator ie; returns True if sub-string not present and returns False if sub-string present.
print("S" not in x) #output: True
print("g" not in x) #output: False
print("G" not in x) #output: True

#count() function:
print(x.count("P")) #output: 2, Since 'P' is present twice count() is returning 2.
print(x.count('P', 2, 17)) #output: 1
print(x.count('on', 2, 17)) #output: 1

#find() function:
print(x.find("P")) #output: 0
print(x.find("P", 2)) #output: 7
print(x.find('on', 2, 17)) #output: 4
print(x.find('ON')) #output: -1, It indicates the sub-string is not present in main string.

#split() function:
y=x.split(" ")
print(y) #output: ['Python', 'Programming']
y=x.split("o")
print(y) #output: ['Pyth', 'n Pr', 'gramming']










