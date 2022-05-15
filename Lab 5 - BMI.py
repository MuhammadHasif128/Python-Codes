weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight/height**2

if BMI >=27.5:
    print("OBESE")
elif BMI >23 and BMI <27.5:
    print("OVERWEIGHT")
elif BMI >18.5 and BMI <23:
    print("NORMAL")
else:
    print("UNDERWEIGHT")





