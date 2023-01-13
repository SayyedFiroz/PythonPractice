# Inheritance :Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Base class,Super class,parent class :The class being inherited from.  derived class,sub class,child class :the class that inherits from another class.

# There are five types of inheritance in python : 1) Single inheritance   2)Multilevel inheritance  3)Multiple inheritance 4)Hierarchical inheritance 5)Hybrid inheritance

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

