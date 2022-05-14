price = float(input("Please Enter the Price of your Item:$ "))
rounded_gst = round(price*(7/100), 2)
total_price = price+rounded_gst
print("Subtotal:$ ", price)
print("GST:$ ", rounded_gst)
print("Total Amount:$ ", total_price)

#x = 3.13433#
#print(round(x,2))#


