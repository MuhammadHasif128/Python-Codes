total_price = 0
count = 1

while True:
    item = float(input("Please Enter Price For Item " + str(count) + ":"))
    if item == 0 and count == 1:
         print("You did not buy any item.\nHave a nice day. Looking forward to see you again")
         break
    if item == 0 and count > 1:
         count -= 1
         print("You have bought", count, "items at the total price of $", total_price, "Have a nice day. Looking forward to see you again")
         break
    elif item > 0:
        count += 1
        total_price = total_price + item

"""total_price = 0
count = 1
no_of_item = 0

while True:
    item = float(input("Please Enter Price For Item " + str(count) + ":"))
    if item > 0:
        total_price += item

    elif item == 0 and count == 1:
         print("You did not buy any item.\nHave a nice day. Looking forward to see you again")
         break

    elif item == 0 and count > 1:
         print("You have bought", no_of_item, "items at the total price of $", total_price, "Have a nice day. Looking forward to see you again")
         break

    count += 1
    no_of_item += 1"""
