print("Please enter your Review Exercise answer")
answers = []
model_answers = ["c", "d", "b", "a", "b", "d", "a", "c", "d", "c"]
correct_answer = 0
wrong_answer = 0
for i in range(1, 11):
    question = input("MCQ #" + str(i) + ": ")
    answers.append(question)
for i in range(0, 10):
    if answers[i] == model_answers[i]:
        correct_answer += 1
    else:
        wrong_answer += 1
print("You have", str(correct_answer), "correct answers and", str(wrong_answer), "wrong answers")


