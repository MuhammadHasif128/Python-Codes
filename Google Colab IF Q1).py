hours = int(input("Enter Hours: "))
hr_rate = int(input("Enter Hourly Rate: "))
Pay = hours * hr_rate

if hours > 40:
    Pay = 40*10 + (hours - 40) * (hr_rate * 1.5)
    print("Please pay $", Pay)
else:
    print("Please pay $", Pay)
