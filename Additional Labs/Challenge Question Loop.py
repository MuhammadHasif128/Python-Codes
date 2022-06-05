studentNO = int(input("How many students do you have? "))
testNo = int(input("How many test for your module? "))

# The answer from input (outer loop) will determine your output

for s in range(1, studentNO+1):
    print("\n******* Student # ", s, "*******")
    totalTestMk = 0
# print can be anything
    for t in range(1, testNo+1):
        testMark = float(input("Test number" + str(t) + ":"))
        totalTestMk = totalTestMk + testMark
    print("The average for student #", s, "is", ":", totalTestMk/testNo)
# input function must be string
# testMark will loop. The outer one wont loop. Only for loop will loop

# revise nested if else and nested loops
# know how to use modulus for even odd number
# when the program ends depending on what the user wants, for lol im range(1, variable+1):
# end = "" horizontal
# by default print vertical line
# put name before u do ur python questions
