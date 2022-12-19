# This is second example of Special variable name
import calcu as cl

def fun1():
    cl.add()           # Need to import add func in fun1 from calcu
    print("from fun1")


def fun2():
    print("from fun2")

def main():
    fun1()
    fun2()

main()