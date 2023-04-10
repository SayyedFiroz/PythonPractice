
# Thread : Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
# It is concurrent

# Three parts : 1) beginning 2) execution 3) conclude

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("hello")
            sleep(0.5)

class hii(Thread):
    def run(self):
        for i in range(10):
            print("hii")
            sleep(0.5)


t1 = Hello()
t2 = hii()

t1.start()
sleep((0.2))
t2.start()


t1.join()
t2.join()
print("Bye")                    # Execute by main thread