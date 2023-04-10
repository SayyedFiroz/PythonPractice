
# Errror : Abnormality in code
# Three types of error in general :
# 1) Compile time error : During Compiling error is identified eg Syntax error :missing(:).
# 2) Logical error  : Wrong output : eg passing wrong name in string
# 3) Runtime error :  no logical error and error after compiling (it does not show the line where exception occur) : eg zero divide e



# Exception :  Exceptions are raised when the program is syntactically correct, but the code resulted in an error. This error does not stop the execution of the program
# , however, it changes the normal flow of the program.
# eg zerodivide exception,indexoutofbound


"""print(".....Ex 1...........")

a = 5                # a,b is normal statement it will not give error
b = 0

print(a/b)          # This is critical statement it can give error

# It will show zero divide error
"""


"""
print("......How to handle error or exception.......")

a = 5
b = 0

try:
    print("resource open")
    print(a/b)
    print("resource close")

except Exception as e:
    print("Number cannot be divide by zero",e)

finally :
    print("resource close")

"""

# All error/exception have name like zero divide,value error ,index out of bound
# we can handle multiple exception trough name

a = 5
b = 2


try:
    print(a/b)                          # first exception
    k = int(input("enter the number"))  # second exception i will put char in this

except ZeroDivisionError as e:
    print("Number cannot be divide by zero",e)

except ValueError as e:
    print("Wrong input")

except Exception as e :               # It handles all the excetion
    print("Some went wrong")
finally :
    print("resource close")
