s = input("Enter a string: ")
new_s = '' # empty string
for index in range(len(s)):
    if index%2 == 0:
        new_s = new_s + s[index].upper() # even to uppercase
    else:
        new_s = new_s + s[index]
print(new_s)
