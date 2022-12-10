


nums = [12,15,18,21,25]
for i in  nums:
        if i % 5 == 0:
            print(i)
            break   # if only need one value

# if we don't have any value
nums = [12,16,18,21,26]
for i in  nums:
        if i % 5 == 0:
            print(i)
        else:
            print("Not found")
            break
