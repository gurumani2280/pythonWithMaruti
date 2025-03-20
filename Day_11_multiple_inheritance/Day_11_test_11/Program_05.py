class A:
    def feature_1(self):
        print("This is feature_1 of class A")

class B:
    def feature_1(self):
        print("This is feature_1 of class B")

class C(B, A):
    def feature_1(self):
        print("This is feature_1 of class C")
        super().feature_1() #Inherit from super class based on the inheritance order

objC = C()
objC.feature_1()

'''
output:
This is feature_1 of class C
This is feature_1 of class B
'''







