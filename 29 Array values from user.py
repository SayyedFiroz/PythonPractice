# Create array by taking value from the user

# MANUALLY

from array import *

arr = array('i', [])

n = int(input("Enter the length of thr array :"))

for i in range(n):
    x = int(input("Enter the next value :"))
    arr.append(x)

print(arr)

# User asked the value and get index number of tha value

val = int(input("Enter the value to search :"))

k=0
for i in  arr:
    if i==val:
         print(k)
         break
    k+=1


print("......")
# Using function
print(arr.index(val))

