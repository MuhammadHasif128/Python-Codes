"""s = input("Enter a string: ")
new_s = ' '
if len(s) >= 5:
    if s[-3] == "ing":
        s = s + "ly"
    else:
        new_s = s + "ing"
    print(new_s)
else:
    print("The string is <5 characters long.")"""

inputt = input("Please Enter A String: ")
if len(inputt)>= 5:
    if inputt.endswith("ing"):
        print(inputt + "ly")
    else:
        print(inputt + "ing")
