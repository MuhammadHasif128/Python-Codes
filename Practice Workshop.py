print("I will convert your values in SECONDS to hours, minutes, seconds")

value = int(input("Enter value: "))

hours = value//3600
minutes = (value//60)-(hours*60)
seconds = value - (hours*3600) - (minutes*60)

print(value, "seconds is", hours,"hours", minutes,"minutes and", seconds,"seconds.")
