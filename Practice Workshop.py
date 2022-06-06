count = 1
total = 0
while True:
    item = float(input("Please Enter Price For Item " + str(count) + ": "))
    count +=1
    total += item
    if item == 0 and count == 1:
        print("You did not buy any item.\nHave a nice day. Looking forward to see you again")
        break
    elif item == 0 and count > 1:
        print("You have bought", count-2, "items at the total price of", total,"\nHave a nice day. Looking forward to see you again.")
        break






