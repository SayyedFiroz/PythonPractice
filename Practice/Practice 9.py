# 1) write a code to add 2  arrays using forloop.

from numpy import *
ar1 = array([1,2,3])
ar2 = array([3,2,1])
ar3 =array([])

for i in ar1:
    for j in ar1:
        ar3 = ar1 + ar2
print(ar3)


# 2) write a code to find the maximum value from an array without using in built function.

from numpy import *
arr=array([11,22,33,58,55])
max=0
for i in arr:
    if max<i:
        max=i
print("The maximum value in the array is",max)




"""if ar[0] > ar[1] and ar[0] > ar[2]:
    print(ar[0])
    if ar[1] > ar[2] and ar[1] > ar[0]:
        print(ar[1])
        if ar[2] > ar[0] and ar[2] > ar[1]:
            print(ar[2]) """

