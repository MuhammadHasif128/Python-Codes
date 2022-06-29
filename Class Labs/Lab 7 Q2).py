s = input("Enter a string: ")
new_s = 0
for index in range(len(s)):
    if s[index]== ' ': #empty space
        new_s = s[0:index] + s[index+1:]
print(new_s)
