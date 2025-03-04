class Student:
    college = "IIT"
    uniform = "White & Grey"
    def __init__(self, name, id): #__init__ is a special method called as constructor which gets executed automatically at the time of object creation.
        self.name = name #self.name -> instance variable and name -> local variable
        self.id = id

    #Instance method:
    def print_student_details(self): #self signifies it is instance method
        print(f"Student name: {self.name}, Student Id: {self.id}")

    @classmethod
    def display_uniform(cls): #cls signifies it is class method.
        print(cls.college, cls.uniform) #when using class or static variable we use cls method instead of instance method(self)

    @staticmethod
    def maximum_of_two_numbers(input1, input2):
        return max(input1, input2)


obj1 = Student("Rahul", 101) #output: Inside the constructor of Student class
print(obj1.college, obj1.name, obj1.id) #output: IIT Rahul 101
obj1.print_student_details() #output: Student name: Rahul, Student Id: 101
obj1.display_uniform() #output: IIT White & Grey
print(obj1.maximum_of_two_numbers(55, 105)) #output: 105

obj2 = Student("Raju", 102)
print(obj2.college, obj2.name, obj2.id) #output: IIT Raju 102
obj2.print_student_details() #output: Student name: Raju, Student Id: 102
obj2.display_uniform()  #output: IIT White & Grey
print(obj2.maximum_of_two_numbers(15, 5))  #output: 15





