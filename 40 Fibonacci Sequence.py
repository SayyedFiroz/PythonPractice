# Creating Fibonacci series function
def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("Invalid number try positive number")
        if n == 1:
            print(a)
            print(b)
    if n > 1:
        print(a)
        print(b)

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

        if c <= n:
            print(c)


fib(100)
