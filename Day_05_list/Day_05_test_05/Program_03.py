#Removing or Deleting items from the list.
#[] -> Subscripting

x = [10, 20, 30, 40, 50]
print(x) #output: [10, 20, 30, 40, 50]
del x[2]
print(x) #output: [10, 20, 40, 50]
#del x[10] #IndexError: list assignment index out of range

print(x.pop()) #output: 50
print(x) #output: [10, 20, 40]

print(x.pop()) #output: 40
print(x) #output: [10, 20]

x = [10, 20, 30, 40, 50]
print(x.pop(1)) #output: 20
print(x) #output: [10, 30, 40, 50]

#print(x.pop(20)) #output: IndexError: pop index out of range

x = []
#x.pop() #output: IndexError: pop from empty list

#remove(): element value as argument
x = [10, 20, 30, 40, 50]
print(x.remove(20)) #output: None
print(x) #output: [10, 30, 40, 50]

#x.remove(20) #output: ValueError: list.remove(x): x not in list

