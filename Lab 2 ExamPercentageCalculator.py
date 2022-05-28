test1 = float(input("What is your score for Test 1: "))
percentage1 = float(input("What is your percentage for Test 1: "))
total_percentaged_score1 = (test1 * percentage1)/100
test2 = float(input("What is your score for Test 2: "))
percentage2 = float(input("What is your percentage for Test 2: "))
total_percentaged_score2 = (test2 * percentage2)/100
test3 = float(input("What is your score for Test 3: "))
percentage3 = float(input("What is your percentage for Test 3: "))
total_percentaged_score3 = (test3 * percentage3)/100
exam = float(input("What is your score for exam: "))
exam_percentage = exam * (50/100)

total_marks = total_percentaged_score1 + total_percentaged_score2 + total_percentaged_score3 + exam_percentage

print("Your final mark is", total_marks)




