a = {"Jane": 75, "John": 60, "Jerome": 81 }

for key, value in a.items():
    print(key, value)

print("============")

name = input("Enter student name: ")

if name in a:
    print(a[name])
