"""there are three tests and one exam contributing to the final marks.
 Each test contributes a different percentage and the three tests sum up to 50% of the final marks.
 The exam contributes 50% of the final marks.
 You are tasked to write a program to calculate the final marks of the students, based on the
inputs as follow on the sample screen.
the 50% for tests divide by yourself"""

score1 = int(input("What is your score for Test 1:"))
percentage1 = int(input("What is percentage for Test 1:"))
score2 = int(input("What is your score for Test 2:"))
percentage2 = int(input("What is percentage for Test 2:"))
score3 = int(input("What is your score for Test 3:"))
percentage3 = int(input("What is percentage for Test 3:"))
exam = int(input("What is your score for Exam: "))

Final_Mark = (score1/100)*percentage1 + (score2/100)*percentage2 + (score3/100)*percentage3 + (exam/2)

print ("Your Final Marks is:", Final_Mark)








