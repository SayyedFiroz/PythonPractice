
#Using while
i=2
x=int(input("enter the prime number :"))
while i<=x:
    if x%i==0 or x==1:
        print("It is not prime number")
        i=+1
        break
    else:
        print("It is a prime number")
        break



print()
# Using for
num = int(input("Enter the number :"))
for i in range(2,num//2):
    if num % i == 0:
        print("Not Prime")
    else:
        print("Prime")
        break