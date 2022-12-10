
# keyword variable length argument: It is different from variable length argument anf it has keywor argument
# ** for KVLA and * for VLA

def person(name,**data):
    print(name)
    print(data)

person('firoz',age=18,city='mumbai',number = 6464654689)

# we can also use for loop for printing data

def person(name,**data):
    print(name)
    age = 0
    for i,j in data.items():
        print(i,j)


person('firoz',age=18,city='mumbai',number = 6464654689)

def person(name,age):
    print(name)
    print(age)

person('firoz',19)




