"""word = input("Enter a string: ")
count = 0
for index in word:
    count += 1
if count >= 5:
        if word.endswith("ing"):
            print(word + "ly")
        else:
            print(word + "ing")"""

inputt = input("Please Enter A String: ")
if len(inputt)>= 5:
    if inputt.endswith("ing"):
        print(inputt + "ly")
    else:
        print(inputt + "ing")
