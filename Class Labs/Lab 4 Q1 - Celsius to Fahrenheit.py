while True:
    degree = input("Enter your temperature: ")
    if degree.upper() == "QUIT":
        print("bye")
    else:
        try:
            degree = float(degree)
            fahrenheit = 9/5 * degree + 32
            print(fahrenheit)
        except ValueError as a:
            print("Error")

#try:
#degree = int(input("Enter your temperature: "))
#fahrenheit = 9/5 * degree + 32
#print("Your temperature in fahrenheit:", fahrenheit)
#except ValueError as a:
#print("Error")

#a)runtime error, input validation text
#b)while loop&for loop











