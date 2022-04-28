#BuyComm = (0.40*2000)*0.03
#CurrentPrice
#TotalComm = BuyComm + SellComm
#SellComm = (CurrentPrice * 2000) * 0.02

#Profit = SellPrice(CurrentPrice*2000) - BuyPrice(0.40*2000) - TotalComm
#Profit = -100 (made a loss of (-1*Profit)


current_price = float(input("Enter current price for ABC Bank Corporation (S$): "))

amount_paid = (2000 * 0.40)
amount_sold = amount_paid * current_price
paid_commission = amount_paid * 0.03
selling_commission = (current_price * 2000) * 0.02
total_commission = paid_commission + selling_commission
profit = amount_sold - amount_paid - total_commission


print("Your paid total commission of (S$): ", total_commission)
print("You have made a profit of (S$): ", profit)







