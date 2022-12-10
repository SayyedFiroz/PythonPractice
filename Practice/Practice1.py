# write code find cube of num and take input also use cmd

# without cmd
x = int(input("Enter the number :"))
cube = x**3
print("This is cube of your num : " + str(cube))

# with cmd
import sys
a = int(sys.argv[1])
b = a**3
print("Cube of the num using cmd : " + str(b))