#Interview question: Reversing the given string using while loop.
x = "Selenium"
y = len(x)-1 #7
output1 = ""

while y>=0:
    output1 = output1+x[y]
    y=y-1

print(output1) #output: muineleS

#Reverse printing string using string slicing operator(Important)
output2=x[::-1]
print(output2) #output:  muineleS

