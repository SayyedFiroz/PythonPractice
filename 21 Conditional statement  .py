# Conditional Statement 21

#If conditoion
#1
if  True or False:
    print("its true")
print("it will always print because it is not in if suite(block)")
#1.2
x = 100
n = x%2
if n==0:
    print("it is even")

if n==1:
    print("it is odd")

# 2 if else condition (for better code efficiency)
a = 99
b = a%2
if b==0:
    print("even")
else:
    print("odd")

# 3 nested if (if inside if only difference is identation)
d = 21
e = d%2
if (e==0):  # If this condition true then it will execute smaller greater if false direct odd statement
    print("even")
    if(d<10):
        print("smaller")
    else:
        print("greater")
else:
    print("odd")

# 4 if elif else (It is same as mutiple if the only difference is that it will stop if condition is met (efficieny))

# Taking number as int and given output as string by looping
number = int(input("enter the number between 0 to 3 :"))
if number==0:
    print("zero")
elif number==1:
    print("one")
elif number==2:
    print("two")
elif number==3:
    print("three")
else:
    print("wrong number")





