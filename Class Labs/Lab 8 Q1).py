print("This program will store 10 numbers")
numbers = []
total = 0
average = 0
for i in range(1, 11):
    number = int(input("Enter number #" + str(i) + " : "))
    numbers.append(number)
    total += number
    average = total/i
print("The lowest number in the list: ", min(numbers))
print("The lowest number in the list: ", max(numbers))
print("The total of the number in the list: ", total)
print("The average of the number in the list:  ", average)

