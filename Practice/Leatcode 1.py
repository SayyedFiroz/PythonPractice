# possibility of adding numbers only 1 and 2 can be used to split
# eg 3
# 1+2 = 1
# 2+1 = 1
# 1+1+1 = 1

x = 4
a = 1
b = 2
c = 1 + 1 + 1
d = 0

for i in range(x+1):
    a=+1
    c=+1
    b=+1
    if x==a+b:
        d=+1
        if x==a+b:
            d=+1
            if x==b+a:
                d=+1
                print(i)

