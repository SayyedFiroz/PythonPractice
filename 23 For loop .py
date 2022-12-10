# 23 For loop

   # It is done when iteration is known.
   # Used for iterating over a sequence (lIST,TUPLE,DICTIONARY,SET, STRING)

# Simple
x=['Firoz',79,'Sayyed',23]
print(x)
print()

# Using FOR loop for getting value one ny one
x=['Firoz',79,'Sayyed',23]
for  i in x:
    print(i)
print()

# FOR loop for iterating string
y = "firoz"
for i in y:
    print(i)
print()

# List within FOR loop
for i in [2,3,'firoz']:
    print(i)
print()

# Range in FOR loop
for i in range(5,51,5):
    print(i)
print()

# Reverse in range
for i in range(50,4,-5):
    print(i)
print()

# EX print num 1 to 100 which is not divisible by 5
for i in range(1,101):
    if (i%5!=0):
        print(i)



