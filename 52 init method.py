#  __init__ method : It is Special method in python.
#  It is called as a constructor in object-oriented programming.
#  it allows the class to initialize the attributes of the class.

class Computer:

    def __init__(self, ram, process):
        self.ram = ram
        self.process = process

    def config(self):
        print("Config : ", "Ram is", self.ram, "Model is", self.process)


com1 = Computer(8, 'i3')
com2 = Computer(16, 'ryzen 3')

com1.config()
com2.config()
