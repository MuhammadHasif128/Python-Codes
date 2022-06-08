print("Welcome to python fast food restaurant.\n")
print("Menu\n====")
print("0) Buy Burger\n1) Buy Drink")

total = 0

order = int(input("Please enter your order: "))

while order == 0 or order == 1:
    if order == 0:
        burger = int(input("How many burger for this order: "))
        for i in range(1, burger+1):
            price = float(input("Enter price for burger" + str(i) + ":"))
            total += price
    elif order == 1:
        drink = int(input("How many drink for this order: "))
        for i in range(1, drink+1):
            price = float(input("Enter price for drink" + str(i) + ":"))
            total += price
    break
print("Total price now is $", total)
exception = input("Do you have more orders (Y/N)?: ")
if exception.upper() == str("Y"):
   order = int(input("Please enter your order: "))
   while order == 0 or order == 1:
    if order == 0:
        burger = int(input("How many burger for this order: "))
        for i in range(1, burger+1):
            price = float(input("Enter price for burger" + str(i) + ":"))
            total += price
    elif order == 1:
        drink = int(input("How many drink for this order: "))
        for i in range(1, drink+1):
            price = float(input("Enter price for drink" + str(i) + ":"))
            total += price
    break
elif exception.upper() == str("N"):
    print("Bye")
print("Thank you. Please Pay", total)
