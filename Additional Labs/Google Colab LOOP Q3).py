# My Solution

students = int(input("Enter the number of students: "))
total = 0
average = 0

while True:
    for i in range(1, students+1):
        score = float(input("Enter exam score for student" + str(i) + ": "))
        total = total + score
        average = total/students
    print("The Average Score of this exam is", average)
    break
