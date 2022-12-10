

# Actual arguments are four types of argument
# 1)Default argument
# 2)Positional argument
# 3) Keyword argument
# 4)Variable-length arguments a) Arbitrary positional arguments (*args) b) Arbitrary keyword arguments (**kwargs)


print("2)Positional argument")
# We give argument according to their position

def add(a, b):          # when declaring(a,b) it is Formal argument
    c = a + b
    print(c)


add(5, 4)               # when calling(a,b) it is known as Actual argument



print("3) Keyword argument")
# We know the argument name but not the postion then we used keyword argument

def person(name,age):
    print(name)
    print(age-5)

person(age=19,name='firoz')



print("1) Default argument")
# We default the argument in declaration so no need to call it ,call it when we need to change the argument

def person(name,age=18):
    print(name)
    print(age)

person('firoz')
person('firoz',20)            # If i pass value it will update/override it

print("4) Variable length")
# We use this when we need to take n number of parameter


"""def sum(a,*b):              # a will be fixed and b will be tuple
    c = a+b
    print(c)                # it will not work

sum(2,8,11,15)"""


def sum(*b):
    c = 0
    for i in b:
        c = c + i

    print(c)

sum(2,8,11,15)






