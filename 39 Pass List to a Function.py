# If user gives you list of elements you need to pass that  list in a function and that function will return value of number of odds and even number

def odd_even_list(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = [2, 323, 244, 2, 2323, 3232]
even, odd = odd_even_list(lst)

print(even)
print(odd)
