# Polymorphism :polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

# Duck typing :If bird  can walk,swim,quack then it is a Duck,Same Duck can perform different behaviour.

class Laptop:
    def code(self,ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print("Running")
class Intellij:
    def execute(self):
        print("Compiling")

l1 = Laptop()

ide = Pycharm()

l1.code(ide)
        
        
# Conclusion : Same execute function but different behaviour according to their class