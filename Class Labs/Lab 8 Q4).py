scores = {
    'Jane': [75, 80, 85],
    'John': [60, 68, 74],
    'Jerome': [81, 63, 77],
    'Jason': [55, 76, 67],
    'Jessica': [62, 45, 68],
    'Joanne': [52, 47, 51]
}

input_name = input("Enter student name: ")
if input_name in scores:
    results = scores[input_name]
    total = results[0] + results[1] + results[2]
    avg_result = total/3
    print("Results of " + input_name)
    print("===========================================")
    print("Results For English = " + str(results[0]))
    print("Results For Math = " + str(results[1]))
    print("Results For Science = " + str(results[2]))
    print("Average marks of " + input_name + " = " + f"{avg_result:.2f}")
else:
    print("name not found")









