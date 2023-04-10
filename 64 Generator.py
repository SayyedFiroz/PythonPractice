# Generator :  A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.

# topten sq value

def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()

print(values.__next__())
print(values.__next__())
