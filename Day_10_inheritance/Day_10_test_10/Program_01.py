class Person:
    #constructor method
    def __init__(self, first_name, last_name):
        self.first_name = first_name #left side is instance variable and right side is local variable
        self.last_name = last_name

    def printName(self): #This is instance method because self is there in the argument
        print(self.first_name, self.last_name)

obj1 = Person("Rahul", "Bhatia") #object of Person class
obj1.printName() #output: Rahul Bhatia


