students = int(input("Enter the number of students: "))
count = 0
total = 0

while count < students:
    count +=1
    score = float(input("Enter the exam score of student" + str(count) + ": "))
    total = total + score

average = total/students
print("The average score of this exam is", average)
