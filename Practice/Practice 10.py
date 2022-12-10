# Matrix multiplication

from numpy import*
m1 = array([[1,2],[2,3]],'i')
m2 = array([[1,2],[2,3]],'i')
m3 = array([[0,0],[0,0]])

for i in range(2):
    for j in range(2):
        for k in range(2):
            m3[i, j] = m1[i, k] * m2[k, j] + m3[i, j]

print(m3)





