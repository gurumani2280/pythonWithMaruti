input1 = input("Please enter any word: ")
dict1={}
for char in input1:
    if char in dict1:
        value = dict1[char]
        dict1.update({char:value+1})
    else:
        dict1.update({char:1})

print(dict1)

'''
output:
Please enter any wordPythonprogramming
{'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'p': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}
'''