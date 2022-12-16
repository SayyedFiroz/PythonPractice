# Decorators: A decorator takes in a function, adds some functionality and returns it

# ex

def div(a, b):
    print(a / b)


def deco(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = deco(div)

div(2, 4)
