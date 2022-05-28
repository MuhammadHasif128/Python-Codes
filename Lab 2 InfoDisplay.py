name = input("Enter your name: ")
adminno = input("Enter admin Number: ")
age = input("Enter Age: ")
gender = input("Enter gender (Male / Female): ")
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))
bmi = weight/height**2

print("Hello!", name,"\n""Your admin no is", adminno, "and age is", age,"\n""Your gender is", gender, "and bmi is", bmi )
