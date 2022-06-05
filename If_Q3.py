print("Welcome to Python Theme Park")
age = int(input("Please enter your age: "))
weight = int(input("Please Enter your weight: "))

if age < 3 and weight > 100:
    print("You are not allowed to take the ride.")
    print("You need to be at least 3 years old and cannot weigh more than 100kg")
elif age < 3 and weight < 100:
    print("You are not allowed to take the ride.")
    print("You need to be at least 3 years old and cannot weigh more than 100kg")
elif age > 3 and weight > 100:
    print("You are not allowed to take the ride.")
    print("You need to be at least 3 years old and cannot weigh more than 100kg")
elif age > 3 and weight < 100:
    print("You are not allowed to take the ride.")
    print("You need to be at least 3 years old and cannot weigh more than 100kg")
else:
    print("Enjoy the ride")
