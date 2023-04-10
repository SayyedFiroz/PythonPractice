
# Method overloading : Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.

# Method overloading (ways) : 1) Method name same ,argument number different 2) Method name same,argument declaring None 3) Diapatch(module) Same method name,Dut difinin data type of different args.



class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):  # We use None when we don't have to assign value
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(58, 69)

print(s1.sum(5))


# Method Overriding :the method in the child class is  to override the method in the parent-class.


class A:
    def show(self):
        print(" in a show")

class B(A):
    # pass
    def show(self):                  # This method override the class A method.
        print("in a b show")
a1 = B()
a1.show()


