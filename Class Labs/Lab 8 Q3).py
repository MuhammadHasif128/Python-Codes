scores = {
    'Jane': 75,
    'John': 60,
    'Jerome': 81,
}

input_name = input("Enter a student name: ")

if input_name in scores:
    attempt = scores[input_name]
    print("Results for English: " + str(attempt))
else:
    print("There is no result for " + input_name)
