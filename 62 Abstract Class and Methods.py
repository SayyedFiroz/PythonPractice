
# ABC(Abstract base class) Module : We use abc module to implement Abstract class

# Abstract class: An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.

# Abstract method :  An abstract method is a method that has a declaration( No body) but does not have an implementation.

# we cannot create object of abstract class

# need to define simple method for abstract method in child class

from abc import ABC, abstractmethod


class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("Running")


# com = computer()       # Can't create this object of this class
com1 = Laptop()
com1.process()