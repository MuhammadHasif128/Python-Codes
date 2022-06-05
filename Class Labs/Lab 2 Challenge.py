per_share = float(input("Enter current price for ABC Bank Corporation ($): "))
total_amount_paid = 2000 * per_share
commission = total_amount_paid * (3/100)
selling_amount = total_amount_paid - commission
commission_selling = selling_amount * (2/100)
total_commission = commission + commission_selling
after_commission = selling_amount - commission_selling
profit = selling_amount - after_commission

print("You paid a commission of ($):", total_commission)
print("You have made a profit of ($):", profit)


