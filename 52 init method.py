#  __init__ method : It is Special method in python.
#  It is called as a constructor in object oriented terminology.
#  it allows the class to initialize the attributes of the class.

class Computer:
    def __int__(self,process,ram):
        self.process = process
        self.ram    = ram

    def config (self):
        print("config is ",self.process,self.ram)


com1 = Computer("i3",8)
com2 = Computer("i5",16)

