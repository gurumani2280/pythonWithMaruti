#Writing program to pring sum of number 1 to 10:

#while loop:
x=1
y=10
sum=0
while x<=y:
    sum=sum+x
    x=x+1
print(sum) #output: 55

#Formula:
print(y*(y+1)//2) #output: 55, --> n*(n+1)//2 - is the formula to print sum of n natural numbers.

#for loop:
sum2=0
for item in range(1, 11, 1):
    sum2=sum2+item
print(sum2) #output: 55

