# class : Blueprint for object

# how to create class :Using class keyword and giving name  to class keyword

# what does class contain  : it had attributed(variables) and behaviour( methods and functions)

class Computer:
    def config(self):
        print("i3 ,1tb")


com1 = Computer()                               # Constructor
com2 = Computer()



# how to call method from class
# Syntax : Class name.method name(Object name)

# Different object will have different behave that's why we need to put which object we want.


# 1st way

Computer.config(com1)
Computer.config(com2)

# 2nd way (it take as argument)

com1.config()
com2.config()


