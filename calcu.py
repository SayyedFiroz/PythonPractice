# This is part of file 49

def add():
    print("result 1",__name__)            # if you run standalone(on this file) it will show main

def sub():
    print("result 2")

def main():
    print("in cal main")
    add()
    sub()
if __name__=="__main__":           # it will not run this thing when you import but it can use the function outside of this main
        main()
        print("under the main")
