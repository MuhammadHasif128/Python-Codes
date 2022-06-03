"""every ques new python file in folder

at the end of it, zip file

for loop (count loop)
i = count variable
5 = always start 0 end 1 number bfr end number 4
(1,5) = 1,2,3,4
inclusive of 5 = (1,6)
(1(start), 2(end), 3(steps, how many times it w jump))

while loop (condition loop)"""

"""for i in range (1, 101):
    if i % 2 == 0:
        print (i)"""

#print indent impt

#for i in range (1, 100+1):
   # if i % 2 == 0:
    #    print(i)

#can be +/- 1

#sum = sum +1 (accumulate)
#sum +=1
#always initial variable bfr incrementing it

#debug, right click python file, step through, troubleshoot

#while loop, so long its true run, false, end loop, wht is true that w make it keep going
#while loop need specify range and add manually, intial value too. change value.

total = 0
num = int(input("Please Enter A Number: "))

for i in range(1, num+1, 1):
    total += i
    print (i, "+", end="")
print("New Sum Is", num, "numbers is:", total)

#ask how to make loop statements vertical, horizontal like how the question wants it to be






