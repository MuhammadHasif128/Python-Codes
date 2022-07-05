word = input("Enter a string: ")
count = 0

for index in word:
    if index.isupper() == True:
        count = count + 1
if count >= 2:
    print(word.upper())
else:
    print("The String Contains less than 2 uppercase characters")
