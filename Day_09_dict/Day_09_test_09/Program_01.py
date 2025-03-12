#Dictionary:

dict1 = {}
print(dict1, type(dict1)) #output: {} <class 'dict'>

dict2 = dict()
print(dict2, type(dict2)) #output: {} <class 'dict'>

dict1[1] = 1
dict1[2.0] = 2.0
dict1['abc'] = 'xyz'
print(dict1, len(dict1)) #output: {1: 1, 2.0: 2.0, 'abc': 'xyz'} 3


dict1[1] = 'one'
print(dict1) #output: {1: 'one', 2.0: 2.0, 'abc': 'xyz'}
#Dictionary will not allow duplicate keys if give duplicate it will take the latest one.

dict2={1: 'eleven', 25: "2.0", 10: 'xyz'}
print(dict2) #output: {1: 'eleven', 25: '2.0', 10: 'xyz'}
#print(dict2[2]) #output: KeyError: 2 -> Since the key 2 is not present it throws KeyError

print(dict2[10]) #output: xyz
print(dict2.get(1)) #output: eleven
print(dict2.get(2)) #output: None -> get() - if key is not there it returns None instead of throwing error.
