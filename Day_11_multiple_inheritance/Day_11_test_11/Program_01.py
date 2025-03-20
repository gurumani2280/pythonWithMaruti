class A:
    def feature_1(self):
        print("This is feature_1 of class A")

class B:
    def feature_2(self):
        print("This is feature_2 of class B")

class C(A, B):
    def feature_3(self):
        print("This is feature_3 of class C")

objC = C()
objC.feature_1() #This is feature_1 of class A
objC.feature_2() #This is feature_2 of class B
objC.feature_3() #This is feature_3 of class C





