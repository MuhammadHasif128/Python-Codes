credit = 0
grade_point_average = 0

for i in range(1, 6):
    credit_module = float(input("Enter the credit for Module" + str(i) + ": "))
    GPA_module = float(input("Enter the GPA for Module" + str(i) + ": "))
    credit += credit_module
    grade_point_average += credit_module * GPA_module
    GPA = grade_point_average / credit
print(f"Your cumulative GPA for 5 Modules is: {GPA:.2f}")





