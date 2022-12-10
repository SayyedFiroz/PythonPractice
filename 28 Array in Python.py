# Array : All the value of same type

# Advantage : No fixed value, Expand ,Shrink

# DisAdvantage :Memory wastage

# Each array has unique letter to describe value and each value is of two type signed and unsigned.
# Signed array :Negative to postive value and Unsigned array :zero to positive value
# eg i ,I :signed Int,Unsigned Int  ; u : unicode character ; f : float........


# Ex 1

from array import *                           # * means all property of import module eg array module

vals = array('i', [1, 2, -3, 4, 5])

vals.reverse()

print(vals.buffer_info())                     # buffer_info : This function get address and size if an array

print(vals.typecode)                          # typecode : Value Type

print(vals[2])                                # indexing

print('......')

# method 1 Directly without indexing
for i in vals:                                # Iterating or printing
    print(i)

print('......')
# method 2 Indirectly with indexing
for i in range(len(vals)):
    print(vals[i])

print('......')

# EX 2
vars = array('u',['a','b','c','d'])

vars.reverse()

print(vars.buffer_info())
print(vars.typecode)
print(vars)

for i in vars:
    print(i)

print('.....')

# Creating new array from already created array
newArray = array(vals.typecode, (a*a for a in vals))

for i in newArray:
    print(i)

print('....')

# Iteration using while loop
i=0
while i<len(newArray):
    print(newArray[i])
    i+=1



