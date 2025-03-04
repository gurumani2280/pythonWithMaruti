class Student:
    college = "IIT"
    def __init__(self): #__init__ is a special method called as constructor which gets executed automatically at the time of object creation.
        print("Inside the constructor of Student class")
obj1 = Student() #output: Inside the constructor of Student class
print(obj1.college) #output: IIT
print(obj1.__dict__) #output: {}
obj1.college = "NIT" #This is Instance variable with the name college. obj1 is reference variable
print(obj1.college) #output: NIT
print(obj1.__dict__) #output: {'college': 'NIT'},
print(Student.college) #output: IIT

obj2 = Student()
print(obj2.college) #output: IIT



