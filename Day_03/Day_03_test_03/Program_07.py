#Writing python program to solve below use case:
'''
If user enters
'0' then print 'Zero',
'1' then print 'one',
'2' then print 'two',
'3' then print 'three',
'4' then print 'four',
'5' to print 'five'.
Also, user enter any value lesser than 0 and greater than 5 should return out of range.
'''

input1 = int(input("Enter your number between '0' to '5': "))
x = ['zero', 'one', 'two', 'three', 'four', 'five']
if input1 < len(x) and input1 >= 0:
    print(x[input1])
else:
    print("Out of Range")

#output:
'''    
input: 0, output:  zero
input: 1, output:  one
input: 2, output:  two
input: 3, output:  three
input: 4, output:  four
input: 0, output:  five
input: -1, output:  Out of Range
input: 6, output:  Out of Range
'''