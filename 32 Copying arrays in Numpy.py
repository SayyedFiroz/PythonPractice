# Operation on array

from numpy import *

arr1 = array([1,2,4,5,])

arr2 = array([1,3,0,3])

arr1 = arr1 + 5                # adding 5 in each values of array

arr3 = arr1 + arr2            # vector adding two arrays

print(arr1)

print(arr2)

print(arr3)

print(sin(arr3))

print(log(arr3))

print(sqrt(arr3))

print(sum(arr3))

print(sort(arr3))

print(concatenate([arr1,arr2]))

# copying of array is two type shallow copy and deep copy

# shallow copy is if i change value of one array it will also change tha value of second array

ar1 = array([1,2,3,4])

ar2 = ar1

ar1[1] = 5                     # This is shallow copy because value of second array will als0 change

print(ar1)
print(ar2)

print(id(ar1))                  # they are not suitable both have same location
print(id(ar2))

ar2 = ar1.view()               # View is function create array at different location and it is shallow copy

print(id(ar2))

# Deep copy is not link with other array any changes to one array does not affect the other array

ar2 = ar1.copy()               # copy function is used.

ar1[1] = 10

print(ar1)
print(ar2)
