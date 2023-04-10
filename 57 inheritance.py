# Inheritance :Inheritance allows us to define a class that inherits all the methods and properties from another class.


# Base class,Super class,parent class :The class being inherited from.  derived class,sub class,child class :the class that inherits from another class.


# There are five types of inheritance in python : 1) Single inheritance   2)Multilevel inheritance  3)Multiple inheritance 4)Hierarchical inheritance 5)Hybrid inheritance


# Single inheritance :child class to inherit properties from a single parent class"

class A:
    def feature1(self):
        print("This is feature 1")

class B(A):
    def feature2(self):
        print ("This is feature 2")


a1 = A()
a1.feature1()

b1 = B()
b1.feature1()
b1.feature2()
print("  ")
# Multi level inheritance :features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

class C(B):
    def feature3(self):
        print("This is feature 3")

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()

# Multiple inheritance :When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.

class D:
    def feature4(self):
        print("this is feature 4")

class E(A,D):
    def feature5(self):
        print("this is feature 5")


e1 = E()


e1.feature1()
e1.feature4()
e1.feature5()





# hierarchical inheritance : when multiple child class inherit single parent class

class z:
    def featurez(self):
        print("This is feature z")
class x(z):
    def featurex(self):
        print("this is featurex")

class c(z):
    def featurec(self):
        print("this is featurec")

class v(z):
    def featurev(self):
        print("this is featurev")

v1 = v()

v1.featurez()

# Hybrid inheritance : when all the types of in heritance is used.
