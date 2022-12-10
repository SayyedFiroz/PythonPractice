# 24 1) Break Statement

# Break is used terminate the current loop (while or FOR) and return to the next statement

# Ex Vending machine is out of stock

Available = 5
x = int(input("Enter the number of candy you want :"))
i = 1
while i<x:
    if i>Available:
        print("Out of Stock 😔")
        break
    i+=1
    print("CANDY")


print("Thank you")
