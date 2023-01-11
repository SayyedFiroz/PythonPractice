# There are three types of methods in python.

# 1)instance methods : Have parameter self, Bound to object , Called by object name , No decorator

# Instance methods are two types : 1) Accessor methods : get_method(fetch the variable)  2)Mutator Methods : set_method(modify the variable).

# 2)class methods: Have parameter cls ,Bound to class , Called by object and class name , @classmethod decorator required

# 3)static methods: No parameter required , Bound to class , Called by object and class name , @staticmethod decorator required


class Student:

    school = 'new model english school'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance method because of self points to object
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # accessor  (getter:getting the variable)
        return self.m1

    def set_m1(self, value):  # modifier (setter:change the value)
        self.m1 = value
        return self.m1

    @classmethod                # It is decorator
    def get_school(cls):              # class method (we use cls to access class variable)
        return cls.school

    @staticmethod                 # Static method(It is independent of class variable  and instance variable)
    def info():
        print("This is Student data")

s1 = Student(74, 23, 23)
s2 = Student(87, 32, 24)

print(s1.avg())

print(s1.m1)  # Directly fetching variable

print(s1.get_m1())
s1.set_m1(99)
print(s1.get_m1())

print(Student.get_school())
print(s1.get_school())
Student.info()

