age = int(input("Please Enter Your Age: "))
print("Monday is 1 to Sunday is 7")

while True:
    if age > 130:
        print("Too old. Invalid Age")
        break
    if age > 4 and age <= 130:
        day = int(input("enter the day of the week: "))
    if day >= 6 and day <= 7:
        print("Pay $10")
        break
    elif day in range(1, 6):
        if age < 16:
            print("You have to pay $7.50")
            break
        elif age >= 16 and age < 65:
            print("You have to pay $10")
            break
        else:
            print("You have to pay $5.50")
            break

else:
    print("Have a nice day")








