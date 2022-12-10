# 1 Print First 50 fibonacci series

a = 0
b = 1
c = 1
while c < 49:
    if a == 0:
        print(a)
    elif b == 1:
        print(b)
    x = a + b
    a = b
    b = x
    c += 1
    print(x)

# Check the given  number is prime number is not
num = int(input("Enter the number to check :"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not prime number")

for i in range(5):
    if i==3:
        continue
    print(i)
