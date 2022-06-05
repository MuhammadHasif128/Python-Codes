print("Welcome to python buffet catering.")

exception = input("Is buffet held on a weekend (Y/N): ")

if exception == str("n"):
    size = int(input("Enter size of the buffet (ppl): "))
    if size < 100:
        price = 10
        total_price = float(price*size)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")
    elif size <=200:
        price = 8.5
        total_price = float(price*size)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")
    else:
        price = 7
        total_price = float(price*size)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")

if exception == str("y"):
    size = int(input("Enter size of the buffet (ppl): "))
    if size < 100:
        price = 10
        total_price = float(price*size) * (115/100)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")
    elif size <=200:
        price = 8.5
        total_price = float(price*size) * (115/100)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")
    else:
        price = 7
        total_price = float(price*size) * (115/100)
        print("Your buffet for", size, f"people cost $ {total_price:.2f}")


