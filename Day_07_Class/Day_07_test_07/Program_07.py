class Student:
    college = "IIT"
    def __init__(self, name, id): #__init__ is a special method called as constructor which gets executed automatically at the time of object creation.
        self.name = name #self.name -> instance variable and name -> local variable
        self.id = id

    def print_student_details(self): #self signifies it is instance method
        print(f"Student name: {self.name}, Student Id: {self.id}")


obj1 = Student("Rahul", 101) #output: Inside the constructor of Student class
print(obj1.college, obj1.name, obj1.id) #output: IIT Rahul 101
obj1.print_student_details() #output: Student name: Rahul, Student Id: 101

obj2 = Student("Raju", 102)
print(obj2.college, obj2.name, obj2.id) #output: IIT Raju 102
obj2.print_student_details() #output: Student name: Raju, Student Id: 102





