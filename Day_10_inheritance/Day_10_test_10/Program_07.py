class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print("Constructor of parent class")

    def printName(self):
        print(self.first_name, self.last_name)

    def isStudent(self):
        print("Not a Student")


obj1 = Person("Rahul", "Bhatia")
obj1.printName() #output: Rahul Bhatia
obj1.isStudent() #output: Not a Student

class Student(Person): #Person is parent class name
    def __init__(self, first_name, last_name):
        print("Constructor of child class")
        super().__init__(first_name, last_name)

    def isStudent(self):
        print("Yes, a Student")


obj2 = Student("Rajath", "Bhatia") #Constructor of child class
obj2.printName() #output: AttributeError: 'Student' object has no attribute 'first_name'
obj2.isStudent() #output: Yes, a Student




