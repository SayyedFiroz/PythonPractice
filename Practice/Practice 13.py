class Exam_Data:

    college_name = "sies college"

    @classmethod
    def clg_name(cls):
        return cls.college_name

    def __init__(self,eng,maths,phy,chem,it):
        self.eng = eng
        self.maths = maths
        self.phy  = phy
        self.chem = chem
        self.it = it

    def pass_fail(self):
        marks = [ self.eng , self.maths , self.phy , self.chem , self.it ]
        for i in marks:
            if i >= 35:
                print("pass")
            else:
                print("fail")


    def avg (self):
        return (self.eng + self.maths + self.phy + self.chem + self.it) / 5

    def per(self):
        return ((self.eng + self.maths + self.phy + self.chem + self.it) / 500 ) * 100



firoz  = Exam_Data(18,95,65,87,99)
bushra =  Exam_Data(90,45,45,37,97)

print(Exam_Data.clg_name())
print(firoz.pass_fail())
print(firoz.avg())
print(firoz.per())
