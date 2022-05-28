weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight/height**2

if bmi > 27.5:
    print(f"Your BMI is {bmi:.2f}", "and you are Obese")
elif 23 < bmi < 27.5:
    print(f"Your BMI is {bmi:.2f}", "and you are Overweight")
elif 18.5 < bmi < 23:
    print(f"Your BMI is {bmi:.2f}", "and you are Normal")
else:
    print(f"Your BMI is {bmi:.2f}", "and you are Underweight")




