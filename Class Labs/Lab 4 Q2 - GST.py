unitprice = float(input("Enter Your Unit Price: "))
copies = float(input("Enter number of copies: "))
total = unitprice * copies
gst = total * (7/100)
total_amount = total + gst

print(f"Subtotal:($){total:.2f}")
print(f"GST:($){gst:.2f}")
print(f"Total Amount:($){total_amount:.2f}")

