from numpy import *

arr1 = array([
    [1, 2, 4],
    [4, 5, 6],
    [3, 5, 6]
])

print(arr1.ndim)  # ndim to check array dimension
print(arr1.shape)  # shape give rows and columns

arr2 = arr1.flatten()  # Multi dimensional array to single  array

print("arr2 -- multi to single array")
print(arr2)

arr3 = arr2.reshape(3, 3)  # Single array to 2d array (ROWS,COLUMN)

print("arr3 --1d to 2d array")
print(arr3)

arr2 = array([[1, 2, 4, 5, 1, 2], [1, 2, 4, 5, 1, 2]])
print(arr2)

arr4 = arr2.reshape(2, 2, 3)
print("arr4 --2d to 3d")
print(arr4)

# CONVERT ARRAY INTO MATRIX because we can perform more operation

M = matrix(arr2)
print(arr2)

m1 = matrix('1 2 3 ;3 2 1 ')  # ; to separate row
print("m1")
print(m1)

# three row three column

m2 = matrix('1 2 3 ;3 2 1 ')

print("m2")
print(m2)

print(diagonal(m2))          # to get diagonal element
print(m2.max())              # max element

print("addition of the matrix")

m3 = m1 + m2;
print(m3)

# multiplication of matrix

# resultant matrix need to be like if m3 is 3*2 and m4 is 2*3 then m5 will be 3 of m3 and 2 of m4 = 3*2

# if u have same size it will show error


m3 = matrix('1 2  ;2 3 ;3 2 ')


print("m3")
print(m3)


m4 = matrix('1 2 3 ;2 3 4 ')

print("m4")
print(m4)

print("Multiplication of the matrix")

m5 = m3 * m4;
print(m5)





