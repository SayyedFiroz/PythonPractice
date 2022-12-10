
# Global Keyword : A global keyword is a keyword that allows a user to modify a variable outside the current scope(function).


# Difference between global and local

a = 10                 # Global variable : Anywhere in the program is accessible

def x():               # Local variable : Inside a function it is accessible and its given first preference inside function
    a = 15
    print("Inside Fun",a)


print("Outside Fun",a)
x()

# Declaring Global inside rhe function

def y():
    global a
    a = 20
    print("It will change 10 to 20:",a)

y()
print(a)

# Declaring Global and local variable inside a function and changing without affecting local  varible
# Globals to access memory address of Global varible

a = 12
print(id(a))

def Demo():
    a = 9
    x = globals()['a']               # Don't change the value of x it will make new variable
    print(id(x))
    print("Inside Fun",a)
    globals()['a'] = 14


Demo()
print(a)


