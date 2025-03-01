#For loop can be used along with string, list, tuple, set, dictionary, dictionary.items(), range() function and any iterable objects.
#for loop with string:
for item in "Python":
    print(item, end=" ") #output: P y t h o n

print() #to separate between above and below programs.

#for loop with list:
for item in [10, 15.5, "abc", True, False]:
    print(item, end=" ") #output: 10 15.5 abc True False

print() #to separate between above and below programs.

#for loop with tuple:
for item in (10, 15.5, "abc", True, False):
    print(item, end=" ") #output: 10 15.5 abc True False

print() #to separate between above and below programs.

#for loop with set: Set is not ordered and it will not allow duplicates.
for item in {10, '10', 15.5, 15.5,  "abc", "abc", True, False, True, False}:
    print(item, end=" ") #output: False True 10 10 15.5 abc

print() #to separate between above and below programs.

for item in {1:10, 2:'10', 3:15.5, 4:15.5,  5:"abc", 6:"abc", 6:True, 7:False, 8:True, 6:False}:
    print(item, end=" ") #output: 1 2 3 4 5 6 7 8 --> Only keys are printed and there is no duplicates of keys.

print() #to separate between above and below programs.

#for loop with dictionary: dictionary is key:value pair
dict0 = {1:10, 2:'10', 3:15.5, 4:15.5,  5:"abc", 6:"abc", 6:True, 7:False, 8:True, 6:False}
for item in dict0:
    print(item,dict0[item], end=", ") #output: 1 10, 2 10, 3 15.5, 4 15.5, 5 abc, 6 False, 7 False, 8 True, #in case of duplicate keys dictionary will pick the latest value as it doesn't allow duplicates.

print() #to separate between above and below programs.

#for loop with dictionary: dictionary is key:value pair
dict1 = {1:10, 2:'10', 3:15.5, 4:15.5,  5:"abc", 6:"abc", 6:True, 7:False, 8:True, 6:False}
for key,value in dict1.items():
    print(key,value, end=", ", sep="-") #output: 1-10, 2-10, 3-15.5, 4-15.5, 5-abc, 6-False, 7-False, 8-True,
#Note: default seperator is space for multiple values used in print statement which can be changed using 'sep' argument.




