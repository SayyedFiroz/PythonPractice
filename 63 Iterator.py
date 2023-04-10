# iteratir in depth


"""nums = [7,73,43,3]

print(nums[1])

for i in nums:
    print(i)

print("....iter function...")
it = iter(nums)           # we don't use to index value

print(it.__next__())"""

# own object iterator

class topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):  # To create object
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = topten()


print(next(values))


for i in values:
    print(i)


