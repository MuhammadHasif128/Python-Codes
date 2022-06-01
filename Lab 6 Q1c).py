sum = 1
num = int(input("Enter Number: "))
new_sum = 0

if num < 2:
    print("Error")

else:
    while sum <= num:
        if sum % 2 == 0:
            new_sum += sum
            print(new_sum)
        sum +=1

    print(new_sum)


#1c) sum = 0
#num = int(input("Enter the number: "))
#if num < 2:
   # print("Sike")
#else:
    #for i in range (2, num+1,2):
        #sum = sum + i

    #print("the sum is", num, "is:", sum)





