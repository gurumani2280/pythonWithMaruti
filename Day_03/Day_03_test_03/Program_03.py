#Slicing Operation:

x="Python Programming"

#slicing syntax: [start:end:step] but end index is exclusive(will not be included).
y = x[1:5:2]
print(y) #output: yh

y = x[7:18:1]
print(y) #output: Programming

y = x[7:18] #step is taking 1 by default.
print(y) #output: Programming

y = x[7:] #end takes end index by default.
print(y) #output: Programming

y = x[:6] #start takes first index by default. ie; '0' index
print(y) #output: Python

y = x[:] #end takes end index by default.
print(y) #output: Python Programming

#Slicing using negative step:
y = x[5::-1] #end takes end index by default.
print(y) #output: nohtyP

y = x[5:-19:-1] #end takes end index by default.
print(y) #output: nohtyP

