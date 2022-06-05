print("Welcome to Python Wonderland.")

age = int(input("Please Enter Your Age: "))

if age == 0:
    print("Invalid Age")
elif age <= 16:
    print("Please Pay $12.00")
elif 17 <= age <= 20:
    print("Please Pay $25.00")
else:
    print("Please pay $56.00")
