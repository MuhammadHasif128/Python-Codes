age = int(input("Please Enter Your Age:"))

if age >=4 and age <=130:
    day = int(input("Enter the day of the week:"))
    if day >5 and day <=7:
        print("Pay $10 sial")
    elif day in range(1,6):
        if age < 16:
            print("You have to pay $7.50")
        elif age >=16 and age <65:
            print("You have to pay $10.00")
        else:
            print("You have to pay 5.50")
else:
    print("Error, bye cb")








if age < 16:
    print("You have to pay $7.50")
elif age >=16 and age <65:
    print("You have to pay $10.00")
else:
    print("You have to pay 5.50")








