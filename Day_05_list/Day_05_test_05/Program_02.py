#Updating of list:

x = [1, 2, 3, 4, 5]
print(x)
x[0] = 11 #0th index element is updating with 11.
print(x) #output: [11, 2, 3, 4, 5]

#x[5] = 65 #output: IndexError: list assignment index out of range
#print(x[10]) #output: IndexError: list index out of range

#apped(): It will append to the list as an end element.
x.append(6)
print(x) #output: [11, 2, 3, 4, 5, 6]

x.insert(-1, 570)
print(x) #output: [11, 2, 3, 4, 5, 570, 6]

x.insert(-10, 800)
print(x) #output: [800, 11, 2, 3, 4, 5, 570, 6]

#insert():
x.insert(2, 10)
print(x) #output: [800, 11, 10, 2, 3, 4, 5, 570, 6]
x.insert(8, 20)
print(x) #output: [800, 11, 10, 2, 3, 4, 5, 570, 20, 6]

x.insert(18, 200) #If index is not present in the list then element will be added to the lst index position.
print(x) #output: [800, 11, 10, 2, 3, 4, 5, 570, 20, 6, 200]

x.insert(-1, 500)
print(x) #output: [800, 11, 10, 2, 3, 4, 5, 570, 20, 6, 500, 200]



