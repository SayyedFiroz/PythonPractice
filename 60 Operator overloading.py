
# Operator overloading : Operator Overloading means giving extended meaning beyond their predefined operational meaning.

# ex : operator + is used to add two integers as well as join two strings and merge two lists.
# It is achievable because ‘+’ operator is overloaded by int class and str class.

# EX 1

a,b= 6,5
print(a + b)

a,b="hello","world"
print(a + b)

# conclusion : Same add operator perform two different on different variable first is int class calling __add__() and second is string class calling __add__()


# Magic method : In build method like __add__(),__sub__(),__mul__() are called magic method .

# EX 2

class int:
    def __init__(self, a: object, b: object) -> object:
        self.a = a
        self.b = b

    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        c = int(a,b)

        return c

    def __gt__(self,other):
        if self.a > self.b:
            return True
        else:
            return False

    def __str__(self):
         a = self.a
         b = self.b
         return '{} {}'.format(self.a,self.b)





i1 = int(8,9)
i2 = int(9,9)

i3 = i1 + i2

if i1 > i2:
    print("i1 wins")
else:
    print("i2 wins")

print(i3)    # its calling __str__ method

