# Attempt problem 1 using while loop. 

num = int(input("Enter number:"))

for i in range(1,11):
    print(num,"*",i,"=",num*i,"\n")

num = int(input("Enter number:"))
i=1; 
while(i<11):
    print(num,"*",i,"=",num*i,"\n")
    i+=1