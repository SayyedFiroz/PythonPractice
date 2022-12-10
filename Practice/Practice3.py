# 1 write a code to print all the values from 1 to 100.Skip the number which are divisible by 3 or 5.
import time
start_time = time.time()
i=1
while i<=1000000:
    if i%3!=0 and i%5!=0 :
        print(i)
    i+=1

# 2 write a code to print below pattern.
#####
#####
#####
#####
i=1
while i<=4:
    print("#",end="")
    j=1
    while j<=4:
        print("#",end="")
        j=j+1
    i=i+1
    print()
end_time = time.time()
final_time = end_time - start_time
print(final_time)
