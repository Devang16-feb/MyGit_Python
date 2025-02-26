# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 

n = 3

i = 0
j = 0
for i in range(0,n):
    for j in range(0,(2*i)+1):
        print("*",end="")
    print("\n")

#   * 
#  *** 
# ***** for n = 3 

i = 0
j = 0
iStart = n-1
iEnd = n-1

for i in range(0,n):
    iStart = (n-1)-i
    iEnd = (n-1)+i
    for j in range(0,2*n-1):
        if(j>=iStart and j<=iEnd):
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")
    
# ANother Easy Approch :
#   * 
#  *** 
# ***** for n = 3 

n = int(input("Enter number:"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")