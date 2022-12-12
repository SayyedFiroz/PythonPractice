# If user gives you list of elements you need to pass that  list in a function and that function will return value of number of odds and even number

def odd_even(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = []
for i in range(0, 6):
    lst.append(int(input("Enter six numbers in the list :")))
print(lst)

even, odd = odd_even(lst)
print("The even numbers in the list", even)
print("The odd numbers in the list", odd)
