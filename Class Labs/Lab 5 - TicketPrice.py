age = int(input("Please input your age: "))
day = range(1, 8)

if 4 < age <= 130:
    day = int(input("Please enter the day of the week: "))
    if day in range(1, 6):
        if age < 16:
            print("You have to pay $7.00 for the ticket.")
        elif 16 < age < 65:
            print("You have to pay $10.00 for the ticket.")
        else:
            print("You have to pay $5.50 for the ticket.")
    else:
        print("You have to pay $10 for the ticket")
else:
    print("Error")
