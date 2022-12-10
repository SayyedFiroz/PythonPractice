# 25 Printing pattern

# EX 1 ####
       ####
       ####
       #### in one print.


# from 4#
for i in range(0, 4):
    print(" # # # # ")

print()

# from 1#
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print() # very important for making new line

print()

# EX 2      #
            # #
            # # #
            # # # #


 # First way
for i in range (4):
    if i==0:
        print("# ")
    elif i==1:
        print("# #")
    elif i==2:
        print("# # #")
    elif i==3:
        print("# # # #")

# By row and column method
for i in range (5):
    for j in range(i):
        print("#",end=" ")
    print()

print()

# EX 3 # # # #
       # # #
       # #
       #
print("ex3")
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()