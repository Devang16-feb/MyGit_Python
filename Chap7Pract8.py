# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  

n = 5
i = 0
j = 0

for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or j == 0 or i == n-1 or j == n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")
    
# Other Approch :

n = int(input("Enter number:"))
for i in range(1,n+1):
    if(i == 1 or i == n):
        print("*"*n, end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")