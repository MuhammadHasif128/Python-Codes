module_1 = int(input("Please Enter your module 1 test marks (total 100): "))
module_2 = int(input("Please Enter your module 2 test marks (total 100): "))

if module_1 >= 80 and module_2 >= 80:
    print("Good Job. GPA is still 4.0!")
else:
    print("GPA is now < 4.0. Keep Trying.")
