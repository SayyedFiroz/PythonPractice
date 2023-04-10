class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def __init__(self):
        super().__init__()                    # super() function is used to give access to methods and properties of a parent or sibling class
        print("in B init")
    def feature1(self):
        print("feature 1 is working")
    def feature3(self):
        print("feature 4 is working")


a1 = B()                     # B class still calling constructor of class A  ,CHANGES:WE didn't made init in class b till now

class C:
    def __init__(self):
        print("in C init")

    def feature4(self):
        print("feature 4 is working")

print("Method resolution order:1)left to wright,2)always A get the preference")

class D(A,C):
    def __init__(self):
        super().__init__()
        super().feature4()              # from super function we can call both init method and class method
        print("in D init")
    def feature5(self):
        print("feature 5 is working")


d1 = D()
