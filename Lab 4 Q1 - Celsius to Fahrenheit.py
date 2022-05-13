while True:
    celsius = (input("Enter Temp in Celsius or Click Quit to exit:"))
    if celsius.upper() == "QUIT":
        print("fuck off")
        break
    else:
        try:
            celsius = float(celsius)
            Fah = 9/5 + celsius + 32
            print(celsius, "degree Celsius in Farenheight is:", Fah)
        except ValueError:
            print("SIKE")











