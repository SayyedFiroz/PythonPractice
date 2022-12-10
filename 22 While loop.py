# 22 while loop

# while is used to repeat the statement multiple times until it becomes true and stop

"""example: Someone says tell your name five
you will count number in your head everytime you say name"""

i=1                         # Initialization
while i<=5:                 # Condition
    print("firoz")  # Statement/Function
    i+=1                    # Increment/Decrement

# If you won't give increment it will loop infinitely

# Nested while with end =" " parameter
j=1
while j<=5:
    print(" Sayyed :",end=" ")
    k=1
    while k<=5:
        print("Mohd Firoz",end="")
        k+=1
    j+=1
    print()

print("Khan",end="")
print(" chacha",end="")
