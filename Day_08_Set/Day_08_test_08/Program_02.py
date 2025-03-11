#add():
set1={10, 15, 20, 20, 30, 10}
print(set1) #output: {10, 20, 30, 15}

set1.add(17)
print(set1) #output: {10, 15, 17, 20, 30}

set1.add(17)
print(set1) #output: {10, 15, 17, 20, 30} -> add() has no effect if the element is already present.

#update():
#set1.update(17) #output: TypeError: 'int' object is not iterable -> update() expect iterable object only single item/element can't update single element.

set1.update([17])
print(set1) #output: {10, 15, 17, 20, 30} -> 17 is already present so doesn't update with value 17

set1.update((18, 'xyz'))
print(set1) #output: {10, 'xyz', 15, 17, 18, 20, 30}

set1.update("python")
print(set1) #output: {'n', 10, 'p', 'xyz', 'h', 15, 'o', 17, 18, 20, 'y', 't', 30} -> string is added as separate elements


