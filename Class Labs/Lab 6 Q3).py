cost_price = int(input("Please Input Your Cost Price: "))
while cost_price > 0:
    selling_price = (25/100) * cost_price
    x = cost_price + selling_price
    print(x)
    cost_price = int(input("Please Input Your Cost Price: "))
while cost_price == 0 or cost_price < 0:
    print("error")
    break
print("Goodbye :D")






