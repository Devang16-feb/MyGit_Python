# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * 

def pattern(n):
    for i in range(n,0,-1):
        print("*"*i,end="")
        print("")
        
pattern(3)