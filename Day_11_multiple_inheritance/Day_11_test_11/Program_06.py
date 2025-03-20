class A:
    def feature_1(self):
        print("This is feature_1 of class A")

class B:
    def feature_1(self):
        print("This is feature_1 of class B")

class C(B, A):
    def feature_1(self):
        print("This is feature_1 of class C")
        A.feature_1(self) #Inherit from super class based on the inheritance order
#Note: super() will always inherit from the first in-order class. If we need to inherit from any other class we can directly use class_name.method()

objC = C()
objC.feature_1()

'''
output:
This is feature_1 of class C
This is feature_1 of class 
'''







