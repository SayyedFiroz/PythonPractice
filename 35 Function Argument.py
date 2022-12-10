# we are declaring the value for the argument see it changes when we call function

print("Part 1")
def modify(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x",x)

b=100
print(id(b))
a=12
print(id(a))     # In programming language there can by pass by value or pass by reference python does not have both
modify(a)        # it will not change it is immutable it is string and int and it will make there reference same
print("a",a)

print("part 2")
def mod(lst):
    print(id(lst))
    lst[1] = 200
    print(lst)
    print(id(lst))

lst = [100,300,400]       # All id will be same beacuse list is mutable
print(id(lst))
print(lst)
mod(lst)
print(id(lst))

