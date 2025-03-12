dict1={1: 'eleven', 25: "2.0", 10: 'xyz'}

for key in dict1.keys():
    print(key, dict1.get(key))
'''
output:
1 eleven
25 2.0
10 xyz
'''

for value in dict1.values():
    print(value)  #dict1.get(key) or dict1[key] is not supported for values
'''
output:
eleven
2.0
xyz
'''

for key,value in dict1.items():
    print(key,value)
'''
output:
1 eleven
25 2.0
10 xyz
'''

for key in dict1:
    print(key, dict1[key])
'''
output:
1 eleven
25 2.0
10 xyz
'''
#Note: In dictionary we can always get value from key but not key from values.
