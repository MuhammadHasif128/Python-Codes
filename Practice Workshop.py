print("Welcome to python zoo.")
name = input("Please Enter Your Name: ")
age = int(input("Enter your age: "))
day = int(input("Enter day (0-7): "))

if 1 < day <= 5:
    print("Hi", name, ",", "Please Pay $10")
elif 6 <= day <=7:
    if age < 21:
        print("Hi", name, ",", "Please Pay $15")
    elif 21 <= age <= 60:
         print("Hi", name, ",", "Please Pay $60")
    else:
        print("Hi", name, ",", "Please Pay $20")
