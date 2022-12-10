# what is function?

# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# function can return data as a result.

# Function are two types 1) Inbuilt fun ex :print(),sqrt(),etc and 2)User defined function

# def (defining function) great (function name) ()(Its function not variable) :(Contain multiple statement)

def greet():
    print("hello")
    print("Good morning")

greet()

# addition of two numbers

def add(a,b):              # Function taking two argument/parameter
    c = a + b
    print(c)

add(5, 4)



# Function have two type one is no returen and second is return
# First type ex: hey firoz call aqsa and tell tomorrow i will be late for the session conclusion:I don't need response(no return)
# Second type ex: hey firoz call aqsa and ask what time is tomorrow session conclusion:I need response(return)

def addd(x,y):
    z = x+y
    return z

result=addd(4,3)         # It will not print result unless you aassign
print(result)

def add_sub(x,y):
    z=x+y
    a=x-y
    return z,a

result1,result2=add_sub(4,3)
print(result1,result2)

print(result1)



