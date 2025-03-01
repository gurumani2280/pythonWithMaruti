#Logical operation with string is rarely used but can be performed.
'''
- ASCII values are used to compare strings
- It doesn't matter how many letters a string has but python always compares only the first letter.
    If first letter is same then it will compare the second letter so on..
- 'b' is always greater than 'a' and 'aaaaaa'
'''

x = 'Python'
y = 'Selenium'

print(x < y) #output: True, Because P ASCII value is lesser than S ASCII value.

print(x > y) #output: False, Because P ASCII value is not greater than S ASCII value.

print(x <= y) #output: True, Because P ASCII value is lesser than or equal to S ASCII value.

print(x >= y) #output: False, Because P ASCII value is not greater than or equal to S ASCII value.

print(x == y) #output: False, Because P ASCII value is not equal to S ASCII value.

print(x != y) #output: True, Because P ASCII value is not equal to S ASCII value.

