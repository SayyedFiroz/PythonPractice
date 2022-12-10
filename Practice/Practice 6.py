# Q1 print 1 2 3 4
        # 2 3 4
        # 3 4
        # 4

# Q2 print A P Q R
#          A B Q R
#          A B C R
#          A B C D

#Q1
#m1
x = 4
for i in range(x):
    for j in range(x-i):
        print(j+i+1, end=" ")
    print()


# m2
for i in range(4):
    for j in range(i+1,5):
        print(j, end=" ")
    print()
#Q2

s1='ABCD'
S2='PQR'
for  i in range (4):
        print(s1[0:i+1]+S2[i:4])

st1='abcd'
st2='pqr'
print(st1[:1]+st2[1:])