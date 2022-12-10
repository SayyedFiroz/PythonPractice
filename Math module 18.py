Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #18 Important maths functions
>>> x=sqrt(25)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x=sqrt(25)
NameError: name 'sqrt' is not defined
>>> #we need to Import math module for this
>>> import math
>>> x=sqrt(25)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x=sqrt(25)
NameError: name 'sqrt' is not defined
>>> x=math.sqrt(25)
>>> print(x)
5.0
>>>  x=9.3
...  
SyntaxError: unexpected indent
>>> x=9.3
>>> print(math.ceil(x))
10
>>> print(math.floor(x))
9
>>> 3**2
9
>>> print(math.pow(3,2))
9.0
>>> #use function in big software instead of simple 3**2
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> print(math.logx(x))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(math.logx(x))
AttributeError: module 'math' has no attribute 'logx'. Did you mean: 'log'?
print(math.log(x))
2.2300144001592104
#ALIAS (as) is used short form the module name
import math as m
m.sqrt(25)
5.0
#Importing specific fuction from the module
from math import pow,sqrt
pow(3,2)
9.0
sqrt(25)
5.0
