
# Inner class : A class defined in another class is known as an inner class or nested class.

# A single object of the class can hold multiple sub-objects.

class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.laptop()                                        # Object creating outer class

    def show(self):
        print("Name of student :",self.name,"  Roll no :",self.roll)
        self.lap.show()



    class laptop:
        def __init__(self):
            self.name = "ACER"
            self.cpu = "i3"
            self.ram = 12

        def show(self):
            print("Name of Laptop :", self.name, " Cpu name :", self.cpu, " ram capacity ", self.ram)


s1 = student("Firoz",96)
s2 = student("bushra",6)

s1.show()
s2.show()

lap1 = s1.lap
lap2 = s2.lap

lap2.name = "asus"
lap2.cpu = "ryzen"
lap2.ram = 8

print(lap2.name)


