# Array can be created in 6 ways

print("1)")
# 1) array()
from numpy import *

arr = array([1, 2, 3, 4, 5.0])  # convert data type implicitly

print(arr.dtype)

print(arr)

print("2)")
# 2) linspace()

arr1 = linspace(0,15,3)   #linspace(start value,end value,number of values in parts will be divided)

print(arr1)

print("3)")
# 3) arange()

arr2 = arange(2,21,2)       # similar to range

print(arr2)

print("4)")
# 4) logspace()

arr3 = logspace(1,40,5)     # logspace (start with 10 raise 1,end with 10 raise 5,In 5 parts)

print(arr3)

print('%.2f'%arr3[0])      # Converting into numbers at 0 index

print("5)")
# 5) zeros()

arr4 = zeros(10,int)        # creating array of ten zero

print(arr4)

print("6)")
# 6) ones()

arr5 = ones(3)             # creating array of ones of three times

print(arr5)



