# 24 2) Continue statement

# It is used to skip the current iteration and move to next iteration

# EX 1
i=1
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)

print()
# EX 2
for i in range(0,101):
    if i%3==0 or i%5==0: # Add divisible by both or only one
        continue
    print(i)





