credit = 0
grade_point_average = 0

for modules in range(1,6):
    credit = float(input("Enter the credit for Module" + str(modules) + ": "))
    credit +=1
    grade_point_average = float(input("Enter your GPA for Module" + str(modules) + ": "))
    grade_point_average +=1
    grade_point = grade_point_average * credit
    overall_gpa = grade_point//5
print(f"Your cumulative GPA for 5 modules is: {overall_gpa:.2f}")

