dict1={1: 'eleven', 25: "2.0", 10: 'xyz'}

print(dict1.keys()) #output: dict_keys([1, 25, 10])
print(dict1.values()) #output: dict_values(['eleven', '2.0', 'xyz'])
print(dict1.items()) #output: dict_items([(1, 'eleven'), (25, '2.0'), (10, 'xyz')])

#dict1.update(11, 50) #output: TypeError: update expected at most 1 argument, got 2
dict1.update({11:50, 12:75.25, 13:'100'})
print(dict1) #output: {1: 'eleven', 25: '2.0', 10: 'xyz', 11: 50, 12: 75.25, 13: '100'}

