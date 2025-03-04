class Animal:
    legs = 4 #class or static variable
    def __init__(self, color): #self is reference variable
        print("This is inside Animal constructor")
        self.color = color #This is also creating instance variable
obj1 = Animal("White") #output: TypeError: Animal.__init__() missing 1 required positional argument: 'color'
print(obj1.legs, obj1.color)
'''
output:
This is inside Animal constructor
4 White
'''

obj2 = Animal("Black")
print(obj2.legs, obj2.color)
'''
output:
This is inside Animal constructor
4 Black
'''

obj3 = Animal("Brown")
print(obj3.legs, obj3.color)
'''
output:
This is inside Animal constructor
4 Brown
'''

#Assignment: Student constructor with name argument
#Employee class with different name
