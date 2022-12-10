# 1) Create an array with 5 values & delete the value at index no. 2 without using in-built function.
print("1)")
from array import *

arr =array('i',[])

n = 5


for i in range(n):
    x = int(input("Enter the values :"))
    arr.append(x)

print(arr)


s=0
for i in arr:
    s+=1
    if s==2:
        arr.remove(s)

print(arr)


print("2)")
# 2) write a code to reverse an array without using in-built function.

arr = array('i',[1,2,3,4])
arr1 = array('i',[])


for i in range(len(arr),0,-1):
    arr1.append(i)
    arr.remove(len(arr))

arr = array(arr1.typecode,(a for a in arr1))

print(arr)


