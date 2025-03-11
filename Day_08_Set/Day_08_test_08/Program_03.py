set1={10, 15, 20, 20, 30, 10}
print(set1) #output: {10, 20, 30, 15}

print(set1.pop()) #output: 10
print(set1) #output: {20, 30, 15}

#print(set1.pop(30)) #output: TypeError: set.pop() takes no arguments (1 given) -> since pop() take index argument and set doesn't support indexing hence pop(index) doesn't support in set.


#discard():
print(set1.discard(30)) #output: None -> not returning anything
print(set1) #output: {20, 15}

print(set1.discard(50)) #output: None -> not returning anything, if element not there also doesn't throw any error.
print(set1) #output: {20, 15}


#remove():
print(set1.remove(20)) #output: None -> not returning anything
print(set1) #output: {15}

#print(set1.remove(50)) #output: KeyError: 50 -> since 50 is not in set throwing KeyError


#clear():
print(set1.clear()) #None
print(set1) #output: set()