s=int(input("enter a value: ")) #seconds
h=s//3600 #hours
m=(s-(h*3600))//60
seconds=(s-(h*3600)-(m*60))
print(s, "seconds is", h, "hours", m, "minutes and", seconds, "seconds")

#a)runtime error, input validation text
#b)while loop&for loop

