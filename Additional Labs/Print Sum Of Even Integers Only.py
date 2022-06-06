number = int(input("Enter a value: "))
total = 0

while number > 2:
    for num in range(3, number+1):
        if num % 2 == 0:
            print(num, end=" ")
            total = total + num
    print("\nTotal Sum of Even Numbers are:", total)
    break
else:
    print("Error")
