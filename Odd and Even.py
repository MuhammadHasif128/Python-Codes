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

"""even = 0
odd = 0
num = 1

while num in range(1, 6):
    x = int(input("Enter Number" + str(num) + ": "))
    num += 1
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even #", even)
print("Odd #", odd)"""

