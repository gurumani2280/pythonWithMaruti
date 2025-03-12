dict2={1: 'eleven', 25: "2.0", 10: 'xyz'}

print(dict2) #output: {1: 'eleven', 25: '2.0', 10: 'xyz'}
del dict2[1]
print(dict2) #output: {25: '2.0', 10: 'xyz'}
#del dict2[1] #output: KeyError: 1 -> Key 1 is not present so throwing KeyError

#pop()
#dict2.pop() #output: TypeError: pop expected at least 1 argument, got 0
#dict2.pop(1) #output: KeyError: 1, Key 1 is not present
dict2.pop(25)
print(dict2) #output: {10: 'xyz'}

#popitem()
dict2.popitem()
print(dict2) #output: {} -> Since only one element was there so it removed that
dict3={1: 'eleven', 25: "2.0", 10: 'xyz'}
dict3.popitem()
print(dict3) #output: {1: 'eleven', 25: '2.0'} -> removed key 10 here.

#clear()
print(dict3.clear()) #output: None, clear() returns None.
print(dict3) #output: {}
print(dict3.clear()) #output: None

dict4={1: 'eleven', 25: "2.0", 10: 'xyz'}
#dict4.remove(1) #AttributeError: 'dict' object has no attribute 'remove'
print(dict4) #
