# The __name__ variable (two underscores before and after) is a special Python variable. It gets its value depending on how we execute the containing script.

print("part 1")
print("hello ",__name__)

# if you run on this file it will show main but when you import on another file eg in Calc file it will show module name


print("2")
import Calc

print("hello")

# the main()function in calc will not run in this file it will only run on Calc