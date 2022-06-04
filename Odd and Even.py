list = []
even_count = 0
odd_count = 0
for num in range(1, 6):
    list = int(input("Enter number" + str(num) + ": "))
    if list % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even #", even_count)
print("Odd #", odd_count)
