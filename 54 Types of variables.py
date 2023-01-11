# There are two types of variable in oops.

# Instance variable :Define variable inside init method ,it is dynamic ,Value can be changed to single object.
# Ex: company and milage in Class car.

# Class(Static) variable : Define variable inside the class,it is static,it applies to all object .
# Ex: wheels in Class car



# Namespace : an area where you create/map and store object/variable
# ex wheels are class namespace
# ex comp,mil are instance namespace



class Car:
    wheels = 4

    def __init__(self):
        self.comp = "BMW"
        self.mil = 10


c1 = Car()
c2 = Car()

Car.wheels = 3                          # Class variable :It will change the wheels variable of all object

c1.comp = "BMW"                         # Instance variable :It will change to specific instance
c1.mil = 20

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
