print("A game where you type numbers from 1-1000 and stop when you want")
print("Type 0 to exit the game")
print("Have fun")
total = 0
numbers = 1

while numbers in range(1, 1000):
    numbers = int(input("Please Input A Value: "))
    print(numbers, "+")
    total += numbers
else:
    print("You stopped the program, your sum of total numbers is,", total)

print("Have a great day!")







