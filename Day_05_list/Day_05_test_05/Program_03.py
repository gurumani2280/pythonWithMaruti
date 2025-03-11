#Removing or Deleting items from the list.
#[] -> Subscripting

#del keyword: It will delete the values.
x = [10, 20, 30, 40, 50]
print(x) #output: [10, 20, 30, 40, 50]
del x[2]
print(x) #output: [10, 20, 40, 50]
#del x[10] #IndexError: list assignment index out of range

#b. pop(): pop() always removes last element unless any argument is passed.  If any index value is passed as an argument then element in that particular index will be removed.
print(x.pop()) #output: 50 -> Last element is removed.
print(x) #output: [10, 20, 40]
print(x.pop()) #output: 40
print(x) #output: [10, 20]

x = [10, 20, 30, 40, 50]
print(x.pop(1)) #output: 20, Since index value is passed element present in that index is removed.
print(x) #output: [10, 30, 40, 50]

#print(x.pop(20)) #output: IndexError: pop index out of range

x = []
#x.pop() #output: IndexError: pop from empty list -> Can't use pop() for empty list as it can't remove any element.

#remove(): element value as argument
x = [10, 20, 30, 40, 50]
print(x.remove(20)) #output: None
print(x) #output: [10, 30, 40, 50]

#x.remove(20) #output: ValueError: list.remove(x): x not in list

#del is used to delete variable.
x = 50
print(x)
del x
print(x)

#pop(): Takes index as argument removes element present in that index.
#remove(): takes element value as an argument removes that element where ever it present.
#list1 = [1, 2, 2, 3]