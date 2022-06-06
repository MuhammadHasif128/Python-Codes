hours = float(input("Enter hours worked: "))
salary = 0

if hours <= 5:
    salary = hours * 5.50
elif hours <= 10:
    salary = 5 * 5.50
    salary = salary + (hours - 5) * 7
else:
    salary = 5 * 5.50
    salary = salary + (5 * 7)
    salary = salary + (hours - 10) * 10
print(f"You have earned, {salary:.2f}", "today!")

