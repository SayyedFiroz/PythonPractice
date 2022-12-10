# USER INPUT
# String
x = input("Enter the 1st Number : ")  # 10
y = input("Enter the 2nd Number : ")  # 20
z = x + y  # Z=1020

print(z)

print(type(x))

# Integer
# We need to convert string into int
A = input("Enter the 1st number : ")
C = int(A)
B = input("Enter the 2nd number : ")
D = int(B)
F = C + D
print(C + D)

# Best way without wasting variable
x = int(input("enter the first number : "))
y = int(input("enter the second number: "))
z = x + y
print("this number is z :" + str(z))

# Character
ch = input('enter the char : ')
print(ch)

""""If someone type string instead of char then"""
char = input('enter the char : ')[0]
print(char)

# Function Eval
""" If i want to pass expression as input value and the ans will be result"""

# without eval
ch = input("enter the expression : ")
print(ch)

# with eval
result = eval(input("enter an expression ::"))
print(result)