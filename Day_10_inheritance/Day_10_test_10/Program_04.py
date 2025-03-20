class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        print(self.first_name, self.last_name)

obj1 = Person("Rahul", "Bhatia")
obj1.printName() #output: Rahul Bhatia

class Student(Person): #Person is parent class name
    def __init__(self, first_name, last_name):
        print("Constructor of child class")


obj2 = Student("Rajath", "Bhatia") #Constructor of child class
obj2.printName() #output: AttributeError: 'Student' object has no attribute 'first_name'



