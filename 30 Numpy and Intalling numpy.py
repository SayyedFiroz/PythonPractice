# why numpy module not array module

# let's try 2d array in array module
"""   from array import *
        arr =array('i',[1,2,3],[2,3,4])

It will show error """

# we use numpy module because it can have more than one dimensional array e.g. 2d array; 3d array....

# numpy is third party module need to install it using pip(preferred installer program)

import numpy as np

arr = np.array([[1, 2, 5], [3, 2, 4], [2, 34, 5]],int)

print(arr)


