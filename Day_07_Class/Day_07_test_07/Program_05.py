class Animal:
    legs = 4 #class or static variable
    def __init__(self): #self is reference variable
        print("This is inside Animal constructor")
        self.color = "White" #This is also creating instance variable
obj1 = Animal()
print(obj1.legs, obj1.color)
'''
output:
This is inside Animal constructor
4 White
'''

obj1 = Animal()
print(obj1.legs, obj1.color)
'''
output:
This is inside Animal constructor
4 White
'''



