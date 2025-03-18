input1 = input("Please enter any word: ")
dict1={}
for char in input1:
    value = dict1.get(char, 0) #It will return 0 instead of None.
    dict1[char] = value+1

print(dict1)

'''
output:
Please enter any word: I am learning Python
{'I': 1, ' ': 3, 'a': 2, 'm': 1, 'l': 1, 'e': 1, 'r': 1, 'n': 3, 'i': 1, 'g': 1, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1}
'''



