
# read data

"""f = open('mydata','r')             # mode = r,w,a,

print(f.readline(),end="")                # method = read(whole file),readline(single line),write
print(f.readline())"""

# write data                         # write the file as new will remove all data

"""
f = open('mydata','w')
f.write("my name is firoz")"""

# append data
"""
f = open('mydata','a')
f.write("i am sd\n")

"""

# copy data from one file to another

"""f = open('mydata','r')

f1= open('abc','a')

for data in f:
    f1.write(data)"""


# open image and copying                        # image in binary


f = open('bitc.jpg','rb')

f1 = open('web3.jpg','wb')

for i in f:
    f1.write(i)