# Filter(): Filters a subset of elements that meets a certain (set of) condition(s). An example is to filter out sentences that contain a specific string.

# Map(): Perform the same operation on all elements in an iterable. An example is performing a log transformation on each element.

# Reduce(): Performs an operation on an iterable, yielding a single-valued outcome. A common example is to sum all elements in a list.


nums = [0, 1, 1, 2, 3, 5]

# filter ()
evens = list(filter(lambda n: n % 2 == 0, nums))  # filter syntax : variable =sequence data type(filter (function,iterable))
print("evens",evens)

# map()
doubles = list(map(lambda n: n * n, nums))  # map syntax :same as filter
print("doubles", doubles)

cube = list(map(lambda n: n ** 3, nums))
print("cube", cube)

# reduce()
# we need import functools module

import functools
sum_all = functools.reduce(lambda a, b: a + b, nums)
print("sum_all", sum_all)




# extra
print("This is extra it is not related to this topic....")
def operations(n):
    return evens, doubles, cube


evens, doubles, cube = operations(5)
print("even", evens, "doubles", doubles, "cube", cube)
