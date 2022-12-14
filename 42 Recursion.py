# Recursion: Recursion is the process of defining something in terms of itself/(A Function which calling itself ).


# 1
def greet1():
    print("Hello! 1")
    greet1()  # It won't print unlimitedly it will stop after 1000 times by python


greet1()

# 2
# To get the limit of recursion

import sys  # To run this code remove the (#1) from above

print(sys.getrecursionlimit())


def greet2():
    print("Hello! 2")
    greet2()


# 3
# To increase the limit of recursion

import sys

sys.setrecursionlimit(2000)  # To run this code remove the (#1) from above
i = 0


def greet3():
    global i
    i += 1
    print("Hello! 3", i)
    greet3()


greet3()
